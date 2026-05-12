import random

#list of starters: colors

starter = ['blue', 'red', 'green']

#list of midles: adjective

middler  = ['crazy','happy', 'sad']

#list of finals: animals

ender = ['dragon', 'ox', 'spren']


print(random.randint(0,len(starter)+1))


def random_from_list(lis):
    i=random.randint(0,len(lis)-1)
    res=lis[i]
    return (res)
    
def gen():

    start=random_from_list(starter)
    middle=random_from_list(middler)
    end=random_from_list(ender)
    
    complete=start+'_'+middle+'_'+end
    return (complete)
    

    
    

