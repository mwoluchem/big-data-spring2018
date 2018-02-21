# PSet1
# Maia Woluchem
# February 18, 2018


## A. Lists

list_a = ["Mom", "Maia", "Malaika", "Mariene"]
print(list_a[2])
print(list_a[:2])
list_a.append("last")
list_a
print(len(list_a))
list_a[-1] = "new"
list_a

## B. Strings

sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
sentence = ' '.join(sentence_words)
print(sentence)
sentence_words.reverse()
print(sentence_words)
sentence_words.sort()
sentence_words
sorted(sentence_words)

#The difference between sorted() and .sort() is that sorted() just returns a sorted version of your list, but it doesn't change
#the initial list itself. In comparison, sentence_words.sort() sorts the list in-place, meaning that now "sentence_words" is itself
#a sorted version of its initial version.

## C. Random Function


def randomfunct(x,lowerbound=0):
    return randint(lowerbound,x)
    print(randint(lowerbound,x))

randomfunct(6)
randomfunct(6,6)

assert(0 <= randomfunct(100) <= 100)
assert(50 <= randomfunct(100, lowerbound = 50) <= 100)

## D. String Formatting Function


def string_format(x,y):
    n = x
    title = y.title()
    string = f"The number {x} bestseller today is: {title}"
    print(string)

string_format(1, "my cute book")

## E. Password Validation Function

special_chars = ['!', '?', '@', '#', '$','%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

def passwordtest(pwd):
    if len(pwd)<=7 or len(pwd)>14:
        print("Error: Password is the wrong length")
    elif sum(1 for char in pwd if char.isdigit()) < 2:
        print("Error: Password does not have enough digits")
    elif sum(1 for char in pwd if char.isupper()) < 1:
        print("Error: Password does not have an uppercase letter")
    elif sum(1 for char in pwd if char in special_chars)< 1:
        print("Error: Password does not have a special character")
    else:
        print("Password is a Success!! Great job girl, no one will hack you now!")

passwordtest('sjfiaKs2!!34')

## F. Exponentiation Function

def exp(base,exp):
    root = 1
    for n in range(exp):
        root= root*base
    return root

exp(5,4)

## G. Extra Credit: Min and Max Functions

try_list = [6,3,5,6,4]

def findmin(x):
    starter = 0
    minimum = None
    for item in try_list:
        if item == starter:
            minimum = item
        if item < starter:
            minimum = item
    return minimum
    print(minimum)

def findmin(list):
    minimum = 0
    for i in list:
        if i == minimum:
            minimum = i
        else:
            minimum +=1
    return minimum

findmin(try_list)
