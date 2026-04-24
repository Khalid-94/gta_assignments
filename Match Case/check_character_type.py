ch = input("Enter a character: ")

match ch:
    case _ if ch.lower() in "aeiou":
        print("Vowel")
    case _ if ch.isalpha():
        print("Consonant")
    case _ if ch.isdigit():
        print("Digit")
    case _:
        print("Special character")