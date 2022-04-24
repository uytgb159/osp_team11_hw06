#team11_program HW06
from select import select
from team_pkg import binTohex
from team_pkg import set_op
from team_pkg import fibonacci

while (True):
    menu=input("\nSelect menu: 1)b2h 2)set 3)fibo 4)exit ? ")
    if(menu=='1'):
        binTohex.bin2hex()
    elif(menu=='2'):
        set_op.setop()
    elif(menu=='3'):
        fibonacci.fibo()
    elif(menu=='4'):
        break
    else:
        print("Wrong input. ")
        
print("exit the program")