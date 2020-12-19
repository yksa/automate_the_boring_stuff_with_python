import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''

	(((\d\d\d) | (\(\d\d\d\)))?		# area code optional
	(\s|-)							# first separator
	\d\d\digits 					# first 3 digits
	-								# separator
	\d\d\d\d 						# last 4 digits
	(((ext(\.)?\s) | x) (\d{2,5}))?)	# extension optional
	''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
	# somethin@someth.something
	[a-zA-Z0-9_.+]+					# name part
	@								# @ symbol
	[a-zA-Z0-9_.+]+					# domain name part
	''', re.VERBOSE)

# text = pyperclip.paste()
text = '''Shirley Carrillo shirleyc43@gmail.com 862-903-5577
Anderson Gibson agibson78@gmail.com 971-459-6814
Millard Foster millardf16@gmail.com 832-973-8787
Stephen Workman sworkman10@mac.com 724-235-8718
Rex Gonzalez rgonzalez19@yahoo.com 401-388-1482
Loyd Morris lmorris@icloud.com 620-456-6406
Alonzo Mckee amckee52@hotmail.com 604-970-5352
Aron Wise awise70@outlook.com 205-650-8301
Shelby Pope spope39@hotmail.com 503-692-6921
Robby Riggs tqqfpjflk38@comcast.net 832-401-6373
Tyron Cooper lsdjhcpu86@hotmail.com 627-940-2958
Domingo
Carpenter dcarpenter50@sbcglobal.net 412-988-2153
Walker Castro wcastro99@hotmail.com 702-441-4902'''

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)