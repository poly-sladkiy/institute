; ��������� �������� ������ 50�50 � ������ ���, ������ �� DRQ1,���������� ��� � ��������� ���.
; ����� ������� ������� ��� 1 �� ���� RST
jmp mm
skip 40h ;������ ��� ������� ����������

; ������ ������� �������� � 0100h
:mm
mvi a,00h
out 02h  
mvi a,01h
out 02h
; ��������� ������ ������� ���� ������ 2500 ��������, 
; ������ ������  ������ � ������ � ���� ������� ������ �� ������ 
mvi a,00h
out 03h
mvi a,8ah
out 03h 

; ������ ����� ���������� � ��-����

mvi a,42h 
out 08h
:k
jmp k

skip 100h

db 00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,00h,0Fh,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,0Fh,0Fh,00h,00h,00h,00h,0Fh,00h,00h,0Fh,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,05h,09h,09h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,05h,05h,09h,09h,09h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,05h,05h,05h,09h,09h,09h,09h,09h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,05h,05h,05h,05h,09h,09h,09h,09h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,05h,05h,09h,05h,05h,09h,09h,09h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,05h,05h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,05h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,05h,05h,05h,09h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,05h,05h,05h,09h,05h,05h,09h,05h,05h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,05h,05h,09h,09h,09h,09h,09h,09h,05h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,0Fh,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,09h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,0Fh,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,0Fh,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,00h,00h,00h,0Fh,00h,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,00h,00h,00h,0Fh,00h,0Fh,0Fh,0Fh,0Fh,0Fh,00h,0Fh,0Fh,0Fh,0Fh,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h,00h



