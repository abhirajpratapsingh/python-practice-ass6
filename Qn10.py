# Q 10 : Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print ( 'enter only three digit numbers :' )
first_num , second_num , third_num = int ( input ( "enter first number :" ) ) , int ( input ( "enter second number :" ) ) , int ( input ( "enter third number :" ) )
if first_num > second_num :
    if first_num > third_num : print ( first_num , 'is the greater number ' )
    else : print ( third_num , 'is the greater numger' )
elif second_num > third_num :
    if second_num > first_num : print ( second_num , 'is the greater number' )
    else : print ( third_num , 'is the greater number' )