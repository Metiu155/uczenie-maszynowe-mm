def zad2a(list_names):
    for n in list_names:
        print(n)
zad2a(['Ania','Krystian','Zosia','Marcin','Piotr'])

def zad2b(list_numbers):
    multiplied_list_numbers = []
    for n in list_numbers:
        multiplied_list_numbers.append(n*2)
    
    return multiplied_list_numbers
        
print(zad2b([3,5,1,7,8]))

def zad2bv2(list_numbers):
    multiplied_list_numbers = [n*2 for n in list_numbers]
    return multiplied_list_numbers

print(zad2bv2([3,5,1,7,8]))

def zad2c(list_numbers):
    for n in list_numbers:
        if n %2 == 0:
            print(n)

zad2c(range(0,10))

def zad2d(list_numbers):
    a = False
    for n in list_numbers:
        if(a):
            print(n)
            a = False
        else: a = True      

zad2d(range(0, 10))