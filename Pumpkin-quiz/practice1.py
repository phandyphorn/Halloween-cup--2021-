
print("Hello")
# NumberOne
arrayOfString = eval(input())
oddArray = []
for index in range(len(arrayOfString)):
    if index%2 == 1:
        oddArray.append(arrayOfString[index])
print(oddArray)

# NumberTwo
list1 = [1,3,5,7,9,11,13]
list2 = [2,3,6,7,10,11,15]
list3 = [4,5,6,7,8,12,16,14]
list4 = [2,5,4,7,8,9,10,21,34,12]
list5 = [4,6,7,8,1,2,3,4,5,7,9]
lists = [list1] + [list2] + [list3] + [list4] + [list5]
for index in range(5):
    strInput = strInput()
    

print("Hello crush")
# Exercise2
# number=str(123)
# space=""
# result=""
# index=0
# while index<len(number):
#     row=""
#     for value in range(int(number[index])):
#         row+="-"
#         space+=" "
#     index+=1
#     if index==len(number):
#         result+=row
#     else:
#         result+=row+"\n"+space+"|\n"+space
# print(result)

# number=eval(input())
# isNotFoundD=True
# index=0
# letter=input()
# while isNotFoundD and index<len(number)-1:
#     if number[index]=="D":
#         if letter=="R":
#             isNotFoundD=False
#             number[index]='0'
#             number[index+1]='D'
#         elif letter=="L":
#             isNotFoundD=False
#             number[index]='0'
#             number[index-1]="D"
#     index+=1
# print(number)
