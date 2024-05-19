; Integer printing function
intPrint:
	
	push eax
	push ecx
	push edx
	push esi
	mov ecx, 0

divLoop:
	inc ecx ; # of chars to print
	mov edx, 0  ; empty edx
	mov esi, 10 ; 
	idiv esi ; divide eax by esi
	add edx, 48 ; convert edx to its ASCII rep
	push edx ; push edx onto stack (string rep of an int)
	cmp eax, 0 ; check if int can be divided anymore
	jnz divLoop ; jump if not zero

printLoop:
	
	dec ecx ; count down each byte we put on the stack
	mov eax, esp ; mov the stack pointer into eax for printing
	call sprint 
	pop eax
	cmp ecx, 0 ; check if all bytes pushed onto the stack
	jnz printLoop

	pop esi
	pop edx
	pop ecx
	pop eax
	ret

; Int printing func with linefeed
intPrintLF:

	call intPrint

	push eax,
	mov eax, 0Ah
	push eax
	mov eax, esp
	call sprint
	pop eax
	pop eax
	ret

; string len calc function
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

; ASCII to integer function
atoi:
	; perserve _ on the stack to be restored after function runs
	push ebx
	push ecx
	push edx
	push esi
	mov esi, eax ; move pointer in eax into esi (# we are converting)
	eax, 0 ; initialize eax with dec value 0
	ecx, 0;  initialize ecx with dec value 0

.multiplyLoop:

	xor ebx, ebx ; resets lower and upper bytes (ebx) to 0
	mov bl, [esi+ecx] ; move single byte into registers lower half(ebx)
	cmp bl, 48 ; compare ebx register lower half val against ASCII val 48 
	jl .fin ; jump if less than label fin
	cmp bl, 57 ; compare ebx register lower half val against ASCII val 57
	jg .fin ; jump if greater than

	sub bl, 48 ; convert ebx lower half to dec representation of ASCII val
	add eax, ebx ; add ebx to our int val in eax
	mov ebx, 10 ; move deimal value 10 into ebx
	mul ebx ; eax * ebx to get place value
	inc ecx ; increment counter register
	jmp multiplyLoop ; continue


.fin:
	cmp ecx 0
	je .restore
	mov ebx, 10
	div ebx

.restore
	; restore x from the value we pushed onto the stack at the start
	pop esi 
	pop edx
	pop ecx
	pop ebx
	ret