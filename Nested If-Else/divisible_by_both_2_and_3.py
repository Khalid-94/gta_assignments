num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by both 2 and 3")
    else:
        print("Not divisible by 3")
else:
    print("Not divisible by 2")