import numpy as np
from random import random as r
from random import randint as ri


trSet=[]
for i in range(0,1000000):
	trSet.append(ri(1,10))

Y=[]
for i in trSet:
	if i>0 and i<=5:
		Y.append(0)
	else:
		Y.append(1)


def sig(x,diff=False):
	if diff:
		 return np.exp(-x)/((1+np.exp(-x))*(1+np.exp(-x)))
	else:
		return 1/(1+np.exp(-x))


def getAV(inp,wb):
	z1=inp*float(wb[0])+float(wb[3])
	a1=sig(z1)
	z2=a1*float(wb[1])+float(wb[4])
	a2=sig(z2)
	z3=a2*float(wb[2])+float(wb[5])
	a3=sig(z3)
	return [[z1,z2,z3],[a1,a2,a3]]


WB=np.matrix([r(),r(),r(),r(),r(),r()]).T
learningRate=0.008

for (i,j) in zip(trSet,Y):
	a=getAV(i*0.05,WB)
	C=(j-a[1][2])*(j-a[1][2])
	print C
	CW1=-2*(j-a[1][2])*sig(a[0][2],True)*float(WB[2])*sig(a[0][1],True)*float(WB[1])*sig(a[0][0],True)*i
	CW2=-2*(j-a[1][2])*sig(a[0][2],True)*float(WB[2])*sig(a[0][1],True)*a[1][0]
	CW3=-2*(j-a[1][2])*sig(a[0][2],True)*a[1][1]
	CB1=-2*(j-a[1][2])*sig(a[0][2],True)*float(WB[2])*sig(a[0][1],True)*float(WB[1])*sig(a[0][0],True)
	CB2=-2*(j-a[1][2])*sig(a[0][2],True)*float(WB[2])*sig(a[0][1],True)
	CB3=-2*(j-a[1][2])*sig(a[0][2],True)
	gradC=np.matrix([CW1,CW2,CW3,CB1,CB2,CB3]).T
	WB = WB - learningRate*gradC

f=open("data.txt",'a')
f.write("\n----------------------------------------------------------------\n")
f.write("C: "+str(C)+"\n"+"gradC: "+str(gradC)+"\n"+"WB: "+str(WB)+"\n")
f.close()
