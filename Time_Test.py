import timeit
setup = '''
List = []
X = lambda a,b: a+b
for x in range(1,100):
    List.append(X(x,x))
'''
setup2 = '''
X = lambda a,b: a+b
List2 = map(X,range(1,100),range(1,100))
'''

print(timeit.timeit(setup,number=10000))
print(timeit.timeit(setup2,number=10000))