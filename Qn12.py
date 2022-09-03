# Q 12 :  Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part

take_complexnum = complex ( input ( 'enter the complex number :' ) )
print ( '{} is greater number'.format ( take_complexnum.real ) if take_complexnum.real > take_complexnum.imag else '{} is the greater number'.format ( take_complexnum.imag ) )