from cmath import sqrt

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
a=sqrt((x1-x2)**2+(y2-y1)**2)
b=sqrt((x2-x3)**2+(y2-y3)**2)
c=sqrt((x3-x1)**2+(y1-y3)**2)
p=(a+b+c)/2
print(f'Площадь треугольника = {sqrt(p*(p-a)*(p-b)*(p-c))}')


