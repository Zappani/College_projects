//***********************************************************************
/*
Programa desenvolvido por Lucas Zappani Siqueira e Gustavo Henrique Sanches
para o projeto de desenvolvimento de um AGV de baixo custo para estudo da
funcionalidade da tecnologia em warehouses.
O projeto foi uma parceiria entre a Univerdade Federal do Paraná (UFPR)
e a empresa Neodent.
*/

//**************************instruções**********************************
  /*
  Este programa tem a finalidade de controlar a navegação do AGV
  Nele pode ser encontrado funções relacionadas ao controle dos drivers dos 
  motores, ativação da sirene de segurança e leitura de cartões RFID
  NÃO É RECOMENDADA A ALTERAÇÃO DESSE PROGRAMA
  */
//**************************bibliotecas*********************************
  #include <SPI.h>
  #include <MFRC522.h>
  #include <LiquidCrystal.h>

//**************************keyPadLcd***********************************
  LiquidCrystal lcd(8, 10, 4, 5, 6, 7);
  
  void leBotao();
  
  int valor = 0x00;                                      //armazena o valor digital do conversor AD

  boolean direita    = 0x00, butt01 = 0x00,
          cima       = 0x00, butt02 = 0x00,
          baixo      = 0x00, butt03 = 0x00,
          esquerda   = 0x00, butt04 = 0x00,
          seleciona  = 0x00, butt05 = 0x00;
          
//**************************rodas***************************************
  #define freioE 3      // freio em ativo em 1E***
  #define speedE 2      // velocidade da rotacao E***

  #define freioD 11     // freio em ativo em 1D***
  #define speedD 12     // velocidade da rotacao D***

  #define dirD 32       // direção roda direita
  #define dirE 30       // direção roda esquerda

  int velocD;           //velocidade da roda direita E
  int velocE;           //velocidade da roda esquerda D

  int b = 0;
  float i = 1.0;

//**************************infravermelho*******************************
  #define ir1 A0
  #define ir2 A1
  #define ir3 A2
  #define ir4 A3
  #define ir5 A4

//**************************rfid****************************************
  #define RST_PIN   49 
  #define SS_PIN    53

  String strID = "";   //armazena UID

  MFRC522 mfrc522(SS_PIN, RST_PIN);   // Cria  instancia MFRC522

  int a;

//**************************segurança***********************************
  #define sinalUno 13

  #define sirene 33

  bool x = 0;
  int s = 0;

