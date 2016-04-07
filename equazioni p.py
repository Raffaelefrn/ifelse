from math import sqrt
a=2
b= 10


if  (a==0) and (b==0):
		print 'non ci sono dati'

else:
	if a==0 or b==0:
		print"Impossibile"
	else:
		b=b*(-1)
		x=b/a
		print"x=",x