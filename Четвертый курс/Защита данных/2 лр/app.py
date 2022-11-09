from itertools import zip_longest, cycle


def xor_crypt_string(data: str, key: str):
    xored = ''
    for (x, y) in zip_longest(data, cycle(key)):
        if not x:
            break
        xored += chr(ord(x) ^ ord(y))
    return xored


if __name__ == '__main__':
    print('Исходный текст:', text := input("Введите текст для шифрования: ").strip().lower().replace('ё', 'е'))
    print('Ключ:', key := str(input("Введите ключ для шифрования: ")))

    encode_text = xor_crypt_string(text, key)
    print('Зашифрованный текст:', encode_text, 'в бинарном виде:', ' '.join(format(ord(x), 'b') for x in encode_text))

    decode_text = xor_crypt_string(encode_text, key)
    print('Расшифрованный текст:', decode_text)
