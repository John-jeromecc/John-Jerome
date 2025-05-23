while True:
    name = input("Enter your name: ")
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a valid number for age.")
        continue

    if age >= 18:
        print(f"Hello {name}, you are eligible to vote.")
    else:
        print(f"Hello {name}, you are not eligible to vote yet.")

    repeat = input("Do you want to check another person? (yes/no): ").lower()
    if repeat != "yes":
        print("Goodbye!")
        break
