section .data
msg     db		'Hello, Jen', 0Ah

section .text
global _start

_start:	

	mov eax, msg ; move the addr of msg into EBX
	call strlen

	mov edx, eax
	mov ecx, msg
	mov ebx, 1
	mov eax, 4
	int 80h

	mov ebx, 0
	mov eax, 1
	int 80h

strlen:

	push ebx
	mov ebx, eax

nextchar:

	cmp byte [eax], 0 ; compare the byte pointed to by EAX at this addr against 0
	jz fin ; jump (if the zero flagged has been set)
	inc eax ; increment the addr in EAX by one byte
	jmp nextchar

fin:
	
	sub eax, ebx
	pop ebx
	ret