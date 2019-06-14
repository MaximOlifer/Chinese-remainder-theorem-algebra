from modules.classes_RNS import *
from modules.functions_RNS import *
from os import system
from sys import platform


def test_1():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    if n1 > n2:
        ans = "больше"
    elif n1 == n2:
        ans = "равно"
    else:
        ans = "меньше"
    print("Результат: "+ans)
    
    
def test_2():
    n = RNS_Natural(input("Введите число: "))
    print("Равно ли число 0:")
    if n == RNS_Natural(0):
        print("Да")
    else:
        print("Нет")
    
    
def test_3():
    n = RNS_Natural(input("Введите число: "))
    n += RNS_Natural(1)
    print(n)
    

def test_4():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Сумма:")
    print(n1 + n2)
    

def test_5():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Разность:")
    if (n1 >= n2):
        print(n1 - n2)
    else:
        print("Ошибка! Первое число должно быть больше либо равно второму.")

def test_6():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Произведение:")
    print(n1 * n2)


def test_7():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Частное от деления:")
    print(n1 // n2)


def test_8():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Остаток от деления:")
    print(n1 % n2)
   
   
def test_9():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("НОД:")
    print(gcd_rns(n1, n2))
    

def test_10():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("НОК:")
    print(lcm_rns(n1, n2))


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки модулей N!")
        print("Команды:")
        print("1 - сравнение 2-х чисел")
        print("2 - проверка числа на 0")
        print("3 - добавление 1 к числу")
        print("4 - сложение")
        print("5 - вычитание")
        print("6 - умножение")
        print("7 - частное от деления")
        print("8 - остаток от деления")
        print("9 - НОД")
        print("10 - НОК")
        print("\n0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            test_1()
        elif menu == 2:
            test_2()
        elif menu == 3:
            test_3()
        elif menu == 4:
            test_4()
        elif menu == 5:
            test_5()
        elif menu == 6:
            test_6()
        elif menu == 7:
            test_7()
        elif menu == 8:
            test_8()
        elif menu == 9:
            test_9()
        elif menu == 10:
            test_10()
        
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод")
        input("\nНажмите enter для продолжения...")
        
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            system("clear") 
        elif platform == "win32":
            system("cls")      
        

if __name__ == "__main__":
    main()
