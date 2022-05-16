# Don't go outside in odd day

len = int(input("Enter len of the series : "))
lst = []

for i in range(len):
    num = int(input("Enter series numbers one by one : "))
    lst.append(num)

tup = tuple(lst)
print("Series you provide is :",tup)

evens = 0
odds = 0

for j in tup:
    if j % 2 == 0:
        evens += 1
    else:
        odds += 1

print("Numbers of Even Numbers :",evens)
print("Numbers of Odd Numbers :",odds)