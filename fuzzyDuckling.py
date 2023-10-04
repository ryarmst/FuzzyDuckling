#mymodule.py
GLOBAL_CHARS = []

GLOBAL_CURSOR = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'UPARROW', 'DOWNARROW', 'LEFTARROW', 'RIGHTARROW', 'PAGEUP', 'PAGEDOWN', 'HOME', 'END', 'INSERT', 'DELETE', 'DEL', 'BACKSPACE', 'TAB', 'SPACE']

GLOBAL_SYSTEM = ['ENTER', 'ESCAPE', 'PAUSE BREAK', 'PRINTSCREEN', 'MENU APP', 'F1', 'F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']

GLOBAL_MODIFIERS = ['SHIFT', 'ALT', 'CTRL', 'GUI', 'CTRL SHIFT', 'ALT SHIFT', 'CTRL ALT', 'CTRL GUI', 'CTRL ALT GUI', 'CTRL SHIFT GUI', 'CTRL ALT SHIFT GUI', 'SHIFT GUI', 'ALT GUI', 'ALT CTRL', 'GUI SHIFT','ALT CTRL GUI', 'ALT CTRL SHIFT', 'ALT GUI SHIFT', 'CTRL GUI SHIFT', 'ALT CTRL GUI SHIFT']
GLOBAL_DELAY = '50' # in ms

## Excluding COMMAND
## Keyboard Fn key? Use 'xev' tool to identify actual key use

def gen_chars():
    ascii_chars = [chr(i) for i in range(128)]
    global GLOBAL_CHARS
    GLOBAL_CHARS = ascii_chars[33:127]
	
	
def combine(prefix, suffix):
    list = []
    for i in prefix:
        for j in suffix:
            list.append(i + ' ' + j)
    return list
            
def ducky(list):
    with open('fuzzyDuckling.txt', 'w') as f:
        for i in list:
            f.write(i)
            f.write('\n')
            f.write('DELAY ' + GLOBAL_DELAY)
            f.write('\n')

 
## Script start
gen_chars()

print(GLOBAL_CHARS)


final_list = combine(GLOBAL_MODIFIERS, GLOBAL_CHARS + GLOBAL_CURSOR + GLOBAL_SYSTEM)


ducky(final_list)

	








