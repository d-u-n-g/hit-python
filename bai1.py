n=int(input("Nhap so luong ptu cua list a (>=7):"))
while n<7:
    n=int(input("Nhap lai so luong ptu cua list a (>=7):"))
a=[]
for i in range(n):
    b=int(input("Nhap phan tu thu "+ str(i+1)+": "))
    a.append(b)
print(a)
x=float(input("Nhap so X bat ki: "))
print("So lan xuat hien cua X trong a la:",a.count(x))
a[1:6]=[8,5,4,0,1,3]
print(a)
for i in range(len(a)):
    max=a[0]
    min=a[0]
    if a[0]<a[i]:
        max=a[i]
    if a[0]>a[i]:
        min=a[i]
print("Max cua a la:",max)
print("Min cua a la:",min)
y=float(input("Nhap so Y bat ki:"))
a.insert(0,y)
print("List a sau khi chen Y vao dau:",a)
if a==a.sort():
    print("TANG")
elif a==a.sort(reverse=True):
    print("GIAM")
else:
    print("NO")