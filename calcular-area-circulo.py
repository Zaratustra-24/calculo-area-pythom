import math

# Paso 1: Solicitar al usuario que ingresse el radio delc ciculo.
radio= float(input("Por favor, ingrese el radio del circulo: "))
# Paso 2: Calcular el área del circulo utilizando la fórmula area= pi * radio^2
area= math.pi*radio**2
# Paso 3: Mostrar al usuario el área calculadamostrar mensaje: "El área del circulo con radio", radio, "es:", area
print("El área del circulo con radio", radio, "es:", area)