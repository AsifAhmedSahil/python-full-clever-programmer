'''
word frequency : ('I love batman because i am a batman')
{'I': 2 , 'love':1}
'''

from unittest import result


def word_frequency(phrase):
    result = {}

    words = phrase.split()

    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result

# print(word_frequency('I am a bat boy because I love batman'))

print(word_frequency(input('please enter your phrase...')))