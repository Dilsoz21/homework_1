
#task2
massiv = [1, 2, 3, 4, 5, 6, 7, 8, 10, 20, 3, 3]


def search(massiv):
    result = 0
    for num in massiv:
        result ^= num
        print(massiv)


search(massiv)


#task3#
num = int(input("Enter the number:"))
list = [1, 3, 4, 5, 8, 9]

def move_to_end(num, list):
    for x in list:
        if num == x:
            list.remove(x)
            list.append(x)
            print(list)

move_to_end(num, list)

#task4
n = int(input("Enter number: "))

def daraja(n):
    if n > 1023 and n < 2048:
        print("10 1024")

    elif n > 511 and n < 1024:
        print("9 512")

    elif n > 255 and n < 512:
        print("8 256")

    elif n > 127 and n < 256:
        print("7 128")

    elif n > 63 and n < 127:
        print("6 64")

    elif n > 2**5 and n < 2**6:
        print("5 32")

    elif n > 15 and n < 33:
        print("4 16")

    elif n > 7 and n < 16:
        print("3 8")

    elif n < 8 and n > 3:
        print("2 4")

    else:
        print("Превышено")


daraja(n)


#task5
x = int(input("Enter number: "))
y = int(input("Enter again number: "))

def kilometres(x, y):
    day = 1
    while y > x:
        x *= 1.1
        day += 1
    print(day)


kilometres(x, y)