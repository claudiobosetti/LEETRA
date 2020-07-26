from leetDict import letters
from termcolor import colored

def displayBanner():
    banner = open('../graphics/banner.txt', 'r')
    print(colored(banner.read(), 'green', attrs=['bold']))

displayBanner()

stringInput = input("To Convert in 1337:")

def translate(stringInput, letters, before=None):
    
    if not stringInput: return stringInput
    before = before or str.lower
    t = before(stringInput)
    for key, value in letters.items():
        t = t.replace(key, value)
    print("1337 translation:", t)

translate (stringInput, letters)
