f = open("some.py")
c = 0
for l in f:
    print(l, end="")
    if c == 2:
        break
    c += 1
f.close()


%%time
f = open('some.py')
flines = ''
for i in range(3):
    lines += f.readline()
