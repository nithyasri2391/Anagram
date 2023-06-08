#Anagram Grouping
    #  Anagrams are words that have the same characters but in a different order.
		

	#Sample Input: ["cat", "dog", "tac", "god", "act"]
	#Sample Output:[["cat", "tac", "act"], ["dog", "god"]]

    
import re
print("enter input:")
str_input=re.sub("[\[\]\"\\s]","",input())
list_input=str_input.split(",")
list_input=[*set(list_input)]
list_anagrams={}

for name in list_input:
    sorted_name=str(sorted(name))

    if sorted_name in list_anagrams:
        #if name not in list_anagrams.values():
        list_anagrams[sorted_name].append(name)

    else:
        list_anagrams[sorted_name]=[name]
print("output:")
print(list(list_anagrams.values()))
