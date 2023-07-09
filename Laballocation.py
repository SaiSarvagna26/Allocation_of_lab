x=int(input())
y=int(input())
z=int(input())
n=int(input())

difference_x=abs(x-n)
difference_y=abs(y-n)
difference_z=abs(z-n)

if difference_x<=difference_y  and difference_x<=difference_z:
    print("L1")
elif difference_y<=difference_x  and difference_y<=difference_z:
    print("L2")
else:
    print("L3")
    