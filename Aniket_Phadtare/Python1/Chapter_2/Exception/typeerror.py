a=10
b="20"
try:
 c=a+b
 print(c)
except TypeError:
 print("Data Type Used In Operatiopn are Different ")
finally:
 print("Program Executed")