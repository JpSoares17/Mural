def fahrenheit_celsius(temp):
    return (temp - 32) * (5/9)

def celsius_fahrenheit(temp):
    return (temp * (9/5)) + 32

def comparador_diferentes(tempA, escalaA, tempB, escalaB):
    temp_convert = 0
    if escalaB == 'C':
        temp_convert = celsius_fahrenheit(tempB)
    if escalaB == 'F':
        temp_convert = fahrenheit_celsius(tempB)
    if tempA>temp_convert:
        return tempA, escalaA
    if temp_convert>tempA:
        return tempB, escalaB
    
def comparador_iguais(tempA, escalaA, tempB, escalaB):
    if tempA>tempB:
        return tempA, escalaA
    if tempB>tempA:
        return tempB, escalaB
    
def main():
    #Leitura:
    temperaturaA = float(input('Digite uma temperatura: ')), input('Está em que escala? ').upper()[0]
    temperaturaB = float(input('Digite uma temperatura: ')), input('Está em que escala? ').upper()[0]

    #Processamento:
    if temperaturaA[1]==temperaturaB[1]:
        maior_temperatura = comparador_iguais(*temperaturaA, *temperaturaB)
    if temperaturaA[1]!=temperaturaB[1]:
        maior_temperatura = comparador_diferentes(*temperaturaA, *temperaturaB)

    #Saída:
    print(maior_temperatura)
if __name__ == '__main__':
    main()
