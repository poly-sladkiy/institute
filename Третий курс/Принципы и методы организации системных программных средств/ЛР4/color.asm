.Model Tiny
.Code
.286
org 100h
Start:
    mov al,13h 
    int 10h          
    push 0A000h      
    pop ds          
    mov dx,330h
    mov al,0c0h
    out dx,al
    mov al,7ah
    out dx,al
    mov al,0c1h
    out dx,al
    mov al,66h
    out dx,al
        xor ax,ax
        mov dx,3C9h      
ALoop:  out dx,al
        push ax
        xor ax,ax
        out dx,al
        pop ax
        out dx,al
        inc ax
        jne ALoop
FLoop:  cmp dx,0Ah
        jl BLoop
        in al,40h
        xchg al,ah
        in al,40h
        add si,ax
        mov word ptr [si],40h
BLoop:  xchg cx,ax
CLoop:  lodsb
        or al,al
        je DLoop
        dec ax
        mov [si][-01],al
        push ax
        in al,40h
        xchg bl,al
        shr bl,4
        add si,bx
        pop ax
        mov [si][0FEB7h],al
        mov [si][137h],al
DLoop:  dec cx
        jne CLoop
        inc dx
        dec word ptr cs:[buffer]
        jne ELoop
        push dx
        mov dx,330h
        mov al,90h
        out dx,al
        in al,40h
    shr al,2
    add al,11h
    out dx,al
    in al,40h
    shr al,1
    out dx,al
    mov dx,330h
    mov al,91h
    out dx,al
    in al,40h
        and al,3Fh
        out dx,al
        mov al,29h
        out dx,al
        mov word ptr cs:[buffer],5
        pop dx
        
ELoop:  
    in al,60h
    dec al
    jne FLoop
    mov dx,330h
    mov al,0b1h
    out dx,al
    mov al,78h
    out dx,al
    xor al,al
    out dx,al
    mov ax, 0003h
    int 10h
    push cs
    pop ds
    ret
buffer:
end start