def es_primo(numero: int) -> bool:
    contador = 0
    for i in range(1, numero+1):
        if i ==1 or i == numero:
            continue
        if numero % i ==0:
            contador += 1
            break
    if contador == 0:
        return True
    else:
        return False
    
## Option 2
# def es_primo(numero: int) -> bool:
# divisores = [x for x in range(2,numero) if numero % x == 0]
# return len(divisores) == 0


def run():
    numero = int(input("Escribe un numero:"))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")
    
# def run():
# numero: int = 3
# numero_es_primo: bool = es_primo(numero)



if __name__ =="__main__":
    run()