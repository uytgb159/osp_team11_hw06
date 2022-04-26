#made by koo
#operate union and intersection of set
from ctypes import Union

def setop():
    str1=input("input the 1st list: ").split()
    str2=input("input the 2nd list: ").split()
    set1=set(map(int,str1))
    set2=set(map(int,str2))
    
    #union
    uni=set.union(set1, set2)
    list_uni=list(uni)
    print("union:",list_uni)
    
    #intersection
    inter=set.intersection(set1, set2)
    list_inter=list(inter)
    print("intersection:",list_inter)

if __name__=='__main__':
    setop()
