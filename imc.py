def imc(alt, mas):
    return mas/(alt**2)

def main():
    mas = float(input(''))
    alt = float(input(''))
    if imc(alt, mas)<18.5:
        print(f'{imc(alt, mas)}\nAbaixo do peso')
    elif 18.5 <= imc(alt, mas) < 25:
        print(f'{imc(alt, mas)}\nPeso normal')
    elif 25 <= imc(alt, mas) < 30:
        print(f'{imc(alt, mas)}\nSobrepeso')
    elif 30 <= imc(alt, mas) < 35:
        print(f'{imc(alt, mas)}\nObeso leve')
    elif 35<= imc(alt, mas) < 40:
        print(f'{imc(alt, mas)}\nObeso moderado')
    elif 40 <= imc(alt, mas):
        print(f'{imc(alt, mas)}\nObeso mórbido')

if __name__ == '__main__':
    main()
