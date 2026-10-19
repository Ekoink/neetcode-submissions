class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False        

#somethign that looks through the input: racecare and if all the element s in one words is the same as the one in the order, return true
#kinda thinking about true statmeent for this then
#the orddder doesnt matter
#there's a form thingie that thakes stuff and doesnt care aboutt he order of the thingie, a function thing
#i'm tinking make a set of s and a set of t
#compare if set s and set t are the same

#that is actually wrong because it's like bro
#it needs to be somethign that will not care for the order of the things in it, like a lsit perhaps? lists care though
#i need somethign that will compare each item ijn the s list to each item in the t lsit,
#like take the first letter dn find it in the second list, and then compare them
#like, oh, r

#but a set wont work becuase it ends up like squishing the stuff and not allwoign duplicates
#but if we work with lsits, and i sort them accoridng tho their aplhabetical shi
#then compare the two lsits witht he aplahbetical shi sorted, adn see what's happening
#that would preserve the duplicates