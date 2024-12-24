# from typing import List


# def skipNum(n: int) -> int:
#     lst = []
#     for i in range(1,n+1):
#         lst.append(i)
#     return(temp(lst))

# def temp(lst: List) -> int:

#     if(len(lst)) == 1:
#         print(lst[0])
#         return lst[0]
    
#     else: 
#         i= 0
#         while(i < len(lst)):
#             lst.pop(i)
#             i+=1

#     print(lst)
#     temp(lst[::-1])


    # while
# Your code here

# print(skipNum(10))



def skipNum(n: int) -> int:
    if(n==1):
        return 1
    else:
        x= n//2
        sol = skipNum(x)
        return(2*(x+1-sol))


print(skipNum(9))