# *
# * *
# * * * 
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()
row=4
for k in range(row,0,-1):
    for l in range(k,0,-1):
        print("*",end=" ")
    print()
    
    
    
    
#         *
#       * *
#     * * *  
#   * * * *  
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i+j>=6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(1, rows + 1):
        if i + j >= rows + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()