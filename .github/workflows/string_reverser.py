string = str(input('please enter a sentence: '))
splt=string.split()
reverse=splt[::-1]
for i in range(len(reverse)):
    print(reverse[i],end=' ')
