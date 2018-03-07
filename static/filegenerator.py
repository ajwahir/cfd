from random import *
yVal = 100; 
x = 1; 
while(1):
	f= open("dps.txt","w");
	yVal = randint(50,110);
	if(x==1):
		yVal = yVal+1000;
		x = 2
	else:
		yVal = yVal+2000;
		x = 1	
	f.write("%d\n"%(yVal))
	f.close()