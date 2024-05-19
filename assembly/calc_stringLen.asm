; sys_write requires that we pass a pointer to the string we want to output into
; memory and the length in bytes we want to print out. 
; if the message string were modified we'd have to update the length in bytes

section .data
msg     db		'Hello, Jen', 0Ah

section .text
global _start

_start:	

	mov ebx, msg ; move the addr of msg into EBX
	mov eax, ebx ; move the addr in EBX into EAX as well

nextchar:

	cmp byte [eax], 0 ; compare the byte pointed to by EAX at this addr against 0
	jz fin ; jump (if the zero flagged has been set)
	inc eax ; increment the addr in EAX by one byte
	jmp nextchar

fin:

	sub eax, ebx ; subtract the addr in EBX from the addr in EAX

	mov edx, eax ; eax now equals the number of bytes in our string
	mov ecx, msg 
	mov ebx, 1
	mov eax, 4
	int 80h

	mov ebx, 0
	mov eax, 1
	int 80h