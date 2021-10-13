def is_prime(n):
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 1
        return True


def get_product (lst):
    product=1
    for i in (lst):
        product=product*i
    return product

def get_cmmdc_1(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def get_cmmdc_2(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

def main():
    val = False
    while not val:
        print("1.Verificare nr prim ")
        print("2. Produs a n numere")
        print("3.CMMDC varianta 1")
        print("4.CMMDC varianta 2")
        print("x. Exit")
        optiune = input()
        if optiune == '1':
            nr=int(input("Scrieti un nr: "))
            print(is_prime(nr))
        elif optiune =='2':
            str=input("Adaugati nr separate prin virgula: ")
            lst=str.split(',')
            for i , x in enumerate(lst):
                lst[i]=int(x)
            print(get_product(lst))
        elif optiune == '3':
            a = int(input())
            b = int(input())
            print(get_cmmdc_1(a, b))
        elif optiune == '4':
            a = int(input())
            b = int(input())
            print(get_cmmdc_2(a, b))
        elif optiune == 'x':
            val = True
        else:
            print("Optiune incorecta")

if __name__ == '__main__':
    main()








