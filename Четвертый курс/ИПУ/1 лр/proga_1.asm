
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
;���������������� ��51
;mvi a,Reset
;out 01h ;
mvi a,word2 ;
out 01h ;
mvi a,com ;
out 01h ;
:m2
mvi a,zond ;�������� ���������� 2-� ������ 
out 00h ;�������� ����
:m1
in 01h ; ������ ������� ��������� ��51
ani MASKresiver ;�������� �������� ������� ���������� ������ � ���������
jz m1 ;���� 0, ������ ���, ���� ���
;�������� ������� �� 2-� ������ ���-��, ��������� � ������,
 in 00h
cpi zond ;
jnz m2 ;
 
; ���� �� �����, 2-� ���-�� �����, ��������� ������������
;  ���� �����,������ ������ ����,  ������� ��������� ����� ������


lxi h,stroka
mvi c,01h  ; ������� � -������� ��������
mov a,c
:m3
cpi N
jz f2
ei
jmp m3 ;���� ���������� �� �����������
:data   ; �� ������ � ���������� ����-� ������
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
jz y3 ;���� 0 ����� �������� � ���� ���������� �����

mov m,a
inx h
jmp y2
 ; � HL ���� ����������� �����, ��� ��������� ��� END, �� ���� 
;��� � ������ �� ������������

:y3

const z 8
mvi l,z
in 0h
ani 80h
cpi 0h
;jz f11 ; ���� �� ����� -�����
lxi b,lab2
:f22
ldax b
out 0h
:f33
in 0h ;��������� ���������� � ������ ����-�� �������
ani 80h
cpi 0h
;jz f33 ; ���� 0 �� �����
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
stroka dw 0h,0h,0h,0h,0h,0h,0h,0436h,0031h,076h,0156h,0930h,03Fh,027Ch,0h,0106h,006Fh,040h,027Ch,040h,040Bh,0h,0h,0h,0h,0h,0h,0h; �������

lab1 dr 14 ;���������� 14 ����� ������ ��� ����
lab2 dr 30 ;���������� 30 ����� ������ ��� �����
lab3 dr 14 ; ��� ���� � ����� �����
