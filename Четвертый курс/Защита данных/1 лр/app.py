import numpy as np

rows = 5
column = 7

russian_alpabeth = (chr(i) for i in range(ord('а'), ord('я') + 1))

def create_table(key: str):
    start_words = []
    updated_alpbeth = list(russian_alpabeth)
    updated_alpbeth.append(' ')
    updated_alpbeth.append('.')
    updated_alpbeth.append(',')
    
    for i in key:
        if i not in start_words:
            start_words.append(i)
            updated_alpbeth.remove(i)

    updated_alpbeth.sort()
    updated_alpbeth = start_words + updated_alpbeth

    table = np.array(updated_alpbeth).reshape((rows, column))
    table.astype('str')

    return table, updated_alpbeth


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
            answer += table[rows * column - new_index]

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
