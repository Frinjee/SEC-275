
%include 'funcs.asm'

section .text
global _start

_start:
	
	pop ecx ; first value is the # of args
	pop edx ; second value is program name (discarded)
	sub ecx, 1 ; decrease # of args without program name (ecx)
	mov edx, 0 ; initialize our data register to store additions

nextArg:

	cmp ecx, 0h ; check if args are left
	jz zeroArgsLeft ; jmp if zero flag is set
	pop nextArg
	call atoi
	add edx, eax ; perform addition logic
	dec ecx ; decrease # of args left by 1
	jmp nextArg 

zeroArgsLeft:

	mov eax, edx ; move data result into eax for printing
	call 