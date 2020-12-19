import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #Write logging info to txt file

# logging.disable(logging.CRITICAL) #To disable logging debug message

logging.debug('Start of program')

def factorial(n):
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	for i in range(n):
		total *= (i+1)
		logging.debug('i is %s, total is %s' % (i, total))

	logging.debug('Return value is %s' % (total))
	return total

num = int(input())
print(factorial(num))

logging.debug('End of program')