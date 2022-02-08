import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
def send_mail():
    mail_content = '''Hello,
    This mail was sent after an attempt of executing the auto buyer bot.
    Below you will find the log file attachment.
    Thank You
    '''
    #The mail addresses and password
    sender_address = 'spyspy3688@gmail.com'
    sender_pass = '87654321bot'
    receiver_address = "abdellatifthabet4@gmail.com"
    #jackeline@synkira.com, yasoluciones@yahoo.es
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Bot verification mail. It has an attachment.'
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name1 = '/home/ubuntu-vm/last-release/spain_log.txt'
    attach_file_name2 = '/home/ubuntu-vm/last-release/portugal_log.txt'
    attach_file1 = open(attach_file_name1, 'rb') # Open the file as binary mode
    attach_file2 = open(attach_file_name2, 'rb') # Open the file as binary mode
    payload1 = MIMEBase('application', 'octate-stream')
    payload2 = MIMEBase('application', 'octate-stream')
    payload1.set_payload((attach_file1).read())
    payload2.set_payload((attach_file2).read())
    encoders.encode_base64(payload1) #encode the attachment
    encoders.encode_base64(payload2) #encode the attachment
    #add payload header with filename
    payload1.add_header('Content-Decomposition', 'attachment', filename=attach_file_name1)
    payload2.add_header('Content-Decomposition', 'attachment', filename=attach_file_name2)
    message.attach(payload1)
    message.attach(payload2)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, ['abdellatifthabet4@gmail.com'], text)
    #'jackeline@synkira.com','yasoluciones@yahoo.es'
    #'yasoluciones@yahoo.es', 
    session.quit()
    print('Mail Sent')
    
    os.remove("/home/ubuntu-vm/last-release/spain_log.txt")
    os.remove("/home/ubuntu-vm/last-release/portugal_log.txt")
    return

send_mail()
