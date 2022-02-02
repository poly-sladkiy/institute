c1 segment
	assume cs:c1, ds:c1, es:c1, ss:c1
	org 100h	; forever in one segment programs

start:
	
	mov ah, 9
	mov dx, offset mess_enter_data
	mov ah, 9	; output data
	int 21h
	
	mov dx, offset arr_data
	mov arr_data, 198	; 2 bytes for max bytes and how much enter

	mov ah, 10		; read data
	int 21h

	mov si, offset arr_data + 2
	mov di, offset arr_res

	mov cx, [arr_data + 1]	
	xor ch, ch
	shr cx, 1	; >> 2

m1:
	mov ax, [si]

	cmp ax, 3231h	; 12 in word
	je m2

	cmp ax, 3332h	; 23 in word
	je m2

	cmp ax, 3433h	; 34 in word
	je m2

	mov [di], ax

	add di, 2

m2:
	add si, 2

	loop m1
	
m3:	; output result
	mov dx, offset mess_out_res 
	mov ah, 9
	int 21h
	
	mov dx, offset arr_res
	mov ah, 9
	int 21h

	mov ah, 7
	int 21h

	mov ax, 4c00h
	int 21h

	mess_enter_data db 10, 13, 'Enter array: ', 10, 13, '$'
	arr_data dw 100 dup(?)
	arr_res	 dw 100 dup('$')
	mess_out_res db 10, 13, 'Result: ', 10, 13, '$'

c1 ends
end start