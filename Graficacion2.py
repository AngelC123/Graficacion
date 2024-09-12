'''
edad = int(input("Ingrese la edad: "))

if edad < 18:
    print("Eres menor de edad.")

status = 400

match status:
    case 400:
        print("Bad Request")
'''

'''
def suma(num1, num2):
    res = num1 + num2
    return res

print("Si sumo 2 + 5 = ",suma(2,5))
print("Si sumo 10 + 9",suma(10,9))

def imprime2(num1=None, num2=None):
    print("="*20)
    if num1 != None:
        print("El número 1 es: ",num1)
    if num2 != None:
        print("El número 2 es: ",num2)

imprime2(5,6)
imprime2(5)
imprime2(num2=10)
imprime2(0,1)
'''

'''
class MiClase:
    def __init__(self, valor1=10):
        self.atributo = valor1
        print("Inicializa el objeto")

    def metodo1(self):
        print("El valor del atributo es:",self.atributo)

a = MiClase()
a.metodo1()
'''