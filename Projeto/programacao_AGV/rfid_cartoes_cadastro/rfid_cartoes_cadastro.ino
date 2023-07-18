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
  Este programa tem por finalidade realizar a leitura via Serial, com um laptop 
  ou desktop, do codigo de identificação de cartões RFID para posterior programação
  com os mesmos no código do aruino mega.
  */

//**************************bibliotecas*********************************
  
  #include <SPI.h>
  #include <MFRC522.h>

//**************************inicialização*******************************
  
  #define RST_PIN   5     // Configurable, see typical pin layout above
  #define SS_PIN    53    // Configurable, see typical pin layout above

  MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance

//**************************SetupAndLoop********************************

  void setup() {
    Serial.begin(9600);  // Initialize serial communications with the PC
    SPI.begin();         // Init SPI bus
    mfrc522.PCD_Init();  // Init MFRC522
  }

  void loop() {
    
    if ( ! mfrc522.PICC_IsNewCardPresent() || ! mfrc522.PICC_ReadCardSerial() ) {
      return;
    }
      
    String strID = "";
    for (byte i = 0; i < 4; i++) {
      strID += (mfrc522.uid.uidByte[i] < 0x10 ? "0" : "") 
      + String(mfrc522.uid.uidByte[i], HEX);
    }
    
    Serial.println(strID); //IMPRIME NA SERIAL O UID DA TAG RFID

  }