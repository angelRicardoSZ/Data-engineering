def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise Exception("Ingresa un número positivo")
        print(divisors(num))
        print("Termino")
    except ValueError:
        print("debes ingresar un numero")
    except Exception:
        print('El numero no puede ser negativo')
    
if __name__ =="__main__":
    run()
        