
%include 'funcs.asm'

section .data
msg1     db		'Enter your name: ', 0h
msg2     db		'Hello, ', 0h

section .bss
sinput:  resb 	 255 ; reserve a 255 byte space in mem

section .text
global _start

_start:

	mov eax, msg1
	call sprint

	mov edx, 255 ; # of bytes to read
	mov ecx, sinput ;
	mov ebx, 0 ; read from STDIN file
	mov eax, 3 ; invoke SYS_READ
	int 80h

	mov eax, msg2
	call sprint

	mov eax, sinput ; move buffer into eax (input contains LF)
	call sprint

	call quit