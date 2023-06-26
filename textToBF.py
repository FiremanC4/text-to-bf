nwChars =' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

strChars = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

char = {
        ' ': 32, 
        '!': 33, 
        '"': 34, 
        '#': 35, 
        '$': 36, 
        '%': 37, 
        '&': 38, 
        "'": 39, 
        '(': 40, 
        ')': 41, 
        '*': 42, 
        '+': 43, 
        ',': 44, 
        '-': 45, 
        '.': 46, 
        '/': 47, 
        '0': 48, 
        '1': 49, 
        '2': 50, 
        '3': 51, 
        '4': 52, 
        '5': 53, 
        '6': 54, 
        '7': 55, 
        '8': 56, 
        '9': 57, 
        ':': 58, 
        ';': 59, 
        '<': 60, 
        '=': 61, 
        '>': 62, 
        '?': 63, 
        '@': 64, 
        'A': 65, 
        'B': 66, 
        'C': 67, 
        'D': 68, 
        'E': 69, 
        'F': 70, 
        'G': 71, 
        'H': 72, 
        'I': 73, 
        'J': 74, 
        'K': 75, 
        'L': 76, 
        'M': 77, 
        'N': 78, 
        'O': 79, 
        'P': 80, 
        'Q': 81, 
        'R': 82, 
        'S': 83, 
        'T': 84, 
        'U': 85, 
        'V': 86, 
        'W': 87, 
        'X': 88, 
        'Y': 89, 
        'Z': 90, 
        '[': 91, 
        '\\':92, 
        ']': 93, 
        '^': 94, 
        '_': 95, 
        '`': 96, 
        'a': 97, 
        'b': 98, 
        'c': 99, 
        'd': 100, 
        'e': 101, 
        'f': 102, 
        'g': 103, 
        'h': 104, 
        'i': 105, 
        'j': 106, 
        'k': 107, 
        'l': 108, 
        'm': 109, 
        'n': 110, 
        'o': 111, 
        'p': 112, 
        'q': 113, 
        'r': 114, 
        's': 115, 
        't': 116, 
        'u': 117, 
        'v': 118, 
        'w': 119, 
        'x': 120, 
        'y': 121, 
        'z': 122, 
        '{': 123, 
        '|': 124, 
        '}': 125, 
        '~': 126,
        }

cycD = {
        192 : '>+++[<++++>-]<[>++++<-]>[<++++>-]<',
        175 : '+++++++[>+++++<-]>[<+++++>-]<',
        150 : '++++++[>+++++<-]>[<+++++>-]<',
        140 : '+++++++[>++++<-]>[<+++++>-]<',
        120 : '++++[>++++++<-]>[<+++++>-]<',
        108 : '>+++[<++++>-]<[>+++<-]>[<+++>-]<',
        96 : '++++++[>++++<-]>[<++++>-]<',
        80 : '++++[>++++<-]>[<+++++>-]<',
        64 : '++++[>++++<-]>[<++++>-]<',
        56 : '++[>++++<-]>[<+++++++>-]<',
        48 : '+++[>++++<-]>[<++++>-]<',
        40 : '+++++[>++<-]>[<++++>-]<',
        32 : '++[>++++<-]>[<++++>-]<',
        24 : '++[>++++<-]>[<+++>-]<',
        16 : '>++++[<++++>-]<',
        12 : '>+++[<++++>-]<',
        8  : '>++[<++++>-]<',
        }


def valid_input(input):
    for i in input:
        if i not in char:
            return False
    return True

def convert(inp):
    def cc(x):
        t = inp.count(x) - 1
        return ')' if t else '('
    st = map(cc, inp)
    return tuple(st)
    
def cyc(x):
    j = char[x]
    nr = sorted(cycD, key=lambda a: abs(a-j))[0]
    res = cycD[nr]
    if (dst := j - nr) > 0:
        res += '+' * dst

    else:
        res += '-' * abs(dst)
    return res
    
def goto():
    cp = 0 # current pos 
    stp = '' #steps in bf
    while 1:
        np = yield stp #np - next pos
        if np > cp:
            stp = '>' * (np - cp)
        else:
            stp = '<' * (cp - np)
        cp = np
mv = goto()
next(mv)
def gt(st):
  return mv.send(st)
  
def literation(inp):
    letters = list(set(inp))
    res = ''.join(map(lambda x: cyc(x) + '>', letters))
    gt(ln := len(letters))
    for i in inp:
        res += gt(letters.index(i)) + '.'
        notCor = True
    while notCor:
        notCor = False
        for i in range(1, len(res)):
            if res[i-1] + res[i] in ('><', '<>', '-+', '+-'):
                res = res[:i-1] + res[i+1:]
                notCor = True
                break
    res += gt(ln)
    res += '<'.join(('[-]',) * (ln + 1))
    return res
        
  
def pointing(inp):
    point, res = 0, ''
    for i in inp:
        if (c := char[i]) > point:
            res += '+' * (c - point)
        elif c < point:
            res += '-' * (point - c)
        res += '.'
        point = c
    return res

def joinAll(inp):
    res = map(lambda x: char[x], inp)
    result = '.>'.join(map(lambda x: '+'*x, res)) + '.'
    return result 


if __name__ == '__main__':
    inp = input('Enter the text to convert:\n')
    if not valid_input(inp):
        print('incorrect input')
    else:
        print('\n')
        print(literation(inp))