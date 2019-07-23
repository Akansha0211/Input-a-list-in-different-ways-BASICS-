#METHOD 1
# list=[]
# n=int(input("Enter the number of elements in the list"))
# for i in range(0,n):
#     x=input()
#     list.append(x)
# print("The list is",list)

#METHOD 2
# try:
#     list=[]
#     n=int(input("Enter tyhe length of list"))
#     for i in range(0,n):
#                         list.append(int(input()))
#     print(list)
# except Exception as e:
#                       print(e)
#

#METHOD 3
# my_list=list(map(int,input("Now enter elements").split(",")))
# print("List",my_list)

#method 4
#LIST OF LISTs
lst=[]
n=int(input("Enter the number of elements in a list"))

for i in range(0,n):
     ele=[input(),int(input())]
     lst.append(ele)
print(lst)


