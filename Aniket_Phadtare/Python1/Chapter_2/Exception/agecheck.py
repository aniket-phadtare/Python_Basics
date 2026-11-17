class AgeError(Exception):
    pass
def checkage(age):
    if age<0:
        raise AgeError("Age Cant Be Negative")
    else:
        print("Age Is Valid")
    return age
try:
    checkage(5)
except AgeError as e:
    print("Errror:",e)
finally:
    print("Program Executed")