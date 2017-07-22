from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            line_words=line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):              
    for word in story_words:
        print(word)
        
def main():
    words=fetch_words()
    print_words(words)
        
if __name__=='__main__':
    main()
    
    
'''
$ python3
>>>from main_function_creation import (fetch_words,print_words)
>>>print_words(fetch_words)
>>>.
>>>.
>>>.
>>>.
>>>from main_function_creation import *
>>># this imports everything. Not recommended.
>>>fetch_words()
>>>.
>>>.
>>>.
>>>.
>>>print_words(['some','words'])
>>>some
>>>words'
>>>print_words('Any iterator')
>>>A
>>>n
>>>y
>>>
>>>i
>>>t
>>>e
>>>r
>>>a
>>>t
>>>o
>>>r
'''
