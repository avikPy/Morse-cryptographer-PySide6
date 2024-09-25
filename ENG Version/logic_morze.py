russ = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890?!().,@')
eng = list('abcdefghijklmnopqrstuvwxyz1234567890?!().,@')
morzR = '.- -... .-- --. -.. .  ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. ---. ---- --.- --.-- -.-- -..- ..-.. ..-- .-.- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ..--.. -.-.-- -.--. -.--.- .-.-.- --..-- .--.-.'.split(' ')
morzE = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. ----- ..--.. -.-.-- -.--. -.--.- .-.-.- --..-- .--.-.'.split(' ')


dct_of_rus = {}
dct_of_morsK = {}
dct_of_eng = {}
dct_of_morsL = {}

for i in range(len(russ)):
    dct_of_rus[russ[i]] = morzR[i]
    dct_of_morsK[morzR[i]] = russ[i]

for i in range(len(eng)):
    dct_of_eng[eng[i]] = morzE[i]
    dct_of_morsL[morzE[i]] = eng[i]





def check(obj):
    return str(obj.checkState()).split('.')[1] == 'Checked'

def checked_duo(obj1, obj2, obj3):
    if check(obj1) and check(obj2):
        return True
    elif check(obj1) and check(obj3):
        return True
    elif check(obj2) and check(obj3):
        return True
    return False

def text2code(text : str) -> str:
    code = ''
    for el in text:
        if el.lower() in dct_of_rus:
            code += dct_of_rus[el.lower()] + ' '
        elif el.lower() in dct_of_eng:
            code += dct_of_eng[el.lower()] + ' '
        else:
            if not el == ' ':
                code += el + ' '
            else:
                code += '/ '
    return code

def code2kir(code : str) -> str:
    text = ''
    code = code.split()
    for el in code:
        if el in dct_of_morsK:
            text += dct_of_morsK[el]
        elif el == '/':
            text += ' '
        else:
            text += el    
        
    return text

def code2lat(code: str) -> str:
    text = ''
    code = code.split()
    for el in code:
        if el in dct_of_morsL:
            text += dct_of_morsL[el]
        elif el == '/':
            text += ' '
        else:
            text += el    
        
    return text
