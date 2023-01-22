
;Regcom=01h, RegData=00h, InT of Transmit(V=RST.7),  Asin
const Reset 40h
const word2 0fdh
const com 05h
const N 32
const zond 0eeh
const MASKresiver 02h
const END 0ffh
jmp f1
skip 38h
jmp data
:f1
lxi sp,0300h
;программирование ВВ51
;mvi a,Reset
;out 01h ;
mvi a,word2 ;
out 01h ;
mvi a,com ;
out 01h ;
:m2
mvi a,zond ;проверим готовность 2-й машины 
out 00h ;запустим зонд
:m1
in 01h ; читаем регистр состояния ВВ51
ani MASKresiver ;выделяем значение разряда готовности данных в приемнике
jz m1 ;если 0, данных нет, ждем эхо
;приемник получил от 2-й машины что-то, срвниваем с зондом,
 in 00h
cpi zond ;
jnz m2 ;
 
; если не равны, 2-я что-то дурит, повторяем зондирование
;  если равны,значит принят Зонд,  начинам тансляцию своих данных


lxi h,stroka
mvi c,01h  ; регистр С -счетчик символов
mov a,c
:m3
cpi N
jz f2
ei
jmp m3 ;ждем прерывание от передатчика
:data   ; ПП записи в передатчик элем-в строки
mov a,m
out 00h 
inx h
inr c
mov a,c
ret

:f2
Lxi h,lab2 ;

:y2
in 01h;
ani MASKresiver;
jz y2;
in 00h;
cpi END  ;
jz y3 ;если 0 прием закончен и надо отображать фразу

mov m,a
inx h
jmp y2
 ; в HL паре сформирован адрес, где находится код END, но этот 
;код в память не записывается

:y3

const z 8
mvi l,z
in 0h
ani 80h
cpi 0h
;jz f11 ; если не готов -выход
lxi b,lab2
:f22
ldax b
out 0h
:f33
in 0h ;проверяем готовность к приему след-го символа
ani 80h
cpi 0h
;jz f33 ; если 0 не готов
inx b
dcr l
mov a,l
cpi 0h
jz f11
jmp f22
:f11
mvi a,04h

:f44
jmp f44
stroka dw 0h,0h,0h,0h,0h,0h,0h,0436h,0031h,076h,0156h,0930h,03Fh,027Ch,0h,0106h,006Fh,040h,027Ch,040h,040Bh,0h,0h,0h,0h,0h,0h,0h; Игнаков

lab1 dr 14 ;резервирум 14 ячеек памяти под нули
lab2 dr 30 ;резервирум 30 ячеек памяти под фразу
lab3 dr 14 ; под нули в конце фразы
