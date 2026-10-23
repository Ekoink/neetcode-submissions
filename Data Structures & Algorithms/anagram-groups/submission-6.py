class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        srtd_anagrams = {}
        for n in range(0, len(strs)):
            sort = "".join(sorted(strs[n]))
            if sort in srtd_anagrams:
                srtd_anagrams[sort].append(strs[n])
            else:
                srtd_anagrams[sort] = []
                srtd_anagrams[sort].append(strs[n])
#                srtd_anagrams.setdefault("n", []).append(n)
#            anagrams.append(srtd_anagrams.values)
            anagrams = list(srtd_anagrams.values())
        return anagrams

#values_list = list(my_dict.values())
'''
a new list called anagrams
make a dictionary (empty)
go through each item in strs
compare if sorted n exists as a key in dictionary
if it does, add it as a value to that key in a list
if it doesnt, add it as a key and a value to that key in the dictionary the value should be in a list
add all the values in the dictionaries to my new list, anagrams 
return anagrams
'''

#my_dict = {"scores": [10, 20]}
# Add a single item
#my_dict["scores"].append(30)


#my_dict = {}
# Safely creates the key and appends the item
#my_dict.setdefault("scores", []).append(10)

#first loop 
#second loop
#soo, here's what should go on, 
#it should look through the dictionary created, 
#oh, is there a key,
#oh no key of the first element 'act'; then you sort it like chakam
'''
add act as the key, and as the value
then for th enext item
sort it
search wit the sorted one if it is a key in the dict
no? ok. add it as a key and as it's own value
then if you come across one that when you sort it, it is a key already in the dictionary
then you jut add it to the value
than after everyhting you drop the stuf in a list and send the lsit
'''


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        not_append = set()
        for n in range(0, len(strs)):
            if strs[n] not in not_append:
                mini_lists = [strs[n]]
                for i in range(n+1, len(strs)):
                    if sorted(strs[n]) == sorted(strs[i]):
                        mini_lists.append(strs[i])
                        not_append.add(strs[i])
                anagrams.append(mini_lists)
        return anagrams
'''

#so this code basically makes a new list for each word|
#creates the condition that says for everythgi afgter this, it has to not be in the the not_append list
#says if the word is equal to another word after sorting, append it to the original list
#also append the word that was found equal to the original list to the not_append list
#this will stop it from like, making a new list for the word that has already been added, and having multiple repetiitons of the same lists of anagrams

#so if instead i have a dictionary with all the stuff and i append thigns there instead
#like i append each word into th dictionary
#because then it wont need to 

'''
each element in the list and compares to the next one
if they're the same, element 1 same as element 2
, adds that in a new list
do the same thign for each element
print a final list, that has all the mini-lists 

actt != cat
act == cat
[act, cat]

anagrams = []
for n in range(0, len(strs)):
    mini_lists = [strs[n]]
    for i in range(n+1, len(strs)):
        if strs[n] == strs[i]:
            mini_lists.append(strs[i])
    anagrams.append(mini_lists)


range(start, stop, interval)
len(list)

acts
pots
tops
cat
stop
hat
'''




