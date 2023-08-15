A = {x for x in range(21)}
print(A)
B = {x for x in range(21) if x % 2 == 0}
C = A - B
print(C)
