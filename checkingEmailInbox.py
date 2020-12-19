import imapclient, pyzmail

# (host, port=None, use_uid=True, ssl=False, stream=False, **)
# A connection to the IMAP server specified by *host* is made this class is instantiated.
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) 
conn.login('username@gmail.com', 'password')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2015'])

rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
message.text_part
message.html_part
message.text_part.get_payload().decode('UTF-8')
message.text_part.charset

conn.list_folders()

conn.select_folder('INBOX', readonly=False) #To delete

UIDs = conn.search(['ON 24-Aug-2015'])

conn.delete_messages([47473])
conn.delete_messages(UIDs) #To delete all uids

conn.logout()