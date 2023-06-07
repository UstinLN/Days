code_library = {'A': '00011', 'B': '11001', 'C': '01110', 'D': '01001',
                'E': '00001', 'F': '01101', 'G': '11010', 'H': '10100',
                'I': '00110', 'J': '01011', 'K': '01111', 'L': '10010',
                'M': '11100', 'N': '01100', 'O': '11000', 'P': '10110',
                'Q': '10111', 'R': '01010', 'S': '00101', 'T': '10000',
                'U': '00111', 'V': '11110', 'W': '10011', 'X': '11101',
                'Y': '10101', 'Z': '10001', ' ': '00100'}
two_code_library = {'00011': 'A', '11001': 'B', '01110': 'C', '01001': 'D',
                    '00001': 'E', '01101': 'F', '11010': 'G', '10100': 'H',
                    '00110': 'I', '01011': 'J', '01111': 'K', '10010': 'L',
                    '11100': 'M', '01100': 'N', '11000': 'O', '10110': 'P',
                    '10111': 'Q', '01010': 'R', '00101': 'S', '10000': 'T',
                    '00111': 'U', '11110': 'V', '10011': 'W', '11101': 'X',
                    '10101': 'Y', '10001': 'Z', '00100': ' '}


def encrypt(message):
    cipher = '11111'
    for letter in message:
        cipher += code_library[letter]
    return cipher


def decrypt(message):
    cipher = ''
    cip = ''
    n = 0
    for letter in message:
        n += 1
        cipher += letter
        if cipher == '11111' and n == 5:
            n = 0
            cipher = ''
            continue
        elif cipher == '00010' and n == 5:
            print(cip, end='\n')
            n = 0
            cipher = ''
            cip = ''
        elif n == 5:
            cip += two_code_library[cipher]
            n = 0
            cipher = ''
    return cip


def main():
    print("Введите '1' если хотите закодировать, если декодировать, то '2': ")
    choice = int(input())
    if choice == 1:
        print("Введите текст: ")
        message = input()
        result = encrypt(message.upper())
        print(result)
    elif choice == 2:
        print("Введите шифр: ")
        message = input()
        result = decrypt(message)
        print(result)
    else:
        print("Вы сделали что-то неправильно, попробуйте ещё раз.")
        exit


if __name__ == '__main__':
    main()