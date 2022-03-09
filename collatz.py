def collatz(number):
    if(number % 2 == 0):
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print('''It's time to enter your number ''')
while True:
    try:
        num = input("Enter your number : ")
        while num != 1:
            num = collatz(int(num))
        break
    except ValueError:
        print("Please enter a number ")
        continue
