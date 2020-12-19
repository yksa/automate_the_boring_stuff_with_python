message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} 

for character in message: # for character in message.upper(): or for character in message.lower():
	count.setdefault(character, 0)
	count[character] = count[character] + 1

print(count)