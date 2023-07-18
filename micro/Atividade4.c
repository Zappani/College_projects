/*
 *Atividade 4
 *Lucas Zappani Siqueira
 */ 

#include <xc.h>								//Biblioteca das funções do C para atmega328p 
#include <avr/interrupt.h>					//Biblioteca de interrupções do atmega328p

#define FOSC 1000000 // Clock Speed			//Constante de CLKcpu para calculo de baudrate
#define BAUD 9600							//Baudrate desejado
#define MYUBRR FOSC/8/BAUD-1				//Constante do resultado do cálculo para parametrização do baudrate USART

char dutyCycle=0;										//Armazena do duty cycle desejado
char rxData=53;											//Armazena o buffer de dados recebido pelo serial
char *ptr_mgn;											//Ponteiro destinado para indicar a mensagem a ser enviada pela serial
char menL[]={"Ligado!\r\n"};							//Mensagem de PWM ativado para ser enviado pelo serial
char menD[]={"Desligado!\r\n"};							//Mensagem de PWM desativado para ser enviado pelo serial
char menDuty[]={"Duty cycle= 0%\r\n"};					//Mensagem indicando o atual duty cycle para ser enviado pelo serial
char menE[]={"Mensagem invalida!\r\n"};					//Mensagem de resposta, para de recebimento de dados do serial não esperrados
char menD0[]={"Desligado! - Duty Cycle=0%\r\n"};		//Mensagem de PWM desativo, por duty cycle = 0%
char flagTX=0, flagRX=0;								//Flag de controle, por software, da comunicação serial
	
char bcd[10]={								//Padrões de exibição para o display de 7seg
0x3F, 0x06, 0x5B, 0x4F, 0x66,
0x6D, 0x7D, 0x07, 0x7F, 0x6F};

//Funções de parametrização
ISR(TIMER0_OVF_vect)						//Tratamento da interrupção por overflow do timer0
{
	OCR0A=dutyCycle;						//Carrega o duty cycle atual;
	return;
}

ISR(USART_RX_vect)							//Tratamento da interrupção por recebimento de dados por serial
{
	rxData=UDR0;							//Carrega o dado do buffer
	return;	
}

ISR(USART_TX_vect)							//Tratamento da interrupção por fim de transmissão por serial
{
	char temp;								//Variável temporária, auxilia na operação da interrupção
	if(flagTX)								//Controle, por software, para transmissão de dados vetorizados
	{
		temp = *(++ptr_mgn);				
		if(temp!='\n') UDR0=temp;			//Verifica se dado a ser enviado, não é o caracter nulo, indicano o fim do vetor
		else 
		{
			UDR0=temp;						//Carrega o caracter nulo, indicando o fim da mensagem e do vetor
			flagTX = 0;						//Libera a transmissão de novas mensagens
		}
	}
	return;
}
void configIO(void)							//Função de parametrização dos GPIO
{
	DDRB=0xff;								//Parametriza todos os terminais do portb como sáidas
	DDRC=0x7f;								//Parametriza todos os terminais do portc como saídas, exceto o PC6, pois é reset por hardware
	DDRD=0x44;								//Parametriza os terminais 3 e 7 do portd como saída
	return;
}
void timer0Config(void)
{
	TIMSK0=(1<<TOIE0);							//Habilita a interrupção por overflow do timer0
	TCCR0A=(1<<COM0A1)+(1<<WGM01)+(1<<WGM00);	//Parametriza do timer0 como fastPWM e habilita a saída OC0A
	TCCR0B=(1<<CS00);							//Parametriza o clock do timer0 sem prescaler
	return;
}
void UARTConfig(void)							//Parametriza o USART0
{
	int aux = MYUBRR;							//Carrega o MYUBRR na variável auxiliar
	UBRR0H = (unsigned char) (aux>>8);			//Carrega os 8 MSB do MYUBRR no resgistrador
	UBRR0L = (unsigned char) aux;				//Carrega os 8 LSB do MYUBRR no resgistrador

	UCSR0A |= (1 << U2X0);											//Habilita a Double Speed Operation
	UCSR0B |= (1<<RXCIE0) + (1<<TXCIE0) + (1<<RXEN0) + (1<<TXEN0);	//Habilita as interrupções de recepção e transmissão, habilita recepção e transmissão por serial
	UCSR0C |= (1<<UCSZ00) + (1<<UCSZ01);							//Configura o tamanho do frame para 8 bits
	return;
}

