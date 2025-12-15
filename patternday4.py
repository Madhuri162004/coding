# * * * * *
# *       *
# *   *   *
# *       *
# * * * * *

rows=5
for i in range(rows):
    for j in range(rows):
        if i==0 or i==rows-1 or j==0 or j==rows-1 or i==j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
#     *  
#    * *
#   * * *
#  * * * *
# * * * * *

rows=5
for i in range(1,rows+1):
    for sp in range(rows-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
    
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

rows=5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+2-i):
        print(rows-i+1,end=" ")
    print()
    
    
    
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

rows=5
for i in range(rows,0,-1):
    for sp in range(rows-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
    
    
    
# * * * * *
# *
# *
# * * * * *
# *
# *
# * * * * *

rows=7
for i in range(rows):
    for j in range(5):
        if i==0 or i==6 or i==3 or j==0:
            print("*",end=" ")
    print()
    
    
 