print('How many cats do you have?')
numCats = input()
try:
	if int(numCats) >= 4:
		print('That is a lot cats.')
	elif int(numCats) < 0:
		print('You cannot enter a negative number.')
	else:
		print('That is not that many cats.')
except ValueError:
	print('You did not enter a number.')