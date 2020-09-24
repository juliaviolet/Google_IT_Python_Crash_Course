def count_letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

# The key is a letter and the value is how many times that letter is present.

count_letters("aaaaa")
{'a': 5}
count_letters("tenant")
{'t': 2, 'e':1, 'n':2, 'a':1}
count_letters("a long string with a lot of letters")
{'a':2, ' ':7, 'l':3, 'o':3, 'n':2, 'g':2, 's':2, 't':5, 'r':2, 'i':2, 'w':2, 'h':1, 'f':1, 'e':2}
