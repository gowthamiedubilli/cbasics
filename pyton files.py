

#mail=str(input())
#pw=str(input())
#if mail == 'karthik1234@gmail.com' and pw == 'karku123':
 #   print('logged in')
#else:
 #   print("invalid credentials")
  #   print('try agin')
#a,b=map(int,input().split())
#if a>b:
 #   print(a,'is>',b)
#elif a==b:
 #   print(a,'is=',b)
#else:
 #   print(a,'is<',b)

#n=int(input())
#if n>=80 and n<=100:
 #   print('a grade')
#elif n>=60 and n<80:
 #   print('b grade')
#elif n>=40 and n<60:
 #   print('c grade')
#else:
  #  print('d grade')

   
#for f in range(0,52,2):

 #   print(f,end=' ')
'''
for i in range(4,81,4):
    print(i,end=' ')

'''
'''for i in range(1,6):
    print(i,end=' ')
print()
print('done')'''

'''for i in range(897,1,-43):
    print(i,end=' ')'''

    
'''for i in range(25,36):
    print(i,end=' ')
print()
for i in range(35,24,-1):
    print(i,end=' ')'''


'''a,b=map(int,input().split())

for i in range(a,b+1):
    print(i,end=' ')
print()

for i in range(b,a-1,-1):
    print(i,end=' '

    '''
'''a=int(input())
b=int(input())
if a>b:
    for i in range(a,b+1,1):
        print(i,end=' ')
else:
    for i in range(a,b+1,-1):
        print(i,end=' ')'''


'''   for count=8
count=0
for i in range(6,51,6):
    count+=1
    print(i,end=' ')
print("\n")
print(count)'''


                #while loop
'''
i=6
c=0
while i<51:
    c+=1
    print(i,end=' ')
    i+=6
print()
print(c)

i=0
while i<=10:
     print(i,end=' ')
     i+=2
i=5
while i!=0:
    print(i,end=' ')
    i-=1    '''
'''
# for i in range(1,6):
 #   for i in range(1,6):
 #       print(i,end=' ')
#    print()
n=int(input())
j=1

for i in range(1,n*n+1):
    print(j,end=' ')
    if j==n:
        j=0
        print()
    j+=1

'''
'''
=====================
n=int(input())
j=1
i=1
while i<n*n+1:
    print(j,end=' ')
    if j==n:
        j=0
        print()
    j+=1
    i+=1  
======================= '''
'''
===========================
i,n=map(int,input().split())
for i in range(i,n+1):
    if i%2!=0:
        continue
    print(i,end=' ')
========================= '''
'''
===========================
i,n=map(int,input().split())
for i in range(1,n+1):
    if i%6!=0:
        continue
    print(i,end=' ')
=============================='''
'''
===============================
a,b,c=map(int,input().split())
flag=0
for i in range(a,b+1):
    if i==c:
         flag+=1
if flag==1:
    print(True)
else:
    print(False)
==============================='''
'''
===============================
a,b,c=map(int,input().split())
flag=0
for i in range(a,b+1):
    if i==c:
         print(True)                  less complexity
         break
else:
    print(False)
==============================='''
'''
=================================
a,b,c=map(int,input().split())
i=a
while i<=b or i>=b:
    if i==c:
        print(True)                        for sortex order only
        break
    i+=1
else:
    print(False)
=================================='''
#  ===================patterns==============
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()  '''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print('@',end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(n+1-i,end=' ')
        else:
            print(' ',end=' ')
    print()
'''    
'''
===================================================
                     #Armstrong number

import math
a,b=map(int,input().split())             # ways to find length of a number
sum=0                                #length of the given number by using                              #  int(math.log10(n)+1
#nu=str(n)
#n=len(nu)
for n  in range(a,b+1):               #there is a function to find length 
    temp=n
    le=int(math.log10(n))+1
    while n:                            #by using function called " len"
        r=n%10
        sum+=r**le
        n=n//10
    if sum==temp:
        print(temp)
    sum=0
=========== 1============================== '''

'''
                               # palindrome

a,b=map(int,input().split())
for n in range(a,b+1):
    re=0
    k=n
    while n>0:
        r=n%10
        re=re*10+r
        n=n//10
    if re==k:
        print(k)
    
======================================'''
            #  =========== prime numbers==============

#1st method   with more iterations
'''
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c<=2:
    print(True)
else:
    print(False)
'''


