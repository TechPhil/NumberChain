import time
import inflect
p = inflect.engine()

def getnumber1():
    global number
    global chain
    chain = 0
    number = 0
    print("Enter a number please")
    number=input()
    n2w()

def n2w():
    global number
    global word
    global p
    word=p.number_to_words(number)
##    print(word)
    lengthtonum()

def lengthtonum():
    global chain
    global word
    global number
    number = len(word)
    print(number)
    chain+=1
    time.sleep(0.1)
    fourcheck()
    n2w()

def fourcheck():
    global number
    if number==4:
        print("You have reached the end of your chain!")
        print("You chain contained "+str(chain)+" numbers!")
        getnumber1()
    else:
        return
getnumber1()
