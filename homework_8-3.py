
#homework 8.3

stevilo_1 = int(input("Vpiši prvo številko: "))
stevilo_2 = int(input("Vpiši drugo številko: "))
operacija = input("Vpišite matematično operacijo (+, -, *, /): ")

if operacija == "+":
    print(stevilo_1 + stevilo_2)

elif operacija == "-":
    print(stevilo_1 - stevilo_2)

elif operacija == "*":
    print(stevilo_1 * stevilo_2)

elif operacija == "/":
    print(stevilo_1 / stevilo_2)

else:
    print("Ne poznam te matematične operacije.")


