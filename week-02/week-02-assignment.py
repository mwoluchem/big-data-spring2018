# PSet1
# Maia Woluchem
# February 18, 2018


## A. Lists

"""1. Create a list containing any 4 strings.
2. Print the 3rd item in the list - remember how Python indexes lists!
3. Print the 1st and 2nd item in the list using [:] index slicing.
4. Add a new string with text “last” to the end of the list and print the list.
5. Get the list length and print it.
6. Replace the last item in the list with the string “new” and print"""

list_a = ["Mom", "Maia", "Malaika", "Mariene"]
print(list_a[2])
print(list_a[:2])
list_a.append("last")
list_a
print(len(list_a))
list_a[-1] = "new"
list_a

## B. Strings

Given the following list of words stored as strings, complete the following tasks:

"""1. Convert the list into a normal sentence with [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join), then print.
2. Reverse the order of this list using the `.reverse()` method, then print. Your output should begin with `[“them”, ”visualize”, … ]`.
3. Now user the [`.sort()` method](https://docs.python.org/3.3/howto/sorting.html) to sort the list using the default sort order.
4. Perform the same operation using the [`sorted()` function](https://docs.python.org/3.3/howto/sorting.html). Provide a brief description of how the `sorted()` function differs from the `.sort()` method.
5. Extra Credit: Modify the sort to do a case [case-insensitive alphabetical sort](http://matthiaseisen.com/pp/patterns/p0005/).
"""

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

Create a function called `exp` that accepts two integers and then `return`s an exponentiation, **without using the exponentiation operator** (`**`). You may assume these are positive integers. Use at least one custom-defined function.

For example, some outputs of this function could be:

```python
exp(2, 3) # output: 8
exp(5, 4) # output: 625
```

+ Inputs
  1. An `integer` that will be recursively multiplied
  2. An `integer` that will define the number of times to multiply the number to get the exponentiation.
+ Outputs
  1. An `integer` that is the result of the exponentiation.

Hint: You can recursively multiply a number. The second function parameter defines the number of times the recursive loop happens. Every time the loop happens, you can redefine the variable that gets multiplied.

## G. Extra Credit: Min and Max Functions

Write your own versions of the Python built-in functions `min()` and `max()`. They should take a list as an argument and return the minimum or maximum element. Assume lists contain numeric items only.

+ Inputs:
  1. A `list` of `numbers` to be tested.
+ Outputs:
  1. A `number` of the list that is the maximum or minimum.

Hint: Pick the first element as the minimum/maximum and then loop through the elements. Each time you find a smaller/larger element, update your minimum/maximum.
