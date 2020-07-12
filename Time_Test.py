import timeit
setup = '''
List = []
funcionName = lambda a,b: a+b
for x in range(1,100):
    List.append(funcionName(x,x))
'''
setup2 = '''
funcionName = lambda a,b: a+b
List2 = map(funcionName,range(1,100),range(1,100)) 
'''

print(timeit.timeit(setup,number=10000))
print(timeit.timeit(setup2,number=10000))