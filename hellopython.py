import numbers; import strings; import lists; import tuples; import sets; import dictionaries


print("Welcome to the world of Python!!")
print("select below to explore python features:")
print("1. Operation on numbers")
print("2. Operation on strings")
print("3. Operation on lists")
print("4. Operation on tuples")
print("5. Operation on dictionary")
print("6. Operation on set")
print("7. Operation on files")

choice = int(input("Enter your choice:"))

if choice == 1 :
    print("1. Sum of numbers")
    print("2. Difference of two numbers")
    print("3. Product of numbers")
    print("4. Power of numbers")
    print("5. Square root of a number")
    print("6. Cuberoot of a number")
    print("7. Factorial of number")
    print("8. Table of a number")

    pick = int(input("Please enter your choice:"))

    if pick == 1:
        numbers.sum()
    elif pick == 2:
        numbers.difference()
    elif pick == 3:
        numbers.product()
    elif pick == 4:
        numbers.power()
    elif pick == 5:
        numbers.squareroot()
    elif pick == 6:
        numbers.cuberoot()
    elif pick == 7:
        numbers.factorial()
    elif pick == 8:
        numbers.printTable()

elif choice == 2:
    print("1. Reverse string")
    print("2. Print alphabet of strings")
    print("3. Slice a string")
    print("4. Check string for a palindrome")
    print("5. captal case string")
    print("6. Small case a string")
    print("7. Count numbers of characters in string")


