n = int(input("Enter the number of students in class :\n"))
i = 0
x = 0
L1 = [x,]
while i < n:
    x = int(input("Enter the marks of Student :\n"))
    L1.insert(i,x)
    i = i + 1
L1.pop(n)
print(L1)
i = 0
while i < n:
    if L1[i] < 33:
        print("Student has failed\n")
    else:
        print("Student has passed\n")
    i = i + 1        
# print(i)
# L1 = [13, ]
# x = 0
# n = 1
# while x < 9:
#    L1.insert(x,n)
#    x = x + 1
#    n = n + 1
# print(L1)