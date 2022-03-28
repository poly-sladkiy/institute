;-------------- Macro --------------

; Macros for output data
print macro srting      
    mov dx, offset srting
    mov ah, 09h
    int 21h
endm

; Macros for input data
input macro srting  
    mov dx, offset srting
    mov ax, 0A00h
    int 21h
endm

; Macro Draw Window
; xStart - left-top - col
; yStart - left-top - row
; xEnd   - rigth-down - col
; yEnd   - rigth-down - row
drawWindow macro xStart, yStart, xEnd, yEnd
    push ax
    push dx
    
    mov ax, 0600h
    
    mov ch, yStart              ;????? ??????? ???? - ??????
    mov cl, xStart              ;????? ??????? ???? - ???????
    
    mov dh, yEnd                ;?????? ?????? ???? - ??????
    mov dl, xEnd                ;?????? ?????? ???? - ???????
    
    mov bh, mainColor           ;????????? ????? ???? ? ????? ????
    
    int 10h                     ;?????????? ?????????
    
    pop dx
    pop ax
endm

drawShadow macro xStart, yStart, xEnd, yEnd
    push ax
    push dx

    inc xStart
    inc yStart
    inc xEnd
    inc yEnd

    mov ax, 0600h
    
    mov ch, yStart              ;????? ??????? ???? - ??????
    mov cl, xStart              ;????? ??????? ???? - ???????
    
    mov dh, yEnd                ;?????? ?????? ???? - ??????
    mov dl, xEnd                ;?????? ?????? ???? - ???????
    
    mov bh, shadowColor         ;????????? ????? ???? ? ????? ????
    
    int 10h                     ;?????????? ?????????
    
    dec xStart
    dec yStart
    dec xEnd
    dec yEnd

    pop dx
    pop ax
endm

clearWindow macro
    mov ax, 0003
    int 10h
endm

drawErrorWindow macro xStart, yStart, xEnd, yEnd
    mov ax, 0600h
    
    mov ch, yStart              ;????? ??????? ???? - ??????
    mov cl, xStart              ;????? ??????? ???? - ???????
    
    mov dh, yEnd                ;?????? ?????? ???? - ??????
    mov dl, xEnd                ;?????? ?????? ???? - ???????
    
    mov bh, 01000000b           ;????????? ????? ???? ? ????? ????
    
    int 10h                     ;?????????? ?????????
endm

drawAnswerWindow macro xStart, yStart, xEnd, yEnd
    push ax
    push dx

    mov ax, 0600h
    
    mov ch, yStart      ;????? ??????? ???? - ??????
    mov cl, xStart      ;????? ??????? ???? - ???????
    
    mov dh, yEnd        ;?????? ?????? ???? - ??????
    mov dl, xEnd        ;?????? ?????? ???? - ???????
    
    mov bh, 01110001b   ;????????? ????? ???? ? ????? ????
    
    int 10h             ;?????????? ?????????
    
    pop dx
    pop ax
endm

printStringInWindow macro string, col, row
    push ax
    push dx
    
    mov ah, 2
    mov dh, row
    mov dl, col
    mov bh, 0
    int 10h
    
    mov ah, 09h
    mov dx, offset string
    int 21h
    
    pop dx
    pop ax
endm

printBytesInWindow macro string, col, row
    push ax
    push dx
    
    mov ah, 2
    mov dh, row
    mov dl, col
    mov bh, 0
    int 10h
    
    mov ah, 09h
    mov dx, string
    int 21h
    
    pop dx
    pop ax
endm

pressButtonW macro y1, y2, pointToMove
    cmp y1, 0d
    je pointToMove
    
    dec y1
    dec y2
    
    jmp pointToMove
endm

pressButtonS macro y1, y2, pointToMove
    cmp y2, 24d
    je pointToMove
    
    inc y2
    inc y1
    
    jmp pointToMove
endm

pressButtonA macro x1, x2, pointToMove
    cmp x1, 0d
    je pointToMove
    
    dec x1
    dec x2
    
    jmp pointToMove
