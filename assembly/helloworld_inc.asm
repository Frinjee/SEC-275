
%include 'funcs.asm'

section .data
msg1     db		'Hello, Jen', 0Ah, 0h
msg2     db		'Recycling in NASM', 0Ah, 0h

section .text
global _start

_start:

	mov eax, msg1
	call sprintLF

	mov eax, msg2
	call sprintLF

	call quit