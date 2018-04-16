
'''
(A.) 請寫一個程式把裡面的字串反過來。 (B.) 請寫一個程式把裡面的字串,每個單字本身做反轉,但是
單字的順序不變。
f(“junyiacademy”) == “ymedacaiynuj”
f(“flipped class room is important”) == “deppilf ssalc moor si tnatropmi”
'''
#Ans:
print('please input a string')
get_string = input()

print('reverse all:',get_string[::-1])
print('reverse word:',[i[::-1] for i in get_string.split(' ')])

'''
請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的倍數以及 5 的倍數,但是
需要保留同時是 3 和 5 的倍數的總數字數。
舉例.
input:15
所有的數字是:1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
其中 3, 6, 9, 12 被替除; 5, 10 被替除;但是 15 被保留
所以剩下來的數字是 1, 2, 4, 7, 8, 11, 13, 14, 15,因此,
output:9
'''

print('please input a number')
get_n = input()
count=int(get_n)
for i in range(1,count+1):
    if (i%3==0) or (i%5==0):
        count-=1
        if  (i%3==0 and i%5==0):
            count+=1      
print('total:',count)
    
        



