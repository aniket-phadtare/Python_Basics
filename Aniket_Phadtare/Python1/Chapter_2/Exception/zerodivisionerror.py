try:
    n1=int(input("Enter The First Number:"))
    n2=int(input("Enter The Second Number:"))
    r=n1/n2
    print(r)
except ZeroDivisionError:
    print("Number Cannot Be Divisible by 0")
finally:
    print("Program Executed")