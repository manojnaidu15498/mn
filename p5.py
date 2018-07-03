A = int(input())
B = int(input())
C = int(input())
if(A>B and A>C):
    large=A
elif(B>A and B>C):
    large=B
else:
    large=C
    print(large)
