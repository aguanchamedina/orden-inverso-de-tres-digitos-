# DEVOLVER NÚMERO DE TRES DIGITOS EN ORDEN INVERSO 

print("---------------------------------------")
print("-----------ORDEN INVERSO---------------")
print("---------------------------------------")


# INPUT
n = int(input("Ingrese un número de 3 dígitos: "))

# PROCESS

NUMERO1 = (n % 1000) // 100
NUMERO2 = (n % 100) // 10
NUMERO3 = n % 10

# OUTPUT

print("El orden inverso de: "+ str(n) + " " + "es:" + " " + str(NUMERO3) + str(NUMERO2) + str(NUMERO1) )