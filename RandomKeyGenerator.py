import datetime
from random import shuffle

def shuffleAnything (num):
  # In case a number is passed converting it to string.
  num=str(num)
  lc1=[x for x in range (len (num))]
  shuffle (lc1)
  temp=""
  for idx1 in range (len (num)):
    temp+=num[lc1[idx1]]
  return temp

def generateMeARandomNumber ():
  datetimeNow=datetime.datetime.now()
  list1=[shuffleAnything(str(datetimeNow.year)),shuffleAnything("0"+str(datetimeNow.month) if datetimeNow.month<10 else str(datetimeNow.month)),shuffleAnything("0"+str(datetimeNow.day) if datetimeNow.day<10 else datetimeNow.day),shuffleAnything(str(datetimeNow.second)),shuffleAnything(str(datetimeNow.microsecond))]
  x = [i for i in range(len(list1))]
  shuffle (x)
  finalVar=""
  for idx in range (len(x)):
    finalVar+=list1[x[idx]]
  shuffleAnything(finalVar)
  return finalVar
  
print ("trail 1: "+generateMeARandomNumber())
print ("trail 2: "+generateMeARandomNumber())
print ("trail 3: "+generateMeARandomNumber())
