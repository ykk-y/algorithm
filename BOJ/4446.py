import sys
change={'a':'e', 'i':'o', 'y':'u', 'e':'a', 'o':'i', 'u':'y','A':'E', 'I':'O', 'Y':'U', 'E':'A', 'O':'I', 'U':'Y',
        'b':'p', 'k':'v', 'x':'j', 'z':'q', 'n':'t', 'h':'s', 'd':'r', 'c':'l', 'w':'m', 'g':'f', 'p':'b', 'v':'k',
    'j':'x', 'q' :'z','t':'n', 's':'h' ,'r': 'd', 'l':'c', 'm':'w', 'f':'g','B':'P', 'K':'V', 'X':'J', 'Z':'Q',
    'N':'T', 'H':'S', 'D':'R', 'C':'L', 'W':'M', 'G':'F', 'P':'B', 'V':'K',
    'J':'X', 'Q' :'Z','T':'N', 'S':'H' ,'R': 'D', 'L':'C', 'M':'W', 'F':'G'}
while True:
    try:
        result=''
        sentence = list(input())
        for i, x in enumerate(sentence):
            if x in change:
                sentence[i] = change[x]
            result+=sentence[i]
        print(result)
    except EOFError:
        break