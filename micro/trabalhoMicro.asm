;TRABALHO 1 LABORATÓRIO DE MICROELETRÔNICA 
;Author : Lucas Zappani Siqueira
;GRR 20202599

;Implemente um programa em assembly que conte de 0 a 99s,
;em BCD, e apresente o valor da contagem 8 LEDs.
;O intervalo de aproximadamente 1s deverá 
;ser gerado com as instruções: LDI, DEC e BRNE.


;*****************************************************************************************************************************************************************************************************************************************
;O programa começa definindo os pinos do microcontrolador 
;que são usados para entrada e saída de dados. 
;O pino DDRB é configurado para saída de dados e o pino 
;PORTB é configurado como entrada de dados.
;*****************************************************************************************************************************************************************************************************************************************

start:			  ;Configura os pinos de entrada/saída do microcontrolador               

    	ldi r16, 0xFF  ;Este comando carrega o valor 0xFF (255 em decimal) no registrador R16. 
		       ;O prefixo ldi carrega um valor imediato em um registrador.

	out DDRB, R16  ;Este comando envia o conteúdo do registrador R16 para o registrador DDRB. 
			;O out envia um valor de um registrador para um dispositivo externo. 
			 ;DDRB é um registrador que controla os pinos de I/O do microcontrolador

	ldi r17, 0x10  ;Este comando carrega o valor 0x10 (16 em decimal) no registrador R17. 
			 ;ldi carrega um valor imediato em um registrador.

;*****************************************************************************************************************************************************************************************************************************************




;*****************************************************************************************************************************************************************************************************************************************
;O loop começa escrevendo um valor zero no registrador PORTB para desligar o LED. 
;Em seguida, o programa chama o delay para atrasar antes de incrementar o valor 
;no registrador R0 em +1. O programa usa o registrador R16 como um 
;filtro bit a bit para permitir apenas os quatro bits mais significativos do registrador R0. 
;Em seguida, o programa subtrai 10 do registrador R16.
;Se o valor de R16 não for zero, o programa reinicia o loop. 
;Se o valor de R16 for zero, o programa continua e filtra os quatro bits mais significativos do 
;registrador R0 e armazena o resultado em R0. 
;O programa adiciona o valor 16 em decimal (0x10 em hexadecimal) ao valor no registrador R0. 
;Em seguida, ele copia o valor de R0 para R16 e subtrai 160 do R16.
;Se o valor de R16 não for zero, o programa volta para o início do loop e repete as etapas acima. 
;Se o valor de R16 for zero, o programa filtra novamente os quatro bits mais significativos do 
;registrador R0 e armazena o resultado em R0. 
;Finalmente, ele retorna ao início do loop e repete todo o processo novamente.
;*****************************************************************************************************************************************************************************************************************************************

loop:			;Ele é usado como um ponto de referência para desvios de fluxo de controle no programa.	

	out PORTB, r0  ;Este comando envia o conteúdo do registrador R0 para o registrador PORTB. 
			;O registrador PORTB é responsável por controlar as saídas do microcontrolador.

	call delay     ;Este comando faz uma chamada para uma sub-rotina chamada "delay". 
			;Essa sub-rotina é responsável por introduzir uma pausa ou atraso no programa.

	inc r0		;Este comando incrementa o valor no registrador R0 em 1.

	ldi r16, 0x0F  ;Este comando carrega o valor 0x0F (15 em decimal) no registrador R16.

	and r16, r0    ;Este comando faz uma operação lógica AND entre o conteúdo dos registradores R16 e R0, 
			;e armazena o resultado no registrador R16. 
			;A operação lógica AND é usada para realizar uma operação de filtragem bit a bit.

	subi r16, 0b00001010  ;Este comando subtrai o valor 0b00001010 (ou 10 em decimal) 
			      ;do conteúdo do registrador R16.

	brne loop      ;Este comando desvia o fluxo para o loop se o conteúdo do registrador R16 não for igual a zero.

	ldi r16, 0xF0  ;Este comando carrega o valor 0xF0 (240 em decimal) no registrador R16.

	and r0, r16    ;Este comando faz uma operação lógica AND entre o conteúdo dos registradores R0 e R16, 
			;e armazena o resultado no registrador R0. 

	add r0, r17    ;Este comando adiciona o conteúdo do registrador R17 ao conteúdo do registrador R0, 
		       ;e armazena o resultado no registrador R0.

	mov  r16, r0   ;Este comando copia o conteúdo do registrador R0 para o registrador R16.

	subi r16, 0b10100000  ;Este comando subtrai o valor 0b10100000 (ou 160 em decimal) do conteúdo do 
			      ;registrador R16.

	brne loop      

	ldi r16, 0x0F   ;Este comando carrega o valor 0x0F (15 em decimal) no registrador R16.
	 
	and r0, r16     ;Este comando faz uma operação lógica AND entre o conteúdo dos registradores R0 e R16, 
			;e armazena o resultado no registrador R0. 

    	rjmp loop       ;Este comando desvia o fluxo de controle de volta para o loop.

delay:			;Este comando define uma sub-rotina chamada "delay". 
			;Essa sub-rotina é responsável por introduzir uma pausa ou atraso no programa.

	ldi r20, 250    ;Este comando carrega o valor 250 no registrador R20.

	ldi r21, 250    ;Este comando carrega o valor 250 no registrador R21.
 
	ldi r22, 5	;Este comando carrega o valor 5 no registrador R22.

dec_r20:		;Este comando define um rótulo chamado "dec_r20". 
				   ;Ele é usado como um ponto de referência para desvios de fluxo de controle no programa.

	dec r20         ;Este comando decrementa o valor no registrador R20 em 1

	brne dec_r20    ;Este comando desvia o fluxo de controle de volta para o rótulo "dec_r20" 
		        ;se o conteúdo do registrador R20 não for igual a zero.

	ldi r20, 250    ;Este comando carrega o valor 250 no registrador R20.

	dec r21         ;Este comando decrementa o valor no registrador R21 em 1.
	
	brne dec_r20   

    	dec r22		;Este comando decrementa o valor no registrador R22 em 1.

	brne dec_r20  

	ret		;Este comando retorna o controle para o ponto de chamada anterior à sub-rotina "delay".
;*****************************************************************************************************************************************************************************************************************************************

