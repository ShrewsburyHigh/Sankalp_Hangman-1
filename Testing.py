import random
randomWords = ["ducks" , "jumbo" ,"lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
#print secret 
def initialize(): 
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = raw_input()     
def ifWon():
    if secret == updateWord: 
        print "you win"
    else:
        getLetter()
def test(Letter):
    global updatedWord
    global letter
    global Secret
    if Letter in Secret:
        updatedWord.append(Letter)
        ifwon()
def main():
    initialize ()
    getLetter()
    ifWon()
main()