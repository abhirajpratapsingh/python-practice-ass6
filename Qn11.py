# Q 11 : Write a python script to take the month value in numeric format and display the number of days in it.
take_month = int ( input ( "enter the month btw 1 - 12 :" ) )
if take_month in ( 1 , 3 , 5 , 7 , 8 , 10 , 12 ) : print ( "{}'s month has 31 days" . format ( take_month ) )
elif take_month == 2 : print ( "{}'s month has 28 or 29 days" . format ( take_month ) )
else : print ( "{}'s month has 30 days" . format ( take_month ) )