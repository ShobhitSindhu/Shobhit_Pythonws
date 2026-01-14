try:
    num = int(input("Enter Amout: "))
    print("....")
    print(10/num)
except ZeroDivisionError:
    print("Cannot divivde by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution Completed")
    