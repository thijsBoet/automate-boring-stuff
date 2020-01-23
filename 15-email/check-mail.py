import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.ziggo.nl', ssl=True)
conn.login('m.boet2@upcmail.nl', '#####')

conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['UNSEEN'])
rawMessage = conn.fetch(UIDs, 'BODY[]', 'FLAGS')

message = pyzmail.PyzMessage.factory(rawMessage[UIDs][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.text_part.get_payload().decode('UTF-8')