list=[1,2,3,4,5,5,6,6]
list1=[1,2,3,7,8,8,9]

num1=set(list)
num2=set(list)

print(num1|num2)
print(num1-num2)
print(num1^num2)
print(num1&num2)

print(len(num1))