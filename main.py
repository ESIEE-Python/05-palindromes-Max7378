"""Programme qui renvoie si un mot ou une suite de chiffres est un palindrome"""
#### Fonction secondaire

INTAB = "AÀàBCçDdEÉèéëêFGHIïJKLMNOôPQRSTUVWXYZ"
OUTTAB = "aaabccddeeeeeefghiijklmnoopqrstuvwxyz"
TRANTAB = str.maketrans(INTAB,OUTTAB)
CAR_A_SUPP = " ',-:!?,"
TRANTAB1 = str.maketrans('', '', CAR_A_SUPP)

def ispalindrome(p):
    """fonction ispalindrome"""
    p1=p.translate(TRANTAB).translate(TRANTAB1)
    l1=len(p1)
    for i in range(0,l1//2):
        if p1[i]!=p1[l1-i-1]:
            print (p, "n'est pas un palindrome")
            return False
    print (p, "est un palindrome")
    return True


#### Fonction principale
def main():
    """Fonction main qui utilise ispalindrome"""
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
