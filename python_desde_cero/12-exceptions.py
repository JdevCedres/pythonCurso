# Exceptions Handling

numberOne, numberTwo = 5, 1
numberTwo = "1"

# try except control de errores

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try excpt else 

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción 
    print("La ejecución continua correctamente")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción 
    print("La ejecución continua correctamente")
finally: # Opcional
    # Se ejucuta siempre, pase lo que pase
    print("La ejecución continua...")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error TypeError")

except ValueError:
    print("Se ha producido un error ValueError")


# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except ValueError as e: # capturamos y printamos toda la información del error 
    print(e)

except Exception as e: # para cualquier error
    print(e)
