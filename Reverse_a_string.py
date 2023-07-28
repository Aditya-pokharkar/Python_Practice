#Python code for reversing a string (without using inbuilt methods)

str1='ABCD'                                               #Define a sample string
print('The original String is = ', str1)
rev=''                                                    #Declareed the reverse string as empty
n=len(str1)-1                                             #calculate the length of given staring -1

while n>=0:
    rev=rev+str1[n]                                       #adding one char to rev string
    n=n-1                                                 #reducing the n value

print('The reversed String is = ', rev)                   #printing the reverse string
