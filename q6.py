str1=input("Enter string 1: ")
str2=input("Enter string 2: ")

def check_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    if (sorted(str1)==sorted(str2)):
        print("Given strings are anagrams")

check_anagram(str1,str2)