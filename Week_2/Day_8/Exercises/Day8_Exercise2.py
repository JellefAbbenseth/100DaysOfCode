# Write your code below this line 👇

def prime_checker(number):
    prime_number = True
    if number == 1:
        print("It's a prime number.")
        return
    for nums in range(2, number):
        if number % nums == 0:
            prime_number = False
            print("It's not a prime number.")
            break
    if prime_number:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Test Primenumbers
for i in range(1, 101):
    print(i, end=" ")
    prime_checker(number=i)


