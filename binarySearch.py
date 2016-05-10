def info(ans, guess, count):
	print "%d. Answer:%d, Guess:%d" % (count, ans, guess)

print "Please enter the lower and upper bounds"
x = raw_input('> ')
lo, hi = x.split()
lo = int(lo); hi = int(hi)
print "Please enter your secret number (within your bounds)"
ans = input('> ')

count = 1
while True:
	guess = (lo + hi)/2
	info(ans, guess, count)
	if guess == ans:
		print "YAY! Finding the answer took me %d guesses." % count
		break
	else:
		if guess > ans:
			hi = max(lo, ((lo+hi)/2)-1)			
		else:
			lo  = min(hi, ((lo+hi)/2)+1)
	count += 1


