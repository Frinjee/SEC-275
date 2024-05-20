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

_listen:
	
	push byte 1 ; move 1 onto the stack (max queue len arg)
	push edi ; push file desc onto stack
	mov ecx, esp ; move addr of args into ecx
	mov ebx, 4 ; invoke subroutine LISTEN
	mov eax, 102 ; invoke SYS_SOCKETCALL
	int 80h

_accept:
	
	push byte 0 ; push addr len arg onto stack
	push byte 0 ; push addr arg onto stack
	push edi ; push file desc onto stack
	mov ecx, esp ; mov addr of args into ecx
	mov ebx, 5 ; invoke subroutine ACCEPT
	mov eax, 102 
	int 80h

_exit:
	
	call quit