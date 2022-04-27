#!/usr/bin/python

def fibo():
    num=int(input("fibonacci number: "))
    if(num<1):
        print("wrong number")
        return
    elif(num==1):
        print(1, end=' ')
        print("F1 = 1")
    else:
        f=[0,1]
        print(f[1], end=' ')
        for i in range(2, num+1, 1):
            f.append(f[i-1]+f[i-2])
            print(f[i],end=' ')
    print("\nF%d = %d"%(num, f[num]))
    
if __name__=='__main__':
    fibo()
