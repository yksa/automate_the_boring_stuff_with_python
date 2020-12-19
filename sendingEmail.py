import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()	#connection start
conn.starttls() #encription
conn.login('asweigart@gmail.com', '1xkjfvcr1xxiinmj') #('username@gmail.com', 'password or app specific password')

#(from)addr, to_addr, msg, mail_options-[], rcpt_options=[])
conn.sendmail('asweigart@gmail.com', 'someone@gmail.com', 'Subject: So long...\n\nDear Al, \nSo long, and thanks for all the fish.\n\n-Al') 
conn.quit()