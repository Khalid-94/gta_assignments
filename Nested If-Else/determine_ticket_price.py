age = int(input("Enter age: "))

if age < 5:
    print("Free")
elif age <= 18:
    print("Discount")
else:
    print("Full price")