
# -*- coding: utf -*-

'''
@author: nir
'''

def hello_world():
    return "hello world!"

def hello_you():
    name = raw_input("What is your name?")
    print ("Hello {}".format(name))

def pub_song():
    for i in range(99, 1, -1):                   
        print("{} bottels of beer on the wall".format(i))
              
#pub_song()
#hello_world()
#hello_you()   



def gematria_value():
    letter = raw_input("Hebrew Letter")
    if (letter == u'א'):
        print ("1")
    else:
        print ("זה לא א")

gematria_value()
