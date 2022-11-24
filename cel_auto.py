# defining locations
class pos:
    x=None
    y=None
    def __init__ (self, x,y):
        print("applying rule to pos " +str(x)+", "+str(y))
        self.x=x
        self.y=y

    def top(self):
        return self.x-1,self.y
    def right(self):
        return self.x-1,self.y+1
    def left(self):
        return self.x-1,self.y-1 
    
        
    
# define cellular automation rule
def rule(i,j,matrix):
    position=pos(i,j)

    n,m=matrix.shape
    left= matrix[position.left()[0]%m][position.left()[1]%m]
    top= matrix[position.top()[0]%m][position.top()[1]%m]
    right=matrix[position.right()[0]%m][position.right()[1]%m]

    #rule for 0
    if left==1 and top==1 and right==1:
        return 0
    if left==1 and top==1 and right==0:
        return 0
    if left==1 and top==0 and right==1:
        return 0
    if left==0 and top==0 and right==0:
        return 0
    # rule for 1
    if left==1 and top==0 and right==0:
        return 1
    if left==0 and top==1 and right==1:
        return 1
    if left==0 and top==0 and right==1:
        return 1
    if left==0 and top==1 and right==0:
        return 1
    

#taking no if ittirations
n= int(input('Enter the no of ittirations: '))
print(str(n)+" ittirations to run...")

#defining shape    
s=(n,(2**(n-1))+n)

# make m*n (s) marix to 
import numpy as np
matrix=np.zeros(s)

# run rule in matrix (start = middle of the row )
n,m=matrix.shape
matrix[0,int((m-1)/2)]=1

for i in range(1,n):
    for j in range(m):
        matrix[i,j]=rule(i,j,matrix)

print(matrix)

# display the image
from matplotlib import pyplot as plt
plt.imshow(matrix,interpolation='nearest')
plt.show()