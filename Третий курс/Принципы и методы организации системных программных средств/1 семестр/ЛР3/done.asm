; ????????? ?????, ???????????? ? ??????? ????????? ?????, ????????? ??????? ????????? ?? ????????? ????? - ?????????????

; Macros for output data
print macro srting      
    push ax
    push dx
    mov dx, offset srting
    mov ah, 09h
    int 21h
    pop dx
    pop ax
endm

; Macros for input data
input macro srting  
    push ax 
    push dx
    mov dx, offset srting
    mov ah, 0Ah
    int 21h
    pop dx
    pop ax
endm



d1 SEGMENT para public 'data'

    in_str label byte           ; String (only for 6 chars)
    razmer  db 7                ; Buffer (for 6 chars)
    kol     db (?)              ; Count of input chars
    stroka  db 7 dup (?)        ; Buffer input value
    number  dw 5 dup (0)        ; Array of values
        
    sumres      dw 0    ; Sum of values in the array
    mulres      dw 0    ; Mul of values in the array
    sredres     dw 0    ; Avarage value of values in the array
    prochres    dw 0    ; Percent of positive value of values in the array

    siz dw 5        ; Lenght of the array
    
    lab3    db 'Laboratory work #3','$'
    author  db 13,10, 'Ignakov Konstantin 19-V-2'
    
    perevod db 10,13,'$'
    
    inputError      db 'Input Error!', 10,10,'$'
    divByZeroError  db 'Divition by zero!', 10,10,'$'
    overflow        db 'Overflow!', 10,10,'$'
    overflowSum     db 'Overflow Sum!', 10,10,'$'
    
    sumText     db 13,10, 'Sum of elements: ','$'
    mulText     db 13,10, 'Mul of elements: ','$'
    sredText    db 13,10, 'Srednee: ','$'
    prochText   db 13,10, 'Prochent: ','$'
    
    maxElText db  13,10, 'Max element:                             ','$'
    minElText db  13,10, 'Min element:                             ','$'
    
    out_str         db 6 dup (' '),'$'
    enter_please    db 'Input value: $'
    
    flag_err equ 1
    
d1 ENDS



st1 SEGMENT para stack 'stack'
    dw 100 dup (?)
st1 ENDS



; Entry point
c1 SEGMENT para public 'code'
    ASSUME cs:c1, ds:d1, ss:st1
    
start:  
    mov ax, d1
    mov ds, ax
    
    
    mov ax, 03h     ; Installing text video mode, clearing the screen
    int 10h         ; ah=0 (number of function), al=3 (number of mode)
    
    print lab3      ; Print work info
    print author    ; Print author 
    print perevod   ; Print `\n`

    ; Input data with Error Flag 
    xor di, di      ; di - Number of an element in the array
    mov cx, siz     ; cx - Lenght of the array
    
inputVal:   
    push cx
    
check:  
    print enter_please  ; Print info for input data
    input in_str        ; Input data like string
    print perevod
    
    call diapazon       ; Chech that value in (-29999, 29999)
    cmp bh, flag_err    ; Compare `BH` and `FLAG_ERROR`
    je inErr            ; If `BH` == 1: smth went wrong

    call dopust         ; ???????? ???????????? ???????? ????????
    cmp bh, flag_err    ; ??????? bh ? flag_err
    je inErr            ; ???? ????? 1 ????????? ?? ?????? ?????
    
    call AscToBin       ; ?????????????? ?????? ? ?????
    inc di
    inc di
    pop cx
    loop inputVal
    jmp searchSum
    
inErr:          
    print inputError    
    jmp check


; Sum of elements
searchSum:
    mov cx, siz             ; cx - array size
    mov si, offset number

searchLoop:
    mov ax, [si]

addToRes:
    add sumres, ax
    jo overFlowErrSum

nextVal:
    inc si
    inc si
    loop searchLoop
        

; Multiply of elements
searchNegMul:
    mov cx, siz
    mov si, offset number
    
    mov ax, 1               ; mul always use ax (smth * 1 = smth)
    
minusEl:
    mov bx, [si]
    imul bx                 ; multiply
    jo overFlowErr          ; chech overflow
    
plusEl:
    inc si
    inc si
    loop minusEl
    
    mov mulres, ax          ; mow answer to variable
    

; Average value of elements
searchSrednee:
    mov ax, sumres

    cwd
    idiv siz

    mov sredres, ax
    

; Percent of positive elements
; Formula (count * 100) / SIZE %
searchProchent:
    mov cx, siz
    mov si, offset number
    mov ax, 0h
    
    
