#path:/usr/scripts/pyScripts/using_main.py

from urllib.request import urlopen

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            line_words=line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
                
    for word in story_words:
        print(word)
        
if __name__=='__main__':
    fetch_words()
    
# __name__ is the name of the file.
'''
$ cd /usr/scripts/pyScripts
$ python using_main.py
# since __name__=using_main
# it executes.
$ python
>> import words
'''
