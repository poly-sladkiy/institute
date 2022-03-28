c1 segment
	assume cs:c1, ds:c1, es:c1, ss:c1
	org 100h

start:
	mov ax, 3
	int 10h

	mov ax, 0FFFFh
	mov ds, ax
	
	mov ax, 0B800h
	mov es, ax

	mov si, 5
	mov di, 1690
	mov cx, 8
	mov ah, 0C2h

m2:
	mov al, [si]
	mov es:[di], ax

	add di, 2
	inc si

	loop m2

	mov ax, 4C00h
	int 21h

c1 ends
end start