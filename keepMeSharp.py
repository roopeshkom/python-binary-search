from sys import argv

def find_extreme(arr, which_one):
	if not arr:
		raise Exception("Empty List is bad")
	xtrm = arr[0]
	for i in arr:
		if which_one == "max":
			if i > xtrm: xtrm = i
		elif which_one == "min":
			if i < xtrm: xtrm = i
		else:
			print which_one
			raise Exception("Please enter a valid command")
	return xtrm

name, command , x = argv
x = x.split(',')
for i in enumerate(x):
	step, val = i
	x[step] = int(val)
print find_extreme(x, command)
