# defining locations
class pos:
    x=None
    y=None
    def __init__ (self, x,y):
        print("applying rule to pos " +str(x)+", "+str(y))
        self.x=x
        self.y=y

    def top(self):
        self.x+=1
        return self.x,self.y  
    def right(self):
        self.x+=1
        self.y+=1
        return self.x,self.y    
    def left(self):
        self.x+=1
        self.y-=1
        return self.x,self.y    
    
        
    
# define cellular automation rule
def rule(i,j):
    matrix=pos(i,j)
    #rule for 0
    if matrix.left()==1 and matrix.top()==1 and matrix.right()==1:
        return 0
    if matrix.left()==1 and matrix.top()==1 and matrix.right()==0:
        return 0
    if matrix.left()==1 and matrix.top()==0 and matrix.right()==1:
        return 0
    if matrix.left()==0 and matrix.top()==0 and matrix.right()==0:
        return 0
    # rule for 1
    if matrix.left()==1 and matrix.top()==0 and matrix.right()==0:
        return 1
    if matrix.left()==0 and matrix.top()==1 and matrix.right()==1:
        return 1
    if matrix.left()==0 and matrix.top()==0 and matrix.right()==1:
        return 1
    if matrix.left()==0 and matrix.top()==1 and matrix.right()==0:
        return 1
    

#taking no if ittirations
while True:
    n= int(input('Enter the no of ittirations: '))
    print(str(n)+" ittirations to run...")
    if n%2==1:
        break
    else:
        print("Please choose an odd no.")
s=(n,(2**(n-1))+n-1)

# make m*n marix to diplay
import numpy as np
matrix=np.zeros(s)

# run rule in matrix (start = middle of the row )
n,m=matrix.shape
for i in range(m)
matrix[0,int(m/2)]=1
for i in range(1,n):
    for j in range(m):
        #if i==0 and j< int(m/2):
        matrix[i,j]=rule(i,j)

print(matrix)

# display the image
from matplotlib import pyplot as plt
plt.imshow(matrix,interpolation='nearest')
plt.show()


