-##def add(a,b):
##    return(a+b)
##def sub(a,b):
##    return(a-b)
##def mult(a,b):
##    return(a*b)
##def div(a,b):
##    return(a//b)
                       ##prime function  '''
##def prime(n):
##    for i in range(2,int(n**0.5)+1):
##        if n%i==0:
##            return False
##    else:
##        return True

                           ##'''lcm function '''

##def lcm(a,b):
##    c=b
##    while True:
##        if c%a==0 and c%b==0 :
##            return c
##        c+=1

                           
                      ##'''gcd in function'''




                     #''' decimal to binary'''
##def decbin(n):
##    s=' '
##    while n>0:
##        r=n%2
##        s+=str(r)
##        n=n//2
##    return s[::-1]
##n=int(input())
##print(decbin(n))
##

                   ##factorial using iterations in function
##def factorial(n):
##    r=1
##    for i in range(1,n+1):
##        r*=i
##    return r
##n=int(input())
##print(factorial(n))


                     ## factorial using recursion in function
##def fact(n):
##    if n==1:
##        return 1
##    return n*fact(n-1)
##n=int(input())
##print(fact(n))


                         ## fibinacci series
##def fib(n):
##    a,b=0,1
##    print(a,b,end=' ')                    
##    for i in range(2,n+1):
##        c=a+b
##        print(c,end=' ')
##        a=b
##        b=c
##n=int(input())
##fib(n)

    

##def fib(n):
##    a,b=0,1
##    #print(a,b,end=' ')                    
##    for i in range(2,n+1):
##        c=a+b
##        a=b
##        b=c
##        if b>m:
##            print(a)
##            break
##n=int(input())
##m=int(input())
##fib(n)










