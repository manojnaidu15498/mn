N = int(input())
while(1<=N<=100000):
    a=N
    if(a%2==0):
        print('Even')
        break
    elif(a%2!=2):
        print('Odd')
        break
    else:
        print('invalid')
