import console.N_RNS, console.Z, console.Q, console.P


def main():
    menu = 1
    while menu:
        print("Добро пожаловать в программу отладки!")
        print("Команды:")
        print("1 - модули натуральных чисел")
        print("2 - модули целых чисел")
        print("0 - выход")
        
        menu = int(input())
        
        if menu == 1:
            console.N_RNS.main()
        elif menu == 2:
            console.Z_RNS.main()
        elif menu == 0:
            pass
        else:
            print("Неизвестный ввод!")
    
    
if __name__ == "__main__":
    main()
