lst = []
num = int(input('how many numbers:'))
for n in range(num):
    num=int(input('enter numbers:'))
    lst.append(num)
print("maximun element in the list is:",max(lst),"\n minimum element in the list is:",min(lst))
