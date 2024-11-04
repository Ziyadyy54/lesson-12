word=input("enter your word ")
letter=input("enter your letter ")
count=0
lettertimes=0
while(lettertimes<len(word)):
    if(word[lettertimes]==letter):
        count=count+1
    lettertimes=lettertimes+1
print("total number of times",letter,"is appearing is",count)