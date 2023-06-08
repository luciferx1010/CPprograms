def reverse_and_add(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    while True:
        reversed_num = int(str(num)[::-1])
        num += reversed_num

        if is_palindrome(num):
            break

    return num

# Example usage
number = int(input("Enter a number: "))
result = reverse_and_add(number)
print("Final palindrome sum:", result)
