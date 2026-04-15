'''
    def salom_ber(a, b):
        if a == b:
            print("kvadrat ")
        else:
            print("Togri tortburchak ")

    x = int(input("a ni kiriting: "))
    y = int(input("b ni kiriting: "))

    salom_ber(x,y)'

    def get_info(name, age, address):
        print(f"Ism: {name}, Yoshi: {age}, adress: {address}")



    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    adress = input("Manzilingizni kiriting: ")




    get_info(ism, yosh, adress)



    def test2(d):
        return {i : i**2 for i in range (d)}


    print(test2(8))

    def son_k(s):
        




    a = input["1","2","3"]


    '''
    #1-masala

    # def ism_kirit(ism):
    #     print(f"Salom {ism}!")


    # ism = input("Ismingizni kiriting: ")


    # ism_kirit(ism)


    #2-masala

    # def son_k(s):
    #     if s > 0:
    #         print("Musbat son")     
    #     elif s < 0:
    #         print("Manfiy son")     
    #     else:
    # k = int(input("Son kiriting: "))    
    # son_k(k)


    #3-masala

    # def son_k(k): 
        
    #     d = k*k
    #     return d

    # k = int(input("Son kiriting: "))
    # print(son_k(k))

    #4-masala

    # def son_k(s):
    #     if s % 2 == 0:
    #         print("Juft son")
    #     else:
    #         print("Toq son")    
    # s = int(input("Son kiriting: "))
    # son_k(s)    

# def son_k(n):

#     d = 1

#     for i in range(1,n+1):
#         d *= i
#     return d

# n = int(input("Son kiriting: "))
# print(son_k(n))


  


# def son_k(*args):

#     sanoq = 0
#     for i in args:
#         if i % 2 == 0 :
#             sanoq +=1
#     return sanoq       
   
# print(son_k(1, 2, 3, 4, 15, 6, 70, 80, 9, 10))


# def kirit(*args):
#     sanoq = 0 
#     for i in args:
#         if i > 0 :
#             sanoq += 1
#     return sanoq

# print(kirit(1,-2,5,-6,4,-9,-8,10))
   

# def kirit (**kwargs):
#    sanoq = 0
#    for i in kwargs.values():
#       if type(i) == int:
#             sanoq += i
#    return sanoq

# print(kirit(a=1, b=2, c=3, d="salom", e="dunyo", f=4, g=5))
      

# def kirit(*args ):
#     sanoq1 = 0
#     sanoq2 = 0 
#     sanoq3 = 0 
#     for i in args:
#         if type(i) == int:
#             sanoq1 += 1 
#         elif type(i) == str:
#             sanoq2 +=1
#         elif type (i) ==float:
#             sanoq3 +=1
       
#     return {
#         "int": sanoq1,
#         "str": sanoq2,
#         "float": sanoq3
#     }
        
# print(kirit(1, 2, 3, "salom", "dunyo", 4.5, 5.6, 7, 8, "python", 9.0))  

# def hisobla(*args, **kwargs):
#     operation = kwargs.get("operation")

#     if operation == "add":
#         return sum(args)

#     elif operation == "mul":
#         natija = 1
#         for i in args:
#             natija *= i
#         return natija

#     elif operation == "max":
#         return max(args)
    
# print(hisobla(1, 2, 3, 4, operation="add"))
# print(hisobla(1, 2, 3, 4, operation="mul"))
# print(hisobla(1, 2, 3, 4, operation="max"))

# n = int(input("son kirit " ))

# sanoq = 0
# d = 0
# while n > 0:
#     d = n % 10
#     print (d)
#     n = n // 10 
#     sanoq +=1

# print(sanoq)


# password = '1234'

# while True:
#     x = input ("parol kiritong: ")
#     if x == password:
#         print("tizimga kirdingiz")
#         break 
#     if 

#     print ('Xaro parol')
    


# n = int(input())
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# n = int(input())
# i = 1
# sanoq = 0
# while i <= n:
#     if i % 2 != 0:
#         sanoq += 1
#     i += 1
# print(sanoq)

# n = int(input())
# while n >= 1:
#     print(n)
#     n -= 1

# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1

# n = int(input())
# i = 1
# sanoq = 0
# while i <= n:
#     if i % 3 == 0:
#         sanoq += 1
#     i += 1
# print(sanoq)

# n = int(input())
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# n = int(input())
# sanoq = 0
# while n > 0:
#     sanoq += 1
#     n //= 10
# print(sanoq)

# n = int(input())
# max_raqam = 0
# while n > 0:
#     r = n % 10
#     if r > max_raqam:
#         max_raqam = r
#     n //= 10
# print(max_raqam)

# n = int(input())
# min_raqam = 9
# while n > 0:
#     r = n % 10
#     if r < min_raqam:
#         min_raqam = r
#     n //= 10
# print(min_raqam)

# n = int(input())
# i = 2
# tub = True

# while i < n:
#     if n % i == 0:
#         tub = False
#     i += 1

# if tub and n > 1:
#     print("tub")
# else:
#     print("tub emas")

# n = int(input())
# i = 1
# f = 1
# while i <= n:
#     f *= i
#     i += 1
# print(f)

# n = int(input())
# i = 2
# sanoq = 0

# while i <= n:
#     j = 2
#     tub = True
#     while j < i:
#         if i % j == 0:
#             tub = False
#         j += 1
#     if tub:
#         sanoq += 1
#     i += 1

# print(sanoq)

# n = int(input())
# teskari = 0
# while n > 0:
#     teskari = teskari * 10 + n % 10
#     n //= 10
# print(teskari)

# n = int(input())
# original = n
# teskari = 0

# while n > 0:
#     teskari = teskari * 10 + n % 10
#     n //= 10

# if original == teskari:
#     print("palindrom")
# else:
#     print("palindrom emas")

# s = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     s += n
# print(s)

# max_son = -999999
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n > max_son:
#         max_son = n
# print(max_son)

# sanoq = 0
# while True:
#     n = int(input())
#     if n < 0:
#         break
#     if n > 0:
#         sanoq += 1
# print(sanoq)












