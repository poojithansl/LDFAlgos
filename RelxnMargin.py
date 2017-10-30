from matplotlib import pyplot as plt
import random
def jerin(ap,yp,p):
	h=[]
	for i in yp:
		g=sum(map((lambda x,y:x*y),ap,i))			#RelaxationAlgmargin
		if g<=p:
			h.append(i)
	return h
#a=[random.randint(-3,3)]*3
a=[3,4,5]
y=[[1,2,7],[1,8,1],[1,7,5],[1,6,3],[1,7,8],[1,5,9],[1,4,5],
[-1,-4,-2],[-1,1,1],[-1,-1,-3],[-1,-3,2],[-1,-5,-3.25],[-1,-2,-4],[-1,-7,-1]]
k=0
eta=0.1
b=input("input b")
#print jerin(a,y,b)
while len(jerin(a,y,0)):
	#print "1"
	t=jerin(a,y,b)
	#print t
	#k = randint(0,len(y)-1)

	if y[k] in t:
		#eta=eta/k
		normsq=sum(map((lambda x:pow(x,2)),y[k]))
		tk=b-sum(map((lambda x,y:x*y),a,y[k]))
		jk=tk*tk
		meta=(eta*jk)/float(normsq)
		gh=map(lambda gk:gk*meta,y[k])
		new_a=map((lambda x,gk:x+gk),a,gh)
		a=new_a
	k=(k+1)%14
	#i = randint(0,len(y)-1)

x1=[]
x2=[]
y1=[]
y2=[]
for t in y:
    if t[0]==1:
        x1.append(t[1])
        y1.append(t[2])
    if t[0]==-1:
        x2.append(t[1])
        y2.append(t[2])
plt.scatter(x1,y1,color='blue')
plt.scatter(x2,y2,color='red')
print a
p1_x=-8
p1_y=-a[1]/a[2]*p1_x*1.0-(a[0]/a[2])*1.0
p2_x=12
p2_y=-a[1]/a[2]*p2_x*1.0-(a[0]/a[2])*1.0
plt.plot([p1_x,p2_x],[p1_y,p2_y],'k-')

plt.show()

	
