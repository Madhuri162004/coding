# a      
# b c    
# d   f
# g     j 
# k l m n o
rows=5
c=97
for i in range(rows):
    for j in range(i+1):
        if i==j or j==0 or i==rows-1:
            print(chr(c),end=" ")
            c+=1
        else:
            print(" ",end=" ")
            c+=1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
c=97
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(c),end=" ")
        c+=1
    print()
    
    
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
rows=5
for i in range(rows):
    for j in range(rows):
        if i==0 or j==0 or j==rows-1 or i==rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
        
# x 0 x 0 x
# 0 x 0 x 0
# x 0 x 0 x
# 0 x 0 x 0
# x 0 x 0 x

rows=5
for i in range(rows):
    for j in range(rows):
        if i==0 or i==2 or i==rows-1:
            if j==0 or j==2 or j==rows-1:
                print("x",end=" ")
            else:
                print("0",end=" ")
        if i==1 or i==rows-2 :
            if j==0 or j==2 or j==rows-1:
                print("0",end=" ")
            else:
                print("x",end=" ")
    print()
