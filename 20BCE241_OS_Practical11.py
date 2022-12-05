# Created By Rana Jay on 21 - 04 - 2022

"""
        Practical 11
        Roll No. - 20BCE241 RANA JAY HARESHBHAI
        Subject - Operating system
        Object -  WAP to impelement fixed size partitioning
"""

from operator import itemgetter

def first(l,b):
    IF=0
    EF=0
    for i in range(len(b)):
        print(b[i])
        for j in range(len(l)):
            if(l[j][0] and l[j][1]>=b[i][1]):
                l[j][0]=False
                l[j][2]=l[j][1]-b[i][1]
                b[i][0]=False
                IF=IF+l[j][2]
                #print(IF)
                break

    sum=0
    for i in range(len(l)):
        if(l[i][0]):
            sum=sum+l[i][1]

    print("Sum of Empty hole :",sum)
    for i in range(len(b)):
        if(b[i][0]):
            if(sum>=b[i][1]):
                EF=b[i][1]
                break
            else:
                EF=0

    print("Internal Fragmentation : {} External Fragmentation : {}".format(IF,EF))


def best(l,b):
    l=sorted(l,key=itemgetter(1))
    IF = 0
    EF = 0
    for i in range(len(b)):
        print(b[i])
        for j in range(len(l)):
            if (l[j][0] and l[j][1] >= b[i][1]):
                l[j][0] = False
                l[j][2] = l[j][1] - b[i][1]
                b[i][0] = False
                IF = IF + l[j][2]
                # print(IF)
                break

    sum = 0
    for i in range(len(l)):
        if (l[i][0]):
            sum = sum + l[i][1]

    print("Sum of Empty hole :", sum)
    for i in range(len(b)):
        if (b[i][0]):
            if (sum >= b[i][1]):
                EF = b[i][1]
                break
            else:
                EF = 0

    print("Internal Fragmentation : {} External Fragmentation : {}".format(IF, EF))

def worst(l,b):
    l = sorted(l, key=itemgetter(1))
    l.reverse()
    IF = 0
    EF = 0
    for i in range(len(b)):
        print(b[i])
        for j in range(len(l)):
            if (l[j][0] and l[j][1] >= b[i][1]):
                l[j][0] = False
                l[j][2] = l[j][1] - b[i][1]
                b[i][0] = False
                IF = IF + l[j][2]
                # print(IF)
                break

    sum = 0
    for i in range(len(l)):
        if (l[i][0]):
            sum = sum + l[i][1]

    print("Sum of Empty hole :", sum)
    for i in range(len(b)):
        if (b[i][0]):
            if (sum >= b[i][1]):
                EF = b[i][1]
                break
            else:
                EF = 0

    print("Internal Fragmentation : {} External Fragmentation : {}".format(IF, EF))

def RanaJay():
    fo = open("20BCE241_OS_Practical11.txt","r")
    z=[]
    for i in fo:
        l1=list(map(int,i.split(" ")))
        z.append(l1)
    # l1=[200,400,600,500,300,250]
    # c=[375,210,468,491]
    l1=z[0]
    c=z[1]
    f=True
    print(l1,c)

    l=[]  # l = [ [ bit , value of memory hole , internal fragmentation ] ]
    for i in range(len(l1)):
        a=[]
        a.append(True)
        a.append(l1[i])
        a.append(0)
        l.append(a)
    print(l)

    b=[]
    for i in range(len(c)):
        a=[]
        a.append(True)
        a.append(c[i])
        b.append(a)

    while(f):
        print("""
            1) First Algorithem 
            2) Best Algorithem 
            3) Wrost Algorithem 
            4) exit
            Choose any one number :
            """)

        c = int(input())
        if (c == 1):
            first(l,b)
        elif (c == 2):
            best(l,b)
        elif (c == 3):
            worst(l,b)
        elif(c==4):
            f=False
        else:
            print("Invalid Number : ")

if __name__ == "__main__":
    RanaJay()