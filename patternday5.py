# *       *
#   *   *
#     *
#   *   *
# *       *
  
rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==j or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
# * * * * *
#     *
#     *
#     *
# * * * * *

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i==rows or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# *       *
# *       *
# * * * * *
# *       *
# *       *

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j==1 or j==rows or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
# * * * * *
# *
# * * * * *
#         *
# * * * * *

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i==3 or i==rows or i+j==3 or i+j==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    

