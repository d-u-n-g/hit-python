s1=[]
s2=[]
s3=[]
s4=""
x=int(input("Nhap so ptu s1:"))
for i in range (x):
    x1=int(input("Nhap ptu thu "+str(i+1)+":"))
    s1.append(x1)
y=int(input("Nhap so luong ptu s2:"))
for i in range(y):
    y1=int(input("Nhap ptu thu "+str(i+1)+":"))
    s2.append(y1)
s1.reverse()
print(s1)
a=int(input("Nhap vao so nguen a (a>=1):"))
b=int(input("Nhap vao so nguyen b (a< b <=len(s2)):"))
if 1 <= a < b <= len(s2):
    s2[a:b] = s2[a:b][::-1]
    print(s2)
else:
    print("Gia tri a, b khong hop le")
for i in range(len(s1)):
    if i%2!=0:
        s3.append(s1[i])
print(s3)
lenght = min(len(s1), len(s2))
for i in range(lenght):
    s4 += s1[i] + s2[i]
s4 += s1[lenght:] + s2[lenght:]
print(s4)
