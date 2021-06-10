str1,str2=input().split(",")            
str1,str2=str1.lower(),str2.lower()
if sorted(str1)==sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")

            
