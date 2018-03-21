
'''=====Q1====='''


print('please input a string')
get_string = input()

print('reverse all:',get_string[::-1])
print('reverse word:',[i[::-1] for i in get_string.split(' ')])

'''=====Q2====='''

print('please input a number')
get_n = input()
count=int(get_n)
for i in range(1,count+1):
    if (i%3==0) or (i%5==0):
        count-=1
        if  (i%3==0 and i%5==0):
            count+=1      
    print('total:',count)
    
        



