; sys_socketcalls subroutine expects 2 args (pointer to array of args in ECX
; and the int value 1 in EBX)
; the opcode is then loaded into EAX and the kernel is called to create the 
; socket. Receivign back a file descriptor of the created socket, we then
; use it for performing other socket prog functions

%include 'funcs.asm'

section .text
global _start

_start:
	
	; init _ 0
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

	call sprintLF

_exit:
	
	call quit