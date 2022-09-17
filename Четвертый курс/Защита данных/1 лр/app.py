abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
specs = ' ,.:;-!?)('

text = '''Игнаков Константин Михайлович'''

sentense = [i.lower() for i in text]

for i in specs:
    while sentense.count(i) > 0:
        sentense.pop(sentense.index(i))
sentense = ''.join(sentense)

key = 'политех'

print(f"Исходный текст: {text}\n"
      f"Ключ: {key}")

addSymbol = 'х'
preList = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

for i in range(len(key)):
    preList[i] = key[i]

abcWithoutKey = abc
for i in key:
    abcWithoutKey.pop(abcWithoutKey.index(i))
abc = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

for i in range(len(key), len(preList)):
    preList[i] = abcWithoutKey[i - len(key)]

codeList = [
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','','']
]
tmp = 0
for i in range(4):
    for j in range(8):
        codeList[i][j] = preList[tmp]
        tmp += 1

del tmp, abcWithoutKey, specs, preList

sentenseReacharge = []
for i in range(0, len(sentense), 2):
    try:
        if sentense[i] != sentense[i + 1]:
            sentenseReacharge.append(sentense[i] + sentense[i + 1])
        else:
            sentense = sentense[:i + 1] + addSymbol + sentense[i + 1:]
            sentenseReacharge.append(sentense[i] + sentense[i + 1])
    except IndexError:
        sentenseReacharge.append(sentense[-1] + addSymbol)

del sentense

def takeIndex(code):
    global codeList
    ans = [[i, _list.index(code)] for i,_list in enumerate(codeList) if code in codeList[i]]
    return ans

def Check(indexF, indexS):
    global codeList
    if indexF[0][1] == indexS[0][1]: #collumn
        (indexF[0][0] + 3) % 4, (indexS[0][0] + 3) % 4
    elif indexF[0][0] == indexS[0][0]: #line
        (indexF[0][1] + 7) % 8, (indexS[0][1] + 7) % 8
    else: #square
        buf = indexF[0][1]
        indexF[0][1] = indexS[0][1]
        indexS[0][1] = buf
    return indexF, indexS

codes = []
for code in sentenseReacharge:
    codes.append(Check(takeIndex(code[0]), takeIndex(code[1])))

AnswerIndex = ''
for i in codes:
    AnswerIndex += codeList[i[0][0][0]][i[0][0][1]]
    AnswerIndex += codeList[i[1][0][0]][i[1][0][1]]
print(f"Шифр текст: {AnswerIndex}")
