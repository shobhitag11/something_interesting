from num2words import num2words

arr = input("Input array: ")
arr = eval(arr)

for ele in arr:
    print(ele)
    print(num2words(ele))
