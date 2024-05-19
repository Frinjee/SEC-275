; Compile with nasm -f elf helloworld.asm
; Link with ld -m elf_i386 helloword.o -o helloworld
; Run with ./helloworld

section .data
msg		db		'Hello World!', 0Ah

section .text
global _start

_start:

	mov edx, 13
	mov ecx, msg
	mov ebx, 1
	mov eax, 4
	int 80h

	mov ebx, 0 ; return 0 status on exit (No errors)
	mov eax, 1 ; invoke SYS_EXIT
	int 80h