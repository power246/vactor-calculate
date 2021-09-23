import math

num = 0
long = []
degree = []

def culc(a,ade,b,bde):
    global c, cde
    a = float(a)
    b = float(b)
    ade = float(ade/360*2*math.pi)
    bde = float(bde/360*2*math.pi)
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


while num < 2:
    num = int(input('请输入一共的矢量数(x>=2)：'))

for x in range(num):
    x += 1
    long.append(float(input('请输入第%s条边'%x)))
    degree.append(float(input('请输入第%s个角'%x)))

culc(long[0],degree[0],long[1],degree[1])

if num > 2:
    for i in range(num-2):
        i += 2
        culc(c,cde,long[i],degree[i])

print("因求长%s"%c)
print("因求角度%s"%cde)
aa = input()


"""
power胖丸
"""


