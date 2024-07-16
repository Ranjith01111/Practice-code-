a = int(input('sub 1:'))
b = int(input('sub 2:'))
c = int(input('sub 3:'))
d = int(input('sub 4;'))
e = int(input('sub 5:'))
m = a+b+c+d+e
print(m)
avg = m/5
n = avg
print(n)
if avg <= 100 and avg > 90:
    print('grade O')
elif avg <= 90 and avg > 80:
    print('grade A')
elif avg <= 80 and avg > 70:
    print('grade B')
elif avg <= 70 and avg >= 60:
    print('grade C')
elif avg >= 50:
    print('Pass')
else:
    print('F')
