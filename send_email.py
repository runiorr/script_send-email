# import the smtplib module. It should be included in Python by default
import smtplib
import time
import my_infos

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
###from email.mime.image import MIMEImage



# set up the SMTP server
login = my_infos.login
password = my_infos.password
s = smtplib.SMTP(host='smtp.mailtrap.io', port=2525)
s.starttls()
s.login(login, password)


# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

# Function to save the message
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


names, emails = get_contacts('mycontacts.txt')  # read contacts
message_template = read_template('message.txt')
###img_data = open('sea_photo.jpg', 'rb').read()


# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']="testandoemail@mail.com"
    msg['To']=email
    msg['Subject']="Sim, isso é um teste."

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    

    # send the message via the server set up earlier.
    sent = s.send_message(msg)
    for sent in range(10):
        if sent == True:
            time.sleep(2)

    del msg