def zad1(name: str,surname: str):
   
    return "Czesc" + name + " " + surname

a = zad1("Ala","Mala")
print(a)

def zad2(a: int,b: int):
    return a*b

print(zad2(3,4))

def zad3(a: int):
    if (a%2 == 0):
        return True
    return False

print(zad3(4))

def zad4(a: int,b: int,c: int):
    if a+b>=c:
        return True
    return False

print(zad4(3,4,8))

def zad5(l: list,a: int):
        if a in l:
            return True
        return False


print(zad5([1,2,3,4,5],5))

def zad6(l1: list,l2: list):
    l3 = list(set(l1+l2))
    l3 = [a**3 for a in l3]
    return l3

print(zad6([4,5,6],[7,8,4]))

