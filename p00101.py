

def outStr(a,b,c):
    print("Numbers :",a)
    print("LowerCase :", b)
    print("UpperCase :",c)

def getStr():
    numCnt = 0
    lowCnt = 0
    uppCnt = 0
    str1 = input("enter string")
    for i in str1:
        if i >= "0" and i <= "9":
            numCnt+=1
        elif i >= "a" and i <= "z":
            lowCnt +=1
        elif i >= "A" and i <= "Z":
            uppCnt += 1
    outStr(numCnt,lowCnt,uppCnt)


getStr()
