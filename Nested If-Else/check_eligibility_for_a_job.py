age = int(input("Enter age: "))
degree = input("Do you have a degree? (Yes/No): ")

if age >= 18:
    if degree.lower() == "yes":
        print("Eligible for job")
    else:
        print("Not eligible (No degree)")
else:
    print("Not eligible (Underage)")