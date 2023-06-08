def collatz_conjecture(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    print(n)

# Take input from the user
num = int(input("Enter a positive integer: "))

# Call the collatz_conjecture function
collatz_conjecture(num)
