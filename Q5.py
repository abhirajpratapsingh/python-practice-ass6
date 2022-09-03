# Q5 : Write a python script to print two given words in dictionary order
print ( "enter two strings :" )
string1 , string2 = input ( ) , input ( )
print ( (string2 , string1) if string1 > string2 else (string1 , string2) )