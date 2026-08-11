def checkLength(a):
    psw = a
    if len(psw) < 8:
        print("pswword length below requirement")
    else:
        return

def checkUpper(a):
    psw = a
    for i in psw:
        if i >= 'A' and i <='Z':
            return True
        else:
            return False
            
def checkLower(a):
    psw = a
    for i in psw:
        if i >= 'a' and i <='z':
           return True
        else:
            return False
            
            
def checkNumber(a):
    psw = a
    for i in psw:
        if i >= '0' and i <='9':
           return True
        else:
            return False

def checkSpecial(a):
    spc = ['@', '#', '$', '%', '&', '*', '!']
    psw = a
    for i in psw:
        if i in spc:
           return True
        else:
            return False

def checkSpace(a):
    psw = a
    if ' ' in psw:
        return False
    else:
        return True

    
def getpsw():
    psw = input("Enter pswword")
    return psw

def validateEmail():
    psw = getpsw()
    if checkLength(psw):
        validFlag = True
    else:
        validFlag = False
        print("password length is below req")
    if checkUpper(psw):
        validFlag = True
    else:
        validFlag = False
        print("password deos not contain any uppercase")
    if checkLower(psw):
        validFlag = True
    else:
        validFlag = False
        print("password does not contain lowercase")
    if checkNumber(psw):
        validFlag = True
    else:
        validFlag = False
        print("password deos no contain numericals")
    if checkSpecial(psw):
        validFlag = True
    else:
        validFlag = False
        print("password does not contain special characters")
    if checkSpace(psw):
        validFlag = True
    else:
        validFlag = False
        print("password contains space")
    if validFlag:
        print("The password is valid")
    else:
        print("The password is not valid")

validateEmail()
