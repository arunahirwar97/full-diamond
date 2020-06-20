a = int(input())

for i in range(a):
    if i < 6:
        print((10-i)*' ' + i*'* ')
    else:
        print((i*' ' + (10 - i)*'* '))
    
