#! /bin/python3.7
#test whether two proportions are equal
import math
print ("Test the difference between nobs1/n1 and nobs2/n2.")
choice='yes'
while choice.upper()=='YES' or choice.upper() == "Y":

	nobs1=int(input("Enter nobs1:"))
	n1= int(input("Enter n1:"))
	nobs2=int(input("Enter nobs2:"))
	n2= int(input("Enter n2:"))
	if nobs1 <= n1 and nobs2 <= n2:

		p1=nobs1*1.0/n1
		p2=nobs2*1.0/n2
		p=(nobs1+nobs2)*1.0/(n1+n2)
		print (p)
		s=math.sqrt(p*(1-p)*(1.0/n1+1.0/n2))
		print (s)
		if nobs1>30 and n1-nobs1>30 and nobs2>30 and n2-nobs2>30:
			z=(p1-p2)/s
			cdf=(1.0 + math.erf(z / math.sqrt(2.0))) / 2.0
			if p1>p2: #if z is positive
				cdf=1-cdf
		else:
			z=(abs(p1-p2))/s
			print (z)
			cdf=(1.0 + math.erf(z / math.sqrt(2.0))) / 2.0
			cdf=1-cdf #z is always positive
			print (cdf)
	
		cdf=cdf*2 #two tail test
		print ("Z=%.3f,p-value(two-tail)=%f" %(z,cdf))
	else:
		print ("This is invalid input try again")
	choice=input("Continue? choice.startswith(y/n)")