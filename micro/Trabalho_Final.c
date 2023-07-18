/*

Trabalho final da matéria de programação de microcontroladores

Orientator: 

Prof. Dr. Marcos Vinicio Haas Rambo

Developers:

Lucas Zappani Siqueira	GRR20202599

Alessandro Farago		GRR20202601

Clock: 16MHz

Intuito do projeto: 

Desenvolver um programa em ANSI C para demonstrar a utilização da linguagem e 
suas propriedades que não estão disponiveis no método tradicional de programação do AtMega328p.

Materiais utilizados na implementação do projeto:

Board Arduino Uno 
3 LED's (vermelho, amarelo e verde)
Jumpers 
3 resistores 220 Ohms



*/



//=================================================================================================================================
//  Definições ====================================================================================================================
#define F_CPU 16000000
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdbool.h>
#include <util/delay.h>

bool upd = false;
unsigned long int baset1 = 0;					// Variável global estática com base de tempo1

//=================================================================================================================================
// Interrupção e timer ============================================================================================================
ISR(INT0_vect) {
	upd = true;									// Torna o valor de upd TRUE quando o push botton é acionado 
}//end ISR

ISR(TIMER0_OVF_vect){							// Atualiza baset1 sempre que um clock ocorre
	
	baset1++;

}//end ISR

/*=================================================================================================================================
Por motivo não solucionado, a utilização do timer em modo overflow não foi possível mesmo com sua configuração
pois o valor de baset1 não foi atulizado em cada ciclo de clock 
*///===============================================================================================================================



//=================================================================================================================================
//  Função main ===================================================================================================================
int main() {
	
	//  Configurações dos LEDs ====================================================================================================
	DDRB |= (1 << DDB0);						// Configura o pino 8 como saída
	DDRB |= (1 << DDB1);						// Configura o pino 9 como saída
	DDRB |= (1 << DDB2);						// Configura o pino 10 como saída

	//  Configurações das interrupções ============================================================================================
	cli();
	
	DDRD &= ~(1 << DDD2);						// Configura pino 2 (PD2) como entrada

	PORTD |= (1 << PORTD2);						// Habilita pull-up interno de PD2

	EICRA |= (1 << ISC01) | (1 << ISC00);		// Configura a interrupção externa 0 como borda de subida
	EIMSK |= (1 << INT0);						// Habilita a interrupção externa 0
	
	TCNT0 = 0x06;								// Inicia Timer0 para contar até 250
	TCCR0B = 0x03;								// Prescaler 1:64
	TIMSK0 = 0x01;								// Habilita interrupção do Timer0

	sei();										//Habilita as interrupções globais
	
	upd = true;

	//  Laço =====================================================================================================================
	while(1){
		
		//  Interrupção push botton ==============================================================================================
		if(upd == true){						// Condicional para validação da interrupção
			upd = false;						// Torna o valor de upd FALSE quando o push botton é acionado
			int i = 0;
			
			while(i != 5){						// Laço para piscar LEDs
				_delay_ms(250);					// Espera 0,25 segundos 
			
				PORTB |= (1 << PORTB0);			// Acende o LED conectado ao pino 8 do PORTB
				PORTB |= (1 << PORTB1);			// Acende o LED conectado ao pino 9 do PORTB
				PORTB |= (1 << PORTB2);			// Acende o LED conectado ao pino 10 do PORTB
			
				_delay_ms(500);					// Espera 0,5 segundos
			
				PORTB &= ~(1 << PORTB0);		// Apaga o LED conectado ao pino 8 do PORTB
				PORTB &= ~(1 << PORTB1);		// Apaga o LED conectado ao pino 9 do PORTB
				PORTB &= ~(1 << PORTB2);		// Apaga o LED conectado ao pino 10 do PORTB
				
				i++;							
			}
			
			_delay_ms(250);					// Espera 0,25 segundos
			PORTB &= ~(1 << PORTB0);		// Apaga o LED conectado ao pino 8 do PORTB
			PORTB &= ~(1 << PORTB1);		// Apaga o LED conectado ao pino 9 do PORTB
			PORTB &= ~(1 << PORTB2);		// Apaga o LED conectado ao pino 10 do PORTB
			_delay_ms(250);					// Espera 0,25 segundos
			
			upd = false;						// Torna o valor de upd FALSE quando o push botton é acionado
		}
		
		
		//  Padrão comum =========================================================================================================
				
		// Controle do LED verde		
		PORTB |= (1 << PORTB0);					// Acende o LED conectado ao pino 8 do PORTB
		_delay_ms(500);							// Espera 0,5 segundos
		PORTB &= ~(1 << PORTB0);				// Apaga o LED conectado ao pino 8 do PORTB

		// Controle do LED amarelo
		PORTB |= (1 << PORTB1);					// Acende o LED conectado ao pino 9 do PORTB
		_delay_ms(500);							// Espera 0,5 segundos
		PORTB &= ~(1 << PORTB1);				// Apaga o LED conectado ao pino 9 do PORTB

		// Controle do LED vermelho
		PORTB |= (1 << PORTB2);					// Acende o LED conectado ao pino 10 do PORTB
		_delay_ms(500);							// Espera 0,5 segundos
		PORTB &= ~(1 << PORTB2);				// Apaga o LED conectado ao pino 10 do PORTB
		
	}
	return 0;									// É esperado da função main o retorno de um int
}