endm

pressButtonD macro x1, x2, pointToMove
    cmp x2, 79d
    je pointToMove
    
    inc x2
    inc x1
    
    jmp pointToMove
endm

sleep macro time
    mov al, 0
    mov ah, 86h
    mov cx, time
    int 15h
endm

;-------------- Macro -------------- END

;-------------- Data --------------
.model small
.data

; MESSAGES
    pressAnyKey db 'Press any key.', 10, '$'

    mess1   db 10, 13, 'Move window: W, A, S, D.. Press <Enter>$'
    lab3    db 'Laboratory work #3','$'
    author  db 13,10, 'Ignakov Konstantin 19-V-2'
    
    perevod db 10,13,'$'
    
    inputError      db 'Input Error!', 10, '$'
    divByZeroError  db 'Divition by zero!', 10, '$'
    overflow        db 'Overflow!', 10, '$'
    overflowSum     db 'Overflow Sum!', 10, '$'
    
    sumText     db 'Sum of elements: ','$'
    lenSumText = $ - sumText
    
    mulText     db 'Mul of elements: ','$'
    lenMulText = $ - mulText
    
    sredText    db 'Srednee: ','$'
    lenSredText = $ - sredText
        
    prochText   db 'Prochent: ','$'
    lenProchText = $ - prochText
    
    out_str         db 6 dup (' '),'$'
    enter_please    db 'Input value: $'

; COLORS

    mainColor db 50h
    shadowColor db 30h

; COORDINATES

    mainWindowX1 db 5d
    mainWindowX2 db 30d
    mainWindowY1 db 5d
    mainWindowY2 db 15d

    secondWindowX1 db 5d
    secondWindowX2 db 35d
    secondWindowY1 db 5d
    secondWindowY2 db 15d

    cursorX db 0d
    cursorY db 0d

; VALUES FOR TASK

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
    
    flag_err equ 1

.stack 0ffh

.code
.386
start:

    mov ax, @data
    mov ds, ax
    
    ; video-mode #3 text 80*25
    clearWindow
    
    ; print mess1
    print mess1
    
    ; draw main window
    drawShadow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    drawWindow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    
;-------------- Move Main Window --------------
    mov ah, 0
    int 16h
    
moveWindow:

    clearWindow
    drawShadow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    drawWindow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    call hideCursor

    mov ah, 0
    int 16h
    
    ; if <Enter>
    cmp ax, 1c0dh
    je startInput
    
    ; press W
    cmp al, 77h
    jne mainWindowsCheckPressA
    pressButtonW mainWindowY1, mainWindowY2, moveWindow
    
    ; press A
mainWindowsCheckPressA:
    cmp al, 61h
    jne mainWindowsCheckPressS
    pressButtonA mainWindowX1, mainWindowX2, moveWindow
    
    ; press S
mainWindowsCheckPressS:
    cmp al, 73h
    jne mainWindowsCheckPressD
    pressButtonS mainWindowY1, mainWindowY2, moveWindow
    
    ; press D
mainWindowsCheckPressD:
    cmp al, 64h
    jne moveWindow
    pressButtonD mainWindowX1, mainWindowX2, moveWindow
    
;-------------- Move Main Window -------------- END

;-------------- Input Data --------------
startInput:

    mov al, mainWindowX1
    mov cursorX, al
    
    mov al, mainWindowY1
    mov cursorY, al

    clearWindow
    drawShadow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    drawWindow mainWindowX1, mainWindowY1, mainWindowX2, mainWindowY2
    
    xor di, di
    mov cx, siz     ; cx - array size
    
inputValues:
    push cx
    
    ; Enter value
    printStringInWindow enter_please, cursorX, cursorY
    
    input in_str        ; ???? ????? ? ???? ??????
    
    call diapazon       
    cmp bh, flag_err    ; if flag_err = 1 - error
    je inErr            

    call dopust         
    cmp bh, flag_err    ; if flag_err = 1 - error
    je inErr           
    
    call AscToBin       ; Convert string to value
    inc di
    inc di
    
    pop cx
    
    inc cursorY
    
    loop inputValues
    jmp searchSum
    
