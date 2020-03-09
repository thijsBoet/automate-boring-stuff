import smtplib

# specify SMTP connection
conn = smtplib.SMTP('smtp.ziggo.nl', 587)

# start connection
conn.ehlo()
# start tls encryption
conn.starttls()
# login
conn.login('m.boet2@upcmail.nl', '#####')
# sender email | receiver email | Subject: \n\n email body
conn.sendmail('m.boet@chello.nl', 'creative.steve@gmail.com', 'Subject: Python send mail script\n\nTest email send via python script.\n\nMatthijs')

conn.quit()