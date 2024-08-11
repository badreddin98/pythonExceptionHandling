def conversion(fahrenheit):
    # Task 2: Temperature Conversion:
    try:
        celsius = (float(fahrenheit) - 32) * 5/9
        return celsius
    except ValueError:
        return None
    # Task 4: Finally: 
    finally:
        print("Thank you for using the weather forecast application!")

def main():
    # Task 1: Ask for temperature in Fahrenheit:
    user = input("Enter temperature in Fahrenheit: ")
    celsius = conversion(user)    
    if celsius is not None:
        print(f"{user} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    # Task 3: User Experience:
    else:
        print("Please enter a valid number.")

if __name__ == "__main__":
    # Ensure that the main function runs when the script is executed
    main()