//Funções de uso recorrente
void atualizarDisplay(char valor)					//Função para atualizar os displays de 7seg
{
	if(valor>9) return;								//Controle de execução, caso o dado esteja fora do esperado
	else 
	{
		PORTB=bcd[0];								//Carrega o padrão 0 para o 7seg de unidade
		if(bcd[valor] & 0b01000000)					//Verifica se o bit6 do padrão do 7seg é 1
		{
			PORTC=bcd[valor] & 0b00111111;			//Corrige e carrega o dados do 7seg decimal no portc
			PORTD=0b00000100;						//Seta apenas o PORTD2
		}
		else
		{
			PORTC=bcd[valor];						//Carrega, sem correção, o padrão do 7seg decimal no portc
			PORTD=0;								//Zera o portd, em conformidade o número a ser exibido no 7seg deciimal
		}
		return;
	}
}

void serialSend(char dado)					//Função para envio de dados pelo serial
{
	if(dado=='0')							//Caso o dado seja '0'		
	{
		flagTX=1;							//Habilita a flag de controle, por software
		ptr_mgn=menD0;						//Carrega o endereço do vetor para o pontero
		UDR0=*ptr_mgn;						//Incia a transmissão do vetor, carregado o primero char no buffer
	}
	else if(dado>='1' && dado<='9')			
	{
		flagTX=1;
		menDuty[11]=dado;					//Complementa a mensagem a ser enviada, exibindo para o correto duty cycle
		ptr_mgn=menDuty;
		UDR0=*ptr_mgn;
	}
	else if(dado=='l' || dado=='L')			//Para exibir a mensagem de "Ligado!"
	{
		flagTX=1;
		ptr_mgn=menL;
		UDR0=*ptr_mgn;
	}
	else if(dado=='d' || dado=='D')			//Para exibir a mensgem de "Desligado!"
	{	
		flagTX=1;
		ptr_mgn=menD;
		UDR0=*ptr_mgn;
	}
	else
	{										//Caso o dado não se encaixa na condições anteriores
		flagTX=1;
		ptr_mgn=menE;
		UDR0=*ptr_mgn;
	}
}
int main(void)						//Função de principal
{
	char mem=0;						//Variável local
	configIO();						//Chama a função de parametrização de port
	timer0Config();					//Chama a função de parametrização do timer0
	UARTConfig();					//Chama a função de parametrização do USART
	sei();							//Habilitador geral de interrupção

    while(1)						//loop principal
    {
		if(mem!=rxData)				//Verifica se o dado da variável rxData é diferente, assim evitando recorrencia de execução
		{
			mem=rxData;										//Copia a variável que será tratada.
			if(rxData=='0') TCCR0B=0;						//Desabilita o timer0, caso o duty cycle seja 0%
			else if(rxData>='1' && rxData<='9') TCCR0B=1;	//Habilita automaticamente o timer0, caso dados indique novo duty cycle
			if(rxData=='1') dutyCycle=26;					//Duty Cycle para 10%
			else if(rxData=='2') dutyCycle=53;				//Duty Cycle para 20%
			else if(rxData=='3') dutyCycle=78;				//Duty Cycle para 30%
			else if(rxData=='4') dutyCycle=104;				//Duty Cycle para 40%
			else if(rxData=='5') dutyCycle=127;				//Duty Cycle para 50%
			else if(rxData=='6') dutyCycle=153;				//Duty Cycle para 60%
			else if(rxData=='7') dutyCycle=180;				//Duty Cycle para 70%
			else if(rxData=='8') dutyCycle=191;				//Duty Cycle para 80%
			else if(rxData=='9') dutyCycle=231;				//Duty Cycle para 90%
			else if(rxData=='d' || rxData=='D') TCCR0B=0;	//Desabilita o timer0
			else if(rxData=='l' || rxData=='L') TCCR0B=1;	//Habilita o timero
			atualizarDisplay(rxData-48);					//Chama a função de atualização dos displays
			serialSend(rxData);								//Chama a função para enviar dados pelo serial
		}
	}
}