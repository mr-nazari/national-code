from nationalcode import NationalCode
from colorama import init, Fore, Back
from os import system
init()

def banner():
    # green
    print(Back.GREEN + ' ' * 60)
    print(Back.GREEN + ' ' * 60)
    print(Back.GREEN + ' ' * 60)
    # white
    print(Back.WHITE + ' ' * 60)
    print(Back.WHITE + ' ' * 22 + Fore.BLACK + 'National Code' + ' ' * 25)
    print(Back.WHITE + ' ' * 60)
    # red
    print(Back.RED + ' ' * 60)
    print(Back.RED + ' ' * 60)
    print(Back.RED + ' ' * 60 + Back.RESET)

def main():
    while True:
        print(Fore.RESET, Back.RESET)

        print(Fore.GREEN, "[1] Check the correctness of the national code")
        print(Fore.WHITE, "[2] Create a random national code")
        print(Fore.RED, "[3] National codes between two numbers" + Fore.RESET)

        opt = input(' $---$ ').lower()
        print()
        if opt == "exit":
            print(Fore.YELLOW, "EXIT!!!")
            quit()
        elif opt == 'cls':
            system('cls')
            banner()
        elif opt == 'clear':
            system('clear')
            banner()
        elif opt == '1':
            if NationalCode.is_valid(input("Enter your national code: ")):
                print(Fore.GREEN, "Valid !")
            else:
                print(Fore.RED, "Invalid !")
        elif opt == '2':
            count = input("Enter count(use '>' for save result to a file) [default: 1]: ")
            if count == '':
                count = '1'
            if '>' in count:
                count, filename = count.split('>')
                with open(filename, mode='a') as f:
                    for _ in range(int(count)):
                        rm1 = NationalCode.random_m1()
                        f.write(rm1+'\n')
                        print("Random National Code (m1): ", rm1)
            else:
                for _ in range(int(count)):
                    print("Random National Code (m1): ", NationalCode.random_m1())
        elif opt == '3':
            num1, num2 = [int(input(f"({i}) Enter national code: ")) for i in range(1, 3)]
            count = input("Enter count(use '>' for save result to a file) [default: 1]: ")
            if count == '':
                count = '1'
            if '>' in count:
                count, filename = count.split('>')
                with open(filename, mode='a') as f:
                    for _ in range(int(count)):
                        rm1 = NationalCode.random_between_m1(num1, num2)
                        f.write(rm1+'\n')
                        print(f"Random National Code Bteween {num1} and {num2} (m1): ", rm1)
            else:
                for _ in range(int(count)):
                    print(f"Random National Code Bteween {num1} and {num2} (m1): ", 
                            NationalCode.random_between_m1(num1, num2)) 

if __name__ == "__main__":
    banner()
    main()