print("Hello")
value=eval(input())
result=[]
for i in range(len(value)):
    if i %2 ==0:
        result.append(i)
print(result)