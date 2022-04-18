# # """  Arithmetic Operators"""
# a=float(input("Enter the values of a:"))              #10
# b=float(input("Enter the values of b:"))              #5
# a,b=[int(x) for x in input('Enter the value of a and b: ').split()]    #10 5
# print(f"The value of {a} + {b} is {a+b}")                               #15
# print(f"The value of {a} - {b} is {a-b}")                               #5
# print(f"The value of {a} * {b} is {a*b}")                               #50
# print(f"The value of {a} / {b} is {a/b}")                               #2.0
# print(f"The value of {a} % {b} is {a%b}")                               #0
# print(f"The value of {a} ** {b} is {a**b}")                              #100000

# """  Floor Division """
# c=4//2
# print(c)                              #2
# d=4//2.0
# print(d)                             #2.0
# e=5//2
# print(e)                             #2
# f=5.0//2
# print(f)                            #2.0

"""  Assignment Operator  """
# a=2 ; b=3
# a=a+b
# print(a)             #5
# a=a+a
# print(a)             #10

# a=5
# a+=3
# print(a)              #8
# a-=2
# print(a)              #6
# a*=4
# print(a)              #24
# a/=2
# print(a)              #12.0
# a**=2
# print(a)             #144.0

# p=int(input("Enter the value of a:"))                              #4
# print(f"The value of p is {p}")                                    #4
# p+=2
# print("The value of p after p+=2 is {}".format(p))                 #6
# p-=4
# print("The value of p after p-=4 is {}".format(p))                  #2
# p*=6
# print("The value of p after p*=6 is {}".format(p))                 #12
# p**=2
# print("The value of p after p**2 is {}".format(p))                #144.0
# p/=2
# print("The value of p after p/=2 is {}".format(p))                #72.0

# """ Relational/Comparision Operators """
# a=int(input("Enter the value of a:"))         #2
# b=int(input("Enter the value of b:"))         #3
# print(f"The value of {a} < {b} is {a<b}")     #True
# print(f"The value of {a} >{b} is {a>b}")      #False
# print(f"The value of {a} <= {b} is {a<=b}")    #True
# print(f"The value of {a} >= {b} is {a>=b}")    #False
# print(f"The value of {a} == {b} is {a==b}")    #False
# print(f"The value of {a} != {b} is {a!=b}")    #True

# a=int(input("Enter the value of a:"))                                                       #2
# b=int(input("Enter the value of b:"))                                                       #3
# print("The value of %d<%d=%d"%(a,b,a<b))                                                 #The value of 2<3=1
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a<b))                                   #The value of a=2 , b=3 and a<b=1
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a>b))                                   #The value of a=2 , b=3 and a<b=0
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a<=b))                                  #The value of a=2 , b=3 and a<b=1
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a>=b))                                  #The value of a=2 , b=3 and a<b=0
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a==b)                                   #The value of a=2 , b=3 and a<b=0
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a!=b))                                  #The value of a=2 , b=3 and a<b=1

# """ Logical Operator """
# a=int(input("Enter the value of a:"))                                 #4
# b=int(input("Enter the value of b:"))                                 #5
# print("The value of a<b and b>a is {}".format(a<b and b>a))           #True
# print("The value of a>b and b<a is {}".format(a>b and b<a))           #False
# print("The value of a!=b and b==a is {}".format(a!=b and b==a))       #False
# print("The value of a==b and b!=a is {}".format(a==b and b!=a))       #False
# print("The opposite of {}=={} is {}".format(a,b,not a==b))            #True
# print("The opposite of {}=={} is {}".format(a,b,not a!=b))            #False

# # """   Bitwise Operators    """
# a=int(input("Enter the value of a:"))                        #5
# b=int(input("Enter the value of b:"))                        #8
# c=int(input("Enter the value of c:"))                        #-7
# print("The value of {} & {} is {}".format(a,b,a&b))          #0
# print("The value of {} | {} is {}".format(a,b,a|b))          #13
# """  Note: The formula for negotion (~) is -(value+1)  """
# print("The value of ~{} is {}".format(a,~a))                 #-6
# print("The value of ~{} is {}".format(c,~c))                 #6

# """   Identity Operator  """
a=20
b=20
# if(a is b):
#     print("a and b have same identity")
# else:
#     print("a and b do not have same identity")
    #a and b have same identity

# print(id(a))
# print(id(b))
# if(id(a)==id(b)):
#     print("a and b have same identity")
# else:
#     print("a and b do not have same identity")
   # a and b  have same identity


# x=5
# print(type(x) is int)           #True
# print(type(x) is  not float)    #True
# print(type(x) is float)         #False
# y=4.5
# print(type(y) is int)            #False
# print(type(y) is not float)      #False
# print(type(y) is float)          #True

# """  Membership Operator  """
# name=['venkat','kaveri','vamsy','indu','priya','ajay','durga','viswa','himaja','bhavani',
    #    'ram','darshi','cherry','pinky']
# print('venkat' in name)                     #True
# print('viswa' in name)                      #True
# print('vamsy' in name)                      #True
# print('priya' in name)                      #True
# print('prassu' in name)                     #False
# print('darshi' in name)                     #True
# print('anu'not in name)                     #True
# print('ravi' not in name)                   #True
# print('bhavani'not in name)                 #False
# name.sort()
# print(name)    #['ajay', 'bhavani', 'cherry', 'darshi', 'durga', 'himaja', 'indu', 'kaveri', 'pinky', 'priya', 'ram', 'vamsy', 'venkat', 'viswa']
# name=['p','n','Y','t','o','H']
# name.sort()
# print(*name)                    #H Y n o p t
# name.sort(reverse=True)
# print(name)                       #['t', 'p', 'o', 'n', 'Y', 'H']
# for i in name:
    # print(i)

#  """     Shift Operator   (>>Right /2  and  <<left *2     """
# a=20
# print(a>>1)            #10
# print(a>>2)            #5
# print(a>>3)            #2
# b=4
# print(b<<1)            #8
# print(b<<2)            #16
# print(b<<3)            #32