//**************************funções*************************************//
  //**************************keyPadLcd*********************************
    void leBotao(){

        valor = analogRead(A5);                       

        if      (valor <  50)                 butt01 = 0x01;
        else if (valor > 70 && valor < 150)   butt02 = 0x01;
        else if (valor > 160 && valor < 300)  butt03 = 0x01;
        else if (valor > 310 && valor < 500)  butt04 = 0x01;
        else if (valor > 560 && valor < 800)  butt05 = 0x01;

        if (valor > 50 && butt01){                      //Botão direita solto e flag butt01 setada?
          butt01 = 0x00;                                //Limpa flag butt01
          direita  = 0x01;                   
                      //Seta flag direita    
        }

        if (valor > 150 && butt02){                     //Botão cima solto e flag butt02 setada?
          butt02 = 0x00;                                //Limpa flag butt02
          cima   = 0x01;                                //Seta flag cima
        } 

        if (valor > 300 && butt03){                     //Botão baixo solto e flag butt03 setada?
          butt03 = 0x00;                                //Limpa flag butt03
          baixo  = 0x01;                                //Seta flag baixo
        }

        if (valor > 500 && butt04){                     //Botão esquerda solto e flag butt04 setada?
          butt04 = 0x00;                                //Limpa flag butt04
          esquerda   = 0x01;                            //Seta flag esquerda
        } 

        if (valor > 800 && butt05){                     //Botão esquerda solto e flag butt05 setada?
          butt05 = 0x00;                                //Limpa flag butt04
          seleciona   = 0x01;                           //Seta flag esquerda
        }
        
    } 
    void parada(){//lista de opções para o usuario escolher   
    
      while(1){ 
        
        paraRoda();

        lcd.setCursor(0,0);
        lcd.print("Iniciar trajeto?");

        lcd.setCursor(0,1);
        lcd.print("Select para sim");

        leBotao();

        if (direita == 0x01){
          direita = 0x00;                              //Seta flag direita    
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Opcao invalida!");
          delay(1500);
        }

        if (cima == 0x01){
          cima = 0x00;                                 //Seta flag cima
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Opcao invalida!");
          delay(1500);
        }

        if (baixo == 0x01){
          baixo = 0x00;                                //Seta flag baixo
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Opcao invalida!");
          delay(1500);
        }

        if (esquerda == 0x01){
          esquerda = 0x00;                             //Seta flag esquerda
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Opcao invalida!");
          delay(1500);
        }

        while()
        if (seleciona == 0x01){
          seleciona = 0x00;
          i = 1.0;                             //Seta flag esquerda
          carga();
          strID = "";
          break; 
        }
      }
      
    }
    void carga(){
      
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Nivel de carga:    ");
      delay(1500);
      
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("1-Vazio 2-Leve  ");
      lcd.setCursor(0,1);
      lcd.print("3-Medio 4-Pesado");
      delay(1500);
      
      while(1){
        
        i = 1;
        leBotao();

        if(direita == 0x01){
          
          direita = 0x00;                              //Seta flag direita    
          lcd.clear();
          lcd.setCursor(0,0);                          //Posiciona cursor na coluna 2, linha 1
          lcd.print("Vazio!");
          delay(2000);
          i = i*4/5;//-20%   
          velocD = 10*i;
          velocE = 10*i;

          andaFrente();
          delay(1000);

          break;
        }

        if(cima == 0x01){
          cima = 0x00;                                 //Seta flag cima
          lcd.clear();
          lcd.setCursor(0,0);                          //Posiciona cursor na coluna 2, linha 1
          lcd.print("Leve!");
          delay(2000);
 
          i = i*19/20;//-5%
          velocD = 10*i;
          velocE = 10*i;


          andaFrente();
          delay(1000);

          break;
        }

        if(baixo == 0x01){
          
          baixo = 0x00;                                //Seta flag baixo
          lcd.clear();
          lcd.setCursor(0,0);                          //Posiciona cursor na coluna 2, linha 1
          lcd.print("Medio!");
          delay(2000);

          i = i*53/50;//+6%
          velocD = 10*i;
          velocE = 10*i;

          andaFrente();
          delay(1000);

          break;
        }

        if(esquerda == 0x01){

          esquerda = 0x00;                             //Seta flag esquerda
          lcd.clear();
          lcd.setCursor(0,0);                          //Posiciona cursor na coluna 2, linha 1
          lcd.print("Pesado!");
          delay(2000);
          
          i = i*117/100;//+15%
          velocD = 10*i;
          velocE = 10*i;

          andaFrente();
          delay(1000);

          break;
        }

        if(seleciona == 0x01){

          seleciona = 0x00;                             //Seta flag esquerda
          lcd.clear();
          lcd.setCursor(0,0);                           //Posiciona cursor na coluna 2, linha 1
          lcd.print("Opcao invalida!");
          delay(2000);
          lcd.clear();
          
          carga();

          break;
        }
        
      }
    }
    void Ativa(){
      
      leBotao();
  
      if(direita == 0x01){                               //tecla direita pressionada?
        direita = 0x00;                                  //limpa flag da tecla
      }
      if(cima == 0x01){                                  //tecla cima pressionada?
        cima = 0x00;                                     //limpa flag da tecla
      }   
      if(baixo == 0x01){                                 //tecla baixo pressionada?
        baixo = 0x00;                                    //limpa flag da tecla
      }   
      if(esquerda == 0x01){                              //tecla esquerda pressionada?
        esquerda = 0x00;                                 //limpa flag da tecla
      }
      if(seleciona == 0x01){                             //tecla select pressionada?
        seleciona = 0x00;                                //limpa flag da tecla
      } 
    }
  //**************************rodas*************************************
    void viraEsquerda(){//agv faz curva para a esquerda
      digitalWrite(freioD, 0);  
      digitalWrite(freioE, 0);

      digitalWrite(dirE, 0);
      digitalWrite(dirD, 1);

      analogWrite(speedE, velocE);
      analogWrite(speedD, velocD);
    }
    void viraDireita(){//agv faz curva para a direita
      digitalWrite(freioE, 0);
      digitalWrite(freioD, 0);

      digitalWrite(dirE, 1);
      digitalWrite(dirD, 0);

      analogWrite(speedE, velocE);
      analogWrite(speedD, velocD);
    }
    void paraRoda(){//freia as rodas do agv
      velocD = 0;
      velocE = 0;

      analogWrite(speedE, velocE);
      analogWrite(speedD, velocD);

      digitalWrite(freioE, 1);
      digitalWrite(freioD, 1);  

    }
    void andaFrente(){//faz o agv andar para frente
      digitalWrite(dirE, 1);
      digitalWrite(dirD, 1);

      analogWrite(speedE, velocE);
      analogWrite(speedD, velocD);

      digitalWrite(freioE, 0);
      digitalWrite(freioD, 0);     
    }
    void vaideRe(){//faz o agv andar para frente
      velocE = 9*i;
      velocD = 9*i;

      digitalWrite(dirE, 0);
      digitalWrite(dirD, 0);

      analogWrite(speedE, velocE);
      analogWrite(speedD, velocD);

      digitalWrite(freioE, 0);
      digitalWrite(freioD, 0);  
      delay(10);   
    }
    void checaLinha(){

      for(int i = 0; i <= 300; i ++){
          
        int x1 = digitalRead(ir1);  //Sensor mais a esquerda
        int x2 = digitalRead(ir2);  //Sensor a esquerda
        int x3 = digitalRead(ir3);  //Sensor central
        int x4 = digitalRead(ir4);  //Sensor a direita
        int x5 = digitalRead(ir5);  //Sensor mais a direita

        if((x1 == 0) &&  (x2 == 0) &&  (x3 == 0) &&  (x4 == 0) &&  (x5 == 0)){
  
          if(i == 300){
            /*lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("FORA DA LINHA  ");*/
            
            while(1){
              paraRoda();
            }

          }else{
            vaideRe();
            //Serial.println("Indo de re");
          }
        }else{
          //Serial.println("Voltei a linha");   
          break;   
        }
        //delay(10); 
      }
    }

  //**************************infraverm*********************************  
    void infrared(){//condicionais de leitura do sensor infra vermelho
      //**************************leitura dos valores dos sensores***********
        int s1 = digitalRead(ir1);  //Sensor mais a esquerda
        int s2 = digitalRead(ir2);  //Sensor a esquerda
        int s3 = digitalRead(ir3);  //Sensor central
        int s4 = digitalRead(ir4);  //Sensor a direita
        int s5 = digitalRead(ir5);  //Sensor mais a direita

      //**************************tudo ou nada******************************* 
        if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){//NADA
          
          checaLinha(); 
        }  
        
        if((s1 == 1) && (s2 == 1) && (s3 == 1) && (s4 == 1) && (s5 == 1)){//TODOS 
          
          velocD=10*i;
          velocE=15*i;
          viraDireita();
          delay(30);
          
        } 
        
      //**************************seguir em frente***************************
        if((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 0) && (s5 == 0)){//1 - seguir em frente
          velocD=11*i;
          velocE=11*i;
          andaFrente(); 
          //delay(20);
        }
        if((s1 == 0) && (s2 == 1) && (s3 == 1) && (s4 == 1) && (s5 == 0)){//2 - seguir em frente
          velocD=11*i;
          velocE=11*i;
          andaFrente();
          //delay(15);  
        }
        if((s1 == 0) && (s2 == 1) && (s3 == 1) && (s4 == 0) && (s5 == 0)){//3 - seguir em frente
          velocD=22*i;
          velocE=8*i;
          andaFrente();
          delay(9);
        } 
        if((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 1) && (s5 == 0)){//5 - seguir em frente
          velocD=8*i;
          velocE=22*i;
          andaFrente();
          delay(9);
        }
        if((s1 == 1) && (s2 == 1) && (s3 == 1) && (s4 == 1) && (s5 == 0)){//7 - seguir em frente
          velocD=11*i;
          velocE=11*i;
          andaFrente();
          delay(50);
        }
        if((s1 == 1) && (s2 == 0) && (s3 == 1) && (s4 == 1) && (s5 == 0)){//8 - seguir em frente
          velocD=11*i;
          velocE=11*i;
          andaFrente();
          delay(50);
        }
        if((s1 == 0) && (s2 == 1) && (s3 == 1) && (s4 == 1) && (s5 == 1)){//9 - seguir em frente
          velocD=11*i;
          velocE=11*i;
          andaFrente();
          delay(50);
        }

      //**************************virar para esquerda************************
        if((s1 == 1) && (s2 == 1) && (s3 == 1) && (s4 == 0) && (s5 == 0)){//4 - seguir em frente // ir menos para a esquerda
          velocD=15*i;
          velocE=12*i;
          //andaFrente();
          viraEsquerda();
          delay(10);
        }
        if((s1 == 1) && (s2 == 1) && (s3 == 0) && (s4 == 0) && (s5 == 0)){//ir para a esquerda
          velocD = 20*i;
          velocE = 12*i;
          viraEsquerda(); 
          delay(15);
        }
        if((s1 == 0) && (s2 == 1) && (s3 == 0) && (s4 == 0) && (s5 == 0)){//ajeita para a esquerda
          velocD = 20*i;
          velocE = 12*i;
          viraEsquerda();
          delay(15);
        }
        if((s1 == 1) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 0)){//ir bastante para a esquerda
          velocD = 32*i;
          velocE = 17*i;
          viraEsquerda();
          delay(50);
        }
      
      //**************************virar para direita************************* 
        if((s1 == 0) && (s2 == 0) && (s3 == 1) && (s4 == 1) && (s5 == 1)){//6 - seguir em frente // ir menos para a direita
          velocD=12*i;
          velocE=15*i;
          //andaFrente();
          viraDireita();
          delay(10);
        }  
        if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 1) && (s5 == 0)){//ajeita para a direita
          velocE = 20*i;
          velocD = 12*i;
          viraDireita();
          delay(15);
        }
        if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 1) && (s5 == 1)){//ir para a direita
          velocE = 20*i;
          velocD = 12*i;
          viraDireita();
          delay(15);
        }
        if((s1 == 0) && (s2 == 0) && (s3 == 0) && (s4 == 0) && (s5 == 1)){//ir bastante para a direita
          velocE = 32*i;
          velocD = 17*i;
          viraDireita();
          delay(50);
        }
    }

  //**************************rfid**************************************
    void rfid(){//faz leitura da UID do cartão RFID

      if ( ! mfrc522.PICC_IsNewCardPresent() || ! mfrc522.PICC_ReadCardSerial() ) {
        return;
      }
      for (byte i = 0; i < 4; i++){
        strID += (mfrc522.uid.uidByte[i] < 0x10 ? "0" : "") 
        + String(mfrc522.uid.uidByte[i], HEX);
      }
      if( strID == "d0c6f332" || strID == "b0645132" || strID == "652e6441" 
       || strID == "f59f6541" || strID == "c51b8a41" || strID == "758e5241"
       || strID == "45d23741" || strID == "65a76441" || strID == "25d27d41" 
       || strID == "65874341" || strID == "35303641" || strID == "756c5441"
       || strID == "6a014924" || strID == "9a234c25" || strID == "1a835a24"
       || strID == "1a834624" || strID == "ea4a4024" || strID == "6ab52124"
       || strID == "0aeea3c6" || strID == "daa1a0c6" || strID == "5ae04025"
       || strID == "8aa74524" ){//inicio
       
        paraRoda();
        ativaSirene();
        parada();
      }
    }
  //**************************segurança*********************************
    void ativaSirene(){
      digitalWrite(sirene, 1);
      delay(3000);
      digitalWrite(sirene, 0);
    }
//**************************SetupAndLoop********************************
 
  void setup(){

    lcd.begin(16,2);                                    
    Serial.begin(9600);  

    SPI.begin(); 
    mfrc522.PCD_Init();

    pinMode(freioE, OUTPUT);
    pinMode(freioD, OUTPUT);

    pinMode(speedE, OUTPUT);
    pinMode(speedD, OUTPUT);

    pinMode(dirE, OUTPUT);
    pinMode(dirD, OUTPUT);

    digitalWrite(dirE, 1);
    digitalWrite(dirD, 1);

    pinMode(ir1, INPUT);
    pinMode(ir2, INPUT);
    pinMode(ir3, INPUT);
    pinMode(ir4, INPUT);
    pinMode(ir5, INPUT);

    pinMode(sinalUno, INPUT);

    pinMode(sirene, OUTPUT);

    lcd.setCursor(0,0);
    lcd.print("CARTAGENA AGV");
    delay(1500);
    lcd.clear();

    carga();
    
  } 

  void loop(){

    x = digitalRead(sinalUno);

    if(x == 0){
      rfid();
      infrared();
    }else{

      paraRoda();
      ativaSirene();      
    }

  } 















