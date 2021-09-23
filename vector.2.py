import math

a = float(input("请输入一条边(A)"))
ade = float(input("请输入一个角(A)"))/360*2*math.pi
b = float(input("请输入一条边(B)"))
bde = float(input("请输入一个角(B)"))/360*2*math.pi

AX = float(format(math.cos(ade)*a, '.3f'))
AY = float(format(math.sin(ade)*a, '.3f'))
BX = float(format(math.cos(bde)*b, '.3f'))
BY = float(format(math.sin(bde)*b, '.3f'))

X = AX+BX
Y = AY+BY

c = format((X**2+Y**2)**(1/2), '.3f')
cde = float(format(math.atan((Y)/(X))/(2*math.pi)*360, '.3f'))

if X >= 0:
    if cde <= 0:
        cde = 360+cde
if X < 0:
    cde = 180+cde
        

print("因求长%s"%c)
print("因求角度%s"%cde)
aa = input()


"""
power胖丸
"""
