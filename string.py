sen=input()
ls,sen=list(sen.split()),''
for i in ls:sen+=i[::-1]+' '
print(sen)
