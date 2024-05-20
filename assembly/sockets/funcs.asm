slen:

	push ebx
	mov ebx, eax

nextchar: 
	
	cmp byte [eax], 0
	jz fin
	inc eax
	jmp nextchar

fin:
	
	sub eax, ebx
	pop ebx
	ret

; String printing function
sprint:
	
	push edx
	push ecx
	push ebx
	push eax
	call slen

	mov edx, eax
	pop eax	

	mov ecx, eax
	mov ebx, 1
	mov eax, 4
	int 80h

	pop ebx
	pop ecx
	pop edx
	ret

; String printing with line feed
sprintLF:
	call sprint

	push eax
	mov eax, 0Ah

	push eax

	mov eax, esp
	call sprint
	pop eax
	pop eax
	ret


; Exit program and restore resources
quit:
	
	mov ebx, 0
	mov eax, 1
	int 80h
	ret



