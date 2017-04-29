def reverse (text):
    revText="";
    for x in range(len(text), 0, -1):
        revText+=text[x-1]
    return revText
