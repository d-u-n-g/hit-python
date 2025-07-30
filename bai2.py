a=[]
k=int(input("Nhap so luong ptu cua list do:"))
for i in range(k):
    b=int(input("Nhap phan tu thu "+str(i+1)+":"))
    a.append(b)
print(a)
n=int(input("Nhap vao so dong cua ma tran:"))
m=int(input("Nhap vao so cot cua ma tran:"))
if len(a)< n*m:
    print("NO")
else:
    X=[]
    for i in range(n):
        hang=a[i*m : (i+1)*m]
        X.append(hang)
print("X("+ str(n) +"x"+str(m)+")="+str(X),end=',' if i<len(X) - 1 else '\n')
# print(str(X),end=',' if i<len(X) - 1 else '\n')