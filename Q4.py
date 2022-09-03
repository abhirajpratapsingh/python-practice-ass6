# Q4 : Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
first_num , second_num = int ( input ( "enter first number :" ) ) , int ( input ( "enter second number :" ) )
print ( ( first_num , 'is greater number') if first_num > second_num else (second_num , 'is greater number') )