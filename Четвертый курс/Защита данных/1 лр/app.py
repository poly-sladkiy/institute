import numpy as np

rows = 5
column = 7

russian_alpabeth = (chr(i) for i in range(ord('а'), ord('я') + 1))


def create_table(key: str):
    start_words = []
    updated_alphabet = list(russian_alpabeth)
    updated_alphabet.append(' ')
    updated_alphabet.append('.')
    updated_alphabet.append(',')
    
    for i in key:
        if i not in start_words:
            start_words.append(i)
            updated_alphabet.remove(i)

    updated_alphabet.sort()
    updated_alphabet = start_words + updated_alphabet

    table = np.array(updated_alphabet).reshape((rows, column))
    table.astype('str')

    return table, updated_alphabet


def encrypt(text: str, table: list):
    answer = ''

    for i in text:
        new_index = table.index(i) + column
        answer += table[new_index % (rows * column)]

    return answer


def decrypt(text: str, table: list):
    answer = ''

    for i in text:
        new_index = table.index(i) - column

        if new_index >= 0:
            answer += table[new_index]
        else:
            answer += table[rows * column - abs(new_index)]

    return answer


if __name__ == '__main__':
    print('Исходный текст:', text := input("Введите текст для шифрования: ").strip().lower().replace('ё', 'е'))
    print('Ключ:', key := input("Введите ключ для шифрования: ").strip().lower().replace('ё', 'е'))

    # text = 'Игнаков К.М.'.lower()
    # key = 'тест'.lower()

    table, slice_array = create_table(key)
    print(f'Таблица с ключем:\n{table}', end='\n\n')

    text_encrypt = encrypt(text, slice_array)
    print(f"Зашифрованный текст: {text_encrypt}")

    decrypt_table = slice_array.copy()
    decrypt_text = decrypt(text_encrypt, decrypt_table)

    print(f'Расшифрованный текст: {decrypt_text}')
