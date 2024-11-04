num=input("enter your number ")
numlen=len(num)
print(numlen)
if(numlen%2==0):
    midnum=int(num[numlen//2-1])
    num2=int(num[numlen//2])
    product=midnum*num2
    print(product)
else:
    num3=int(num[numlen//2])
    product2=num3*num3
    print(product2)