findPosElem:
    mov bx, [si]
    
    cmp bx, 0h
    jl foundNegElem     ; If value is negative - skip
    
    add ax, 100d        ; 1 peace * 100 - check formula
    jo overFlowErrSum
    
    
foundNegElem:
    inc si
    inc si
    loop findPosElem
    
    cwd
    idiv siz
    
    mov prochres, ax
    
    jmp resOutput
    
    
    ; Print errors
overFlowErr:        
    print overflow          ; Print overflow
    jmp progend
    
zero:
    print divByZeroError    ; Print DivisionByZero
    jmp progend
        
overFlowErrSum:        
    print overflowSum  ; Print owerflow from sum
    jmp progend
    
        
; Print results
resOutput:      
    print sumText
    mov ax, sumres
    call BinToAsc
    print out_str

    mov cx,6            ; clear buffer
    xor si,si
clear1:     
    mov [out_str+si],' '
    inc si
    loop clear1

    print mulText
    mov ax,mulres   
    call BinToAsc
    print out_str

    mov cx,6            ; clear buffer
    xor si, si
clear2:     
    mov [out_str+si],' '
    inc si
    loop clear2

    print sredText
    mov ax,sredres  
    call BinToAsc
    print out_str
    
    
    mov cx,6            ; clear buffer
    xor si,si
        
clear3:     
    mov [out_str+si],' '
    inc si
    loop clear3

    print prochText
    mov ax, prochres
    call BinToAsc
    print out_str

    jmp progend
    
progend:    
        mov ax,4c00h
        int 21h
    
    
    

; Data in (-29999, +29999)
; Args:       
;       Buffer input - stroka
; Res:
;       bh - error flag
DIAPAZON PROC
    xor bh, bh
    xor si, si
    
    cmp kol, 05h    ; Count is 5
    jb dop
        
    cmp stroka, 2dh     ; If enter 5 and more, check for `-`
    jne plus            ; If first is not `-` - check count of numbers
    
    cmp kol, 06h        ; If first `-` and values less 6 
    jb dop        
    
    inc si      ; Chech first value
    jmp first

plus:   
    cmp kol, 6      ; If count of data is 6 and first is not `-` 
    je error1       ; ERROR
    
first:  
    cmp stroka[si], 32h     ; Check first simbol with `2`
    jna dop                 ; If first simbol <= '2' - check the validity of the characters
    
error1:
    mov bh, flag_err    ; Else bh = flag_err
    
dop:    
    ret
DIAPAZON ENDP


; Chech data is value or `-`
; Args:
;       Buffer input - stroka 
;       si - number of simbol
; Res:
;       bh - error flag
DOPUST PROC

    xor bh, bh
    xor si, si
    xor ah, ah
    xor ch, ch
    
    mov cl, kol     ; Count of input chars
    
m11:    
    mov al, [stroka + si]   ; In `al` - first 
    cmp al, 2dh             ; If first char is `-`
    jne testdop             ; If no
    cmp si, 00h             ; If yes
    jne error2              ; If another - ERROR
    jmp m13
    
testdop:
    cmp al, 30h     ; Data in [30h, 39h]
    jb error2
    cmp al, 39h
    ja error2
    
m13:    
    inc si
    loop m11
    jmp m14
    
error2: 
    mov bh, flag_err    ; Another error
    
m14:    
    ret
DOPUST ENDP



; ASCII to number 
; Args:               
;       cx - Count of input simbols
;       bx - number of simbol from last
; Res:
;       number - buffer numbers 
;       di - number of value in the array
AscToBin PROC
    xor ch, ch
    mov cl, kol
    xor bh, bh
    mov bl, cl
    dec bl
    mov si, 01h  ; In si, the weight of the discharge
    
n1: 
    mov al, [stroka + bx]
    xor ah, ah
    cmp al, 2dh     ; Check positive or negative
    je otr          ; if negative
    sub al, 30h
    mul si
    add [number + di], ax
    mov ax, si
    mov si, 10
    mul si
    mov si, ax
    dec bx
    loop n1
    jmp n2
otr:    
    neg [number + di]   ; Show negative in `adding` code
    
n2: 
    ret
AscToBin ENDP



; Number to ASCII
; Args
;       ax - number
; Res
;       out_str - numbers buffer
BinToAsc PROC
    xor si, si
    add si, 05h
    mov bx, 0Ah
    push ax
    cmp ax, 00h
    jnl mm1
    neg ax
    
mm1:    
    cwd
    idiv bx
    add dl,30h
    mov [out_str + si], dl
    dec si
    cmp ax, 00h
    jne mm1
    pop ax
    cmp ax, 00h
    jge mm2
    mov [out_str + si], 2dh
    
mm2:    
    ret
BinToAsc ENDP
      
      
c1 ENDS 
end start