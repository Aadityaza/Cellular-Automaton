# defining position
class pos:
    x=None
    y=None
    def __init__ (self, x,y):
        self.x=x
        self.y=y
    #neighbours
    def top(self):
        return self.x-1,self.y
    def right(self):
        return self.x-1,self.y+1
    def left(self):
        return self.x-1,self.y-1 
       
# define cellular automation rule
def rule_30(i,j,matrix):
 # Get matrix shape and compute the position of the cell at (i, j)
    position=pos(i,j)
    n,m=matrix.shape
# Get the values of the cells to the left, top, and right of the cell at (i, j)
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
# define cellular automation rule   
def my_rule(i,j,matrix):
    position=pos(i,j)

    n,m=matrix.shape
    left= matrix[position.left()[0]%m][position.left()[1]%m]
    top= matrix[position.top()[0]%m][position.top()[1]%m]
    right=matrix[position.right()[0]%m][position.right()[1]%m]
    return ((top-left-right ))%2

#Reading Number of Itirations
n= int(input('Enter the no of ittirations: '))
print(str(n)+" ittirations to run...")

#defining shape of output matrix    
s=(n,n+2*(n-1))

# Creating m*n (s) Marix 
import numpy as np
matrix=np.zeros(s)

# Setting up middle value of 1st row to zero
n,m=matrix.shape
matrix[0,int((m-1)/2)]=1

# Applying rule to each element of matrix
for i in range(1,n):
    for j in range(m):
        matrix[i,j]=rule_30(i,j,matrix)

print(matrix)

# display the image
import matplotlib.pyplot as plt

plt.imshow(matrix, cmap="binary")

# Turn off the axis labels
plt.axis("off")

# Show the plot
plt.show()
