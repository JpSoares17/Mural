from math import pi

def comp(r):
    return 2*pi*r

def area(r):
    return pi*r**2

def area_e(r):
    return 4*pi*r**2

def vol_e(r):
    return (4*pi*r**3)/3

def main():
    r = float(input("Valor do raio: "))
    print(f'Comprimento: {comp(r)}', f'Área: {area(r)}', f'Área da esfera: {area_e(r)}', f'Volume da esfera: {vol_e(r)}', sep='.\n')

if __name__ == '__main__':
    main()
