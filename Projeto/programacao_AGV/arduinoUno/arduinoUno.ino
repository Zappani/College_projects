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
  Este programa tem por finalidade controlar o arduino uno do qual é responsavel 
  pelo sensoriamento do trajeto utilizando 4 sensores ultrassonicos.
  Modificando este programa é possivel controlar a distancia de acionamento por meio
  do parametro de leitura e tambem visualizar a distancias lidas.
  */

//**************************bibliotecas*********************************
  
  #include <HCSR04.h>

//**************************inicialização*******************************
  
  HCSR04 hc1(3,2);//trig pin , echo pin
  HCSR04 hc2(5,4);//trig pin , echo pin
  HCSR04 hc3(7,6);//trig pin , echo pin
  HCSR04 hc4(9,8);//trig pin , echo pin

  #define freioMega 13 

//**************************SetupAndLoop********************************

  void setup(){ 

    Serial.begin(9600);
  
    pinMode(freioMega, OUTPUT);

    digitalWrite(freioMega, 0);
    delay(1500);
  }

  void loop(){ 
  
    Serial.print("Sensor 1:");
    Serial.println( hc1.dist() ); //retorna a distancia na serial
    Serial.print("Sensor 2:");
    Serial.println( hc2.dist() ); //retorna a distancia na serial
    Serial.print("Sensor 3:");
    Serial.println( hc3.dist() ); //retorna a distancia na serial
    Serial.print("Sensor 4:");
    Serial.println( hc4.dist() ); //retorna a distancia na serial*/
    
    if(hc1.dist()< 45 || hc2.dist()< 45 || hc3.dist()< 45 || hc4.dist() < 45){
      digitalWrite(freioMega, 0); 
      delay(1500);
    }else{
      digitalWrite(freioMega, 1); 
    }
    
  }
