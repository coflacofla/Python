'''
apart = [[101,102],[201,202],[301,302]]

for i in apart:
 for j in i:
     print("{}호".format(j))

for row in apart[::-1]:
    for col in row[::-1]:
        print(col,"호")
'''

###실습###

print("1")
for i in range(8):
    b = '*'*i
    print(b)

print("2")
for i in range(7,0,-1):
    b = '*'*i
    print(b)

print("3")
width = 7
for i in range(1,8):
    b = '*'*i
    result = b.rjust(width)
    print(result)

print("4")
width = 15
for i in range(1,14,2):
    b = '*'*i
    result = b.center(width)
    print(result)

print("5")
width = 7
for i in range(1,8,2):
    b = '*'*i
    result = b.center(width)
    print(result)
for j in range(5,-1,-2):
    c = '*'*j
    result = c.center(width)
    print(result)




