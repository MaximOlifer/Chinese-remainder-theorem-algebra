from modules.classes_RNS import *
from modules.functions_RNS import *


def test_N_1():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    if n1 > n2:
        ans = "больше"
    elif n1 == n2:
        ans = "равно"
    else:
        ans = "меньше"
    print("Результат: "+ans)
    
    
def test_N_2():
    n = RNS_Natural(input("Введите число: "))
    print("Равно ли число 0:")
    if n == RNS_Natural(0):
        print("Да")
    else:
        print("Нет")
    
    
def test_N_3():
    n = RNS_Natural(input("Введите число: "))
    n += RNS_Natural(1)
    print(n)
    

def test_N_4():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Сумма:")
    print(n1 + n2)
    

def test_N_5():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Разность:")
    print(n1 - n2)
    

def test_N_6():
    pass
    

def test_N_7():
    pass


def test_N_8():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Произведение:")
    print(n1 * n2)
    

def test_N_9():
    pass

def test_N_10():
    pass

def test_N_11():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Частное от деления:")
    print(n1 // n2)


def test_N_12():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("Остаток от деления:")
    print(n1 % n2)
   
   
def test_N_13():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("НОД:")
    print(gcd_rns(n1, n2))
    

def test_N_14():
    n1 = RNS_Natural(input("Введите первое число: "))
    n2 = RNS_Natural(input("Введите второе число: "))
    print("НОК:")
    print(lcm_rns(n1, n2))


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки модулей N!")
        print("Команды:")
        print("1 - тест модуля N-1")
        print("2 - тест модуля N-2")
        print("3 - тест модуля N-3")
        print("4 - тест модуля N-4")
        print("5 - тест модуля N-5")
        print("6 - тест модуля N-6")
        print("7 - тест модуля N-7")
        print("8 - тест модуля N-8")
        print("9 - тест модуля N-9")
        print("10 - тест модуля N-10")
        print("11 - тест модуля N-11")
        print("12 - тест модуля N-12")
        print("13 - тест модуля N-13")
        print("14 - тест модуля N-14")
        print("\n0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            test_N_1()
        elif menu == 2:
            test_N_2()
        elif menu == 3:
            test_N_3()
        elif menu == 4:
            test_N_4()
        elif menu == 5:
            test_N_5()
        elif menu == 6:
            test_N_6()
        elif menu == 7:
            test_N_7()
        elif menu == 8:
            test_N_8()
        elif menu == 9:
            test_N_9()
        elif menu == 10:
            test_N_10()
        elif menu == 11:
            test_N_11()
        elif menu == 12:
            test_N_12()
        elif menu == 13:
            test_N_13()
        elif menu == 14:
            test_N_14()
        
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод")
        input("\nНажмите enter для продолжения...")
    

if __name__ == "__main__":
    main()
    