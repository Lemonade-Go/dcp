"""
d1 solution
"""

"""
Psuedocode thinking:
	- have a list [1,2,3,4,5]
	- python can print list elements doing stack[::1] in order and stack[::-1] in reverse
	mylist = [1,2,3,4,5]- if we take list length, and read 
	from front and end mylistand walk towards middle, should be able to create a new list.
	- struggling to understand the requirement of "must be in place" and how that will work with this code. 
	- thinking list comprehension may have a cool way of doing this too... just havent figured it out yet.
	- added in logic to make sure you didnt duplicate last item on odd length list
"""

def interleave(mylist):
	count = 0
	secondlist = []
	while count < (len(mylist)/2):
		secondlist.append(mylist[::1][count])
		if len(secondlist) > len(mylist)-1:
			break
		else:
			secondlist.append(mylist[::-1][count])
		count += 1
	return secondlist

if __name__ == "__main__":
	mylist = [1,2,3,4,5]
	print(interleave(mylist))
