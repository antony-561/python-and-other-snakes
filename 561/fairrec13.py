def checkAt(email):
    em = email
    cnt = 0
    for i in em:
        if i == '@':
            cnt += 1
    if cnt==1:
        return em.index('@')
    else:
        return 0


def checkDot(email):
    em = email
    loc = 0
    for i in em:
        if '.' == i:
            loc = em.index(i)
    if loc > checkAt(em):
        return loc
    else:
        print("Dot not present")
        return 0
    
def checkDom(email):
    doms = [".com",".org",".in",".edu"]
    em = email
    for i in doms:
        if i in em:
            if email.index(i) >= checkDot(em):
                print("It is a valid Email Address!")
                return
        else:
            print("Domain Invalid")

def checkSpc(email):
    em = email
    if ' ' in em:
        print("Domain invalid: Space Found")
    else:
        return
        

def valEmail():    
    email = input("Enter Mail id")
    checkAt(email)
    checkSpc(email)
    checkDot(email)
    checkDom(email)

