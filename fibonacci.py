#!/usr/bin/python

def fibo(num):
        if(num == 1 or num  == 2):
                return 1
        else:
                return(fibo(num-2) + fibo(num-1))


if __name__=='__main__':
        num = int(input("fibonacci input: "))
        for i in range(1,num+1,1):
                print(fibo(i))

        print("F%d = %d" %(num,fibo(num)))
