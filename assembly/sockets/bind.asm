; Associate the created socket with a local IP address and port, we can connect
; to this. Done by calling the second subroutine of sys_socketcall(bind)
; This subroutine expects 2 args, a pointer to an array of args in ECX and
; the int value 2 in EBX

%include 'funcs.asm'

section .text
global _start

_start:
	
	; init registers
	xor eax, eax 
	xor ebx, ebx
	xor edi, edi
	xor esi, esi

_socket:
	
	push byte 6 ; push IPPROTO_TCP(6) onto the stack
	push byte 1 ; push SOCK_STREAM(1)
	push byte 2 ; push PF_INET(2)
	mov ecx, esp ; mov addr of args into ecx
	mov ebx, 1 ; invoke subroutine SOCKET
	mov eax, 102 ; invoke SYS_SOCKETCALL
	int 80h

_bind:
	
	mov edi, eax ; move return val of SYS_SOCKETCALL into edi
	push dword 0x00000000 ; push 0(dec) onto IP addr stack (0.0.0.0)
	push word 0x2923 ; push 9001(dec) onto stack PORT
	push word 2 ; push 2(dec) onto stack AF_INET
	mov ecx, esp ; mov addr of stack pointer into ecx
	push byte 16 ; push 16(dec) onto stack (args len)
	push ecx ; push addr of args onto stack
	push edi ; push file descriptor onto stack
	mov ecx, esp ; mov addr of args into ecx
	mov ebx, 2 ; invoke subroutine BIND
	mov eax, 102 ; invoke SYS_SOCKETCALL 
	int 80h

_exit:
	
	call quit