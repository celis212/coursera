hrs = float(input("Enter Hours: "))
rate = float(input("Enter eate: "))
pay = rate * hrs
print("Pay:", pay)

#3.1 Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la 
# entrada para calcular el salario bruto. Pague la tarifa por hora por las horas hasta 40 y 1.5 
# veces la tarifa por hora por todas las horas trabajadas por encima de las 40 horas. Utilice 45 
# horas y una tarifa de 10,50 por hora para probar el programa (el pago debe ser 498,75). Debe usar 
# input para leer una cadena y float () para convertir la cadena en un número. No se preocupe por los 
# errores al verificar la entrada del usuario, asuma que el usuario escribe los números correctamente.
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("enter a numeric value")
    quit()

if h > 40:
    h1 = h - 40
    pay = (40*r)+(h1*r*1.5)
else:
    pay = h*r
print(pay)


def computepay(hours, rate):
    try:
        h = float(hours)
        r = float(rate)
    except:
        print("enter a numeric value")
        quit()
    if h > 40:
        h1 = h - 40
        pay = (40*r)+(h1*r*1.5)
    else:
        pay = h*r
    print(pay)


hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
computepay(hrs, rate)

score = input("Enter Score: ")
try:
    s=float(score)
except:
    print("enter a numeric value")
    quit()

if s >= 0 and s <= 1:
        if s >= .9:
            print("A")
        elif s >= .8 :
            print("B")
        elif s >= .7 :
            print("C")
        elif s >= .6 :
            print("D")
        else:
            print("F")
else:
    print('ingrese un valor correcto')


def computegrade(score):
    try:
        s=float(score)
    except:
        print("Bad score")
        quit()

    if s >= 0 and s <= 1:
            if s >= .9:
                print("A")
            elif s >= .8 :
                print("B")
            elif s >= .7 :
                print("C")
            elif s >= .6 :
                print("D")
            else:
                print("F")
    else:
        print('Bad score')

scr = input("Enter Score: ")
computegrade(scr)

count = 0
total = 0
while True:
    number = input("Enter a number: ")
    if number == "done":
        average = total/count
        print(total, count, average)
        break
    else:
        try:
            n = float(number)
        except:
            print("Invalid input")
            continue
        count += 1
        total = total + n


count = 0
total = 0
smallest = None
largest = None
while True:
    number = input("Enter a number: ")
    if number == "done":
        average = total/count
        largest = int(largest)
        smallest = int(smallest)
        print("Maximum is", str(largest))
        print("Minimum is", str(smallest))
        print(total, count, smallest, largest)
        break
    else:
        try:
            n = float(number)
        except:
            print("Invalid input")
            continue
        count += 1
        total = total + n
        small = n
        big = n
        if largest is None or big>largest:
            largest = big
            pass
        if smallest is None or small<smallest:
            smallest = small
            pass