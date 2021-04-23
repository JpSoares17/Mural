def cond(c):
    if c in 'AEIOU':
        return c in 'AEIOU'
    else:
        return c in 'AEIOU'

def main():
    c = input('').upper()
    print(cond(c))

if __name__ == '__main__':
    main()