inErr:          
    drawErrorWindow 27, 9, 53, 16
    
    printStringInWindow inputError, 34d, 12d
    printStringInWindow pressAnyKey, 33d, 14d
    
    call hideCursor
    mov ah, 0           ; wait input
    int 16h
    jmp endProgram
    
;-------------- Input Data -------------- END

;-------------- Count answer --------------
    
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
    
    jmp outputRes
    
    
; Print errors
overFlowErr:

    drawErrorWindow 27, 9, 53, 16
    
    printStringInWindow overflow, 34d, 12d
    printStringInWindow pressAnyKey, 33d, 14d
    
    call hideCursor
    mov ah, 0           ; wait input
    int 16h
    jmp endProgram
    
zero:

    drawErrorWindow 27, 9, 53, 16
    
    printStringInWindow divByZeroError, 34d, 12d
    printStringInWindow pressAnyKey, 33d, 14d
    
    call hideCursor
    mov ah, 0           ; wait input
    int 16h
    
    jmp endProgram
        
overFlowErrSum: 

    drawErrorWindow 27, 9, 53, 16
    
    printStringInWindow overflowSum, 34d, 12d
    printStringInWindow pressAnyKey, 33d, 14d
    
    call hideCursor
    mov ah, 0           ; wait input
    int 16h
           
    jmp outputRes
    
;-------------- Count answer -------------- END


;-------------- Output answer --------------

outputRes:

    ; clearWindow
    drawAnswerWindow 20, 5, 50, 17
    
    mov al, 21
    mov cursorX, al
    
    mov al, 6
    mov cursorY, al
    
    printStringInWindow sumText, cursorX, cursorY
    add cursorX, lenSumText
    
    mov ax, sumres
    call BinToAsc
    
    printStringInWindow out_str, cursorX, cursorY

    inc cursorY
    mov al, 21
    mov cursorX, al
    
    mov cx, 6            ; clear buffer
    xor si, si
clear1:     
    mov [out_str+si], ' '
    inc si
    loop clear1

    printStringInWindow mulText, cursorX, cursorY
    add cursorX, lenMulText
    
    mov ax, mulres   
    call BinToAsc
    
    printStringInWindow out_str, cursorX, cursorY

    inc cursorY
    mov al, 21
    mov cursorX, al
    
    mov cx,6            ; clear buffer
    xor si, si
clear2:     
    mov [out_str+si],' '
    inc si
    loop clear2

    printStringInWindow sredText, cursorX, cursorY
    add cursorX, lenSredText
    
    mov ax, sredres  
    call BinToAsc
        
    printStringInWindow out_str, cursorX, cursorY
    
    inc cursorY
    mov al, 21
    mov cursorX, al
    
    mov cx,6            ; clear buffer
    xor si,si
        
clear3:     
    mov [out_str + si], ' '
    inc si
    loop clear3

    printStringInWindow prochText, cursorX, cursorY
    add cursorX, lenProchText
    
    mov ax, prochres
    call BinToAsc
    
    printStringInWindow out_str, cursorX, cursorY

    jmp endProgram
    
    
drawRamka:
     mov al, 21
     mov cursorX, al

     mov al, 4
     mov cursorY, al
     
     mov cx, 30
     
printTopGorizontal:
    printStringInWindow prochText, cursorX, cursorY
    printBytesInWindow 20h
   

;-------------- Output answer -------------- END
    
endProgram:
    mov ah, 02
    int 21h
    
    mov ax, 4c00h
    int 21h
    

;-------------- Procedures --------------
    
; Hide cursor
hideCursor PROC 
    mov ah,2   
    mov dh,26         
    mov dl,81
    mov bh,0
    int 10h 
    ret
ENDP

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

end start