;Lucas Zappani Siqueira
;GRR20202599

.cseg
.org 0x0000				; Configura a função start no endereço de memória em 0x0000
	jmp  start

.org 0x0008				; Configura a função PCINT1_ISR para o endereço de memória 0x0008
	jmp  PCINT1_ISR


.org 0x0100				; Configura o resto do código para o endereço de memória 0x0100
start:
	ldi r16, 0xFF		; Carrega o valor 0b11111111 no r16
	out DDRB, r16		; Habilita todas os pinos de saída do PORTB
	ldi r16, 3			; Carrega o valor 3 em r16
	out PORTC, r16		; Habilita os dois primeiros pinos do PORTC
	ldi r16, 2			; Carrega o valor 2 em r16
	sts PCICR, r16		; Seleciona as saídas para interrupção em PCINT8 - 14
	ldi r16, 3			; Carrega o valor 3 em r16
	sts PCMSK1, r16		;Seleciona as saídas para interrupções PCINT8 e PCINT9 
	sei					; Habilita as interrupções globais

ldi r17, 0				; Carrega o valor 0 em r17
ldi r20, 0x10			; Carrega o valor 0b00010000 em r20
; Função que conta de 0 a 99 em BCD progressivamente
cresc:
	out PORTB, r17		; Manda o valor em r17 para a saída do PORTB
	call delay			; Chama a função delay
	inc r17				; Incrementa 1 em r17
	ldi r16, 0x0F		; Carrega o valor 0b00001111 em r16
	and r16, r17		; Funções lógica AND entre os valores dos registradores r16 e r17
	cpi r16, 0x0A		; Compara se o valor em r16 é igual a 0b00001010
	brne PCINT1_ISR		; Se o valor não for igual, volta para a função PCINT1_ISR para verificar se houve interrupção
	ldi r16, 0xF0		; Carrega o valor 0b11110000
	and r17, r16		; Funções lógica AND entre os valores dos registradores r17 e r16
	add r17, r20		; Adiciona o valor de r20 em r17
	mov r16, r17		; Move o valor de r17 para r16
	cpi r16, 0xA0		; Compara se o valor em r16 é igual a 0b10100000
	brne PCINT1_ISR		; Se o valor não for igual, volta para a função PCINT1_ISR para verificar se houve interrupção
	ldi r16, 0x0F		; Carrega o valor 0b00001111
	and r17, r16		; Funções lógica AND entre os valores dos registradores r17 e r16
    rjmp PCINT1_ISR		; Pula para a função PCINT1_ISR

; Função que conta de 0 a 99 em BCD regressivamente
decresc:
	 out PORTB, r17		; Manda o valor em r17 para a saída do PORTB
     call delay			; Chama a função delay
     dec r17			; decrementa 1 em r17
     ldi r16, 0x0F		; Carrega o valor 0b00001111 em r16
     and r16, r17		; Funções lógica AND entre os valores dos registradores r16 e r17
     cpi r16, 0X0F		; Compara se o valor em r16 é igual a 0b00001111
     brne PCINT1_ISR	; Se o valor não for igual, volta para a função PCINT1_ISR para verificar se houve interrupção
     ldi r16, 0XF9		; Carrega o valor 0b11111001
     and r17, r16		; Funções lógica AND entre os valores dos registradores r17 e r16
     mov r16, r17		; Move o valor de r17 para r16
     cpi r16, 0xF9		; Compara se o valor em r16 é igual a 0b11111010
     brne PCINT1_ISR	; Se o valor não for igual, volta para a função PCINT1_ISR para verificar se houve interrupção
     ldi r16, 0x99		; Carrega o valor 0b00001111 em r16
     and r17, r16		; Funções lógica AND entre os valores dos registradores r17 e r16
     rjmp PCINT1_ISR	; Pula para a função PCINT1_ISR

; Função delay
delay:
	ldi r25, 100
	ldi r26, 100
	ldi r27, 30
	delay_1:
		dec r25
		brne delay_1
		ldi r25, 100
		dec r26
		brne delay_1
		ldi r26, 100
		dec r27
		brne delay_1
		ret

; Função de interrupção
PCINT1_ISR:
	in  r19, PINC		; Verifica se o PINC tem valor 1 ou 0 e carrega em r19
	sbrs r19, 0			; Se o valor for 0, faz a instrução abaixo
	rjmp decresc		; Pula para a função decresc
	sbrs r19, 1			; Se o valor em r19 for 1, faz a instrução abaixo
	ldi r17, 0			; Carrega o valor 0 em r17
	rjmp cresc			; Pula para a função cresc 
	
	
