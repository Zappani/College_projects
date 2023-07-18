;Lucas Zappani Siqueira
;GRR20202599
;Display de 7 segmentos

;Armazena dados na memória Flash
 
.cseg							; Diretiva para memória de programa

.org 0x0400						; Direciona para área de memoria 400

; Vetor 'bytes' contendo os valores que sao mostrados no display através de seus segmentos
bytes: .db 0b00111111,0b00000110,0b01011011,0b01001111,0b01100110,0b01101101,0b01111101,0b00000111,0b01111111,0b01100111

.org 0x00						; Direciona para área de memória 00
	  jmp RESET					; Pula para a função RESET
.org 0x08						; Direciona para a área de memória 08
	  jmp PCINT1_ISR			; PC_ISR DO PORT C
  
  .org 0x050					; Direciona para a área de memória 50
  RESET:
	  sbi PORTC, 1				; Define o bit do registrador PORTC como 1
	  ldi r17, 0xff				; Carrega o valor 0b11111111 em r17
	  out PORTC, r17			; Habilita todos os pull ups da porta c
	  ldi r17, 0b00000010		; Carrega o valor 2 em r17
	  sts PCICR, r17			; Direciona as saídas das portas PCINT8 - 14
	  ldi r17, 0b00001001		; Atribui o valor 1 em r17
	  sts PCMSK1, r17			; Seleciona a porta PCINT8 para verificar as interrupções
	  sei						; Habilita a interupção global
	  ldi r18, 1				; Atribui o valor 1 em r18


;Configura os pino 0b01111111 DDRB E DDRD Como saídas
start:
	ldi r16, 0x7F
	out DDRB, r16
	out DDRD, r16
; O r16 indicará o valor, dentro do vetor 'bytes', a ser mostrado no display da direita (menos significativo)
; O r20 indicará o valor, dentro do vetor 'bytes', a ser mostrado no display da direita (mais significativo)
	ldi r16, 0					; Aponta para o primeiro valor do vetor 'bytes'
	ldi r20, 0					; Aponta para o primeiro valor do vetor 'bytes'

loop:
; r30 e r31 recebem o end de bytes

; recebe uma cópia de r16, para que Z aponte para o digito desejado
	ldi r30, low(bytes*2)		;r16
	ldi r31, high(bytes*2)
	add r30, r16				; Adiciona o valor de r16 em r30
	lpm r17, Z					; r17 é carregado com o valor apontado por Z
	out PORTB, r17				; Mostra o número que Z aponta no display da direita (menos significativo)
; Dezena
; recebe uma cópia de r20, para que Z aponte para o digito desejado
	ldi r30, low(bytes*2)		; r20
	add r30, r20				; Adiciona o valor de r16 em r30
	lpm r17, Z					; r17 é carregado com o valor apontado por Z
	out PORTD, r17				; Mostra o número que Z aponta no display da esquerda (mais significativo)
	call delay					; Chama a função 'delay'
	add r16, r18				; incrementa r16 para percorrer todas as posições do vetor 'bytes'
	cpi r16, 0x0A				; Continua a sequência quando o valor de r16 for 10 para aumentar o valor da dezena
	brne loop
	ldi r16, 0					; r16 volta a apontar para o primeiro valor do vetor 'bytes'
	inc r20						; Incrementa r20 para apontar para o próximo valor do vetor 'bytes'
	cpi r20, 0x0A				; Compara com 10 para reiniciar o processo
	brne loop
	ldi r20, 0					; r20 volta a apontar para o primeiro valor do vetor 'bytes' para reiniciar a contagem
	rjmp loop

; Delay de 1 segundo
delay:
	ldi r21, 94
	ldi r22, 100
	ldi r23, 33
loop_delay:
	dec r21
	brne loop_delay
	ldi r21, 100
	dec r22
	brne loop_delay
	ldi r22, 100
	dec r23
	brne loop_delay
	ret

PCINT1_ISR:
	in  r19, PINC				; Le e armazena o valor do registrador PINC
	com r19						; Complemento de um
	andi r19, 0x01				; Realiza função and entre o registrador e uma constante
	eor r18, r19				; Realiza a função ou exclusivo entre o registrador 
	reti						; Retorna à interrupção 