# 2nd method with less iterations then 1st method
'''
n=int(input())
for  i in range(2,n):
    if n%i==0:
        print(False)
        break
else:
    print(True)
'''

#  3rd method for prime numbers with less iterations than 2nd method
'''
n=int(input())
for i in range(2,(n//2)+1):
    if(n%i==0):
        print(False)
else:
    print(True)
'''
# 4th method for prime numbers with less iterations than 3rd method
'''
n=int(input())
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(False)
else:
    print(True)
'''
               #======Mega Prime============
'''
n= int(input())
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print('Not a prime')
        break
else:
    while n>0:
        r=n%10
        n=n//10
        for i in range(2,int(r**0.5)+1):
            if r%i==0:
                print('not mega prime')
                break
        else:
            print('mega prime')
'''

'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 :
            print(n+1-i,end=' ')
        else:
            print(' ',end=' ')
    print()

'''


             #     ==========FUNCTIONS=================
'''
             
def add(a,b):
    return(a+b)


a,b=map(int,input().split())
c=add(a,b)
print(c)

'''
          #PRIME IN FUNCTION
'''
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True


n=int(input())
if prime(n) is True:
    print("prime")
else:
     ("not prime")
'''

# mega prime in function
'''
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

n=int(input())
if prime(n):
    d=0
    pd=0
    while n:
        r=n%10
        n=n//10
        d+=1
        if prime(r):
            pd+=1
    if d==pd:
        print("Mega prime")
    else:
        print(" not mega prime")

else:
    print("not a prime")

'''
    #twisted prime in functions 
'''
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def rev(n):
    re=0
    while n>0:
        r=n%10
        re=re*10+r
        n=n//10
    return re


n=int(input())
if prime(n):
    if prime(rev(n)):
        print("twisted prime")
    else:
        print("not twisted prime")
    
else:
    print('not prime')
'''
   #lcm
'''
def lcm(a,b):
    c=b
    while True:
        if c%a==0 and c%b==0 :
            return c
        c+=1
a,b=map(int,input().split())
print(lcm(a,b))

'''



####count of element using count function
##a=list(map(int,input().split()))
##b=int(input())
##print(a.count(b))

####count of element  without using count function
##a=list(map(int,input().split()))
##b=int(input())
##c=0
##for i in a:
##    if i==b:
##        c+=1
##print(c)


####length of list without using len function
##
##a=list(map(int,input().split()))
##c=0
##for i in a:
##    c+=1
##print(c)


####max element and min  element without using functions
##a=list(map(int,input().split()))
##m=a[0]
##for i in a:
##    if i>m:
##        m=a[i]
##print(m)

##min

##a=list(map(int,input().split()))
##m=a[0]
##for i in a:
##    if i<m:
##        m=a[i]
##print(m)


#### call by reference
##def add(a):
##    a+=[9]
##    return a
##
##print(add([1,2,3]))
##
##


##a='sachin'
##for i in range(len(a)):
##    print(i,a[i])
##
##for i in a:
##    print(i)

##n=input()
##c=0
##for i in n:
##    if ord(i)>=48 and ord(i)<=57:
####  if i in '0123456789':
####    if i.isdigit()
##        c+=1
##print(c)

##n=input()
##b=[]
##c=[]
##for i in range(len(n)):
##    if i%2==0:
##        b.append(n[i])
##    else:
##        c.append(n[i])
##d=(b+c)
##e=''.join(d)
##print(e)
##                              ## or
##a=input()
##print(a[::2]+a[1::2])
   
                        #  dictionary  in loop
##a={1:1,2:2,3:3,4:5}
##for i in a.keys():
##    print(i,a[i])
##        # or
##for i in a.values():
##    print(i)
                        ##or
##for i,j in a.items():
##    print(j,i)

   ##create own dictionary
##a={}
##for i in range(1,6):
##    a[i]=i*i
##print(a)
##
##a={i:i*i for i in range(1,6)}
##print(a)
##    

##a=list(map(int,input().split()))
##d={}
##for i in a:
##    if i not in d.keys():
##        d[i]=1
##    else:
##        d[i]+=1
##print(d)

                                    ## OOPS 

##class car():
##    def __init__(self):#constructor
##        print('hi')
##    def display(self):
##        print('hello')
##a=car() #object
##a.display()
##
##b=car()
##b.display()
##
##            






class car():
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def display(self):
        print(self.name,self.model)
a=car('karthik',21311208) #object
a.display()

b=car('karku',213100405)
b.display()




