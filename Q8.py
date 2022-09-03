# Q8 : Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
from tkinter import E


print ( 'enter the value of a,b,c of a quardratic equation :' )
a , b , c = int ( input ( 'coefficient of x^2 :' ) ) , int ( input ( 'coefficient of x :' ) ) , int ( input ( 'enter constent :' ) )
D = b ** 2 - 4 * a * c
if D > 0 : print ( 'Real and Distinct roots' )
elif D == 0 : print ( 'Real and Equal roots' )
else : print ( 'Imaginary roots' )