a = int(input("Введите 1 число"))
b = int(input("Введите 2 число"))
c = int(input("Введите 3 число"))
if a > b:
    maximum = a
else: 
    maximum = b

if c > maximum:
    maximum = c

print ("Максимальное число ", maximum)
