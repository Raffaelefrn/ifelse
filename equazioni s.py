from math import sqrt
a=1
b= -5
c=6


if  (a==0) and (c==0):
	if (b==0):
		print 'non ci sono dati'
else:
	if (a==0):
		print "L'eq.  non e' di secondo grado"
		b*(-1)
		x=b/a
		print"x= ",x
	if(b==0):
		print "L'eq. e' pura"
		c*(-1)
		x1=c/a
		x2=sqrt(x1)
		if x2<0:
			print"impossibile"
		else:
			print"x1/2:+o-  ",x2
		
	if(c==0):
		print"L'eq. e' spuria"
		b*(-1)
		x2=b/a
		print"x1=0 e x2=",x2
	
	if a!=0 and b!=0 and c!=0:
		print"L'eq. e' completa"
		print '(ax*x)+bx+c=0'
		delta=(b*b)-4*a*c
		print 'Delta: ',delta
		if (delta<0):
			print'Impossibile, delta negativo'
		else:
			x1=((b*(-1))+ sqrt(delta))/(2*a)
			x2=((b*(-1))- sqrt(delta))/(2*a)
			print'x1: ',x1,'x2: ',x2