print(" WELCOME TO  PYTHON")
nombre = input("Ingrese su nombre : ")

print("Hello" , nombre )\

a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run

#----------------LOGICA ANIDADA -----------------------
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

#------- OPERADORES -------------------------------------
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)


a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)