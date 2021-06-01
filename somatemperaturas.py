def fahrenheit_celsius(temp):
    return (temp - 32) * (5/9)

def celsius_fahrenheit(temp):
    return (temp * (9/5)) + 32

def somando_diferentes(tempA, escalaA, tempB, escalaB):
    temp_convertida = 0
    if escalaA == 'C':
        temp_convertida = celsius_fahrenheit(tempA)
    if escalaA == 'F':
        temp_convertida = fahrenheit_celsius(tempA)
    return float('{:.4f}'.format(temp_convertida+tempB)), escalaB

def somando_iguais(tempA, escalaA, tempB, escalaB):
    return tempA+tempB, escalaA

def main():
    #Leitura:
    temperaturaA = float(input('Digite uma temperatura: ')), input('Está em que escala? ').upper()[0]
    temperaturaB = float(input('Digite uma temperatura: ')), input('Está em que escala? ').upper()[0]

    #Processamento:
    if temperaturaA[1]==temperaturaB[1]:
        temperatura_somada = somando_iguais(*temperaturaA, *temperaturaB)
    if temperaturaA[1]!=temperaturaB[1]:
        temperatura_somada = somando_diferentes(*temperaturaA, *temperaturaB)

    #Saída:
    print(temperatura_somada)
        
if __name__ == '__main__':
    main()
