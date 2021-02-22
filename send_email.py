import smtplib
import time
import my_infos

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# SMTP server
login = my_infos.login
password = my_infos.password
s = smtplib.SMTP(host='smtp.mailtrap.io', port=2525)
s.starttls()
s.login(login, password)

# Função para ler os contatos de um arquivos de um arquivo e 
# retornar uma lista com nome e email.
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

# Função para salvar a mensagem.
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


names, emails = get_contacts('mycontacts.txt')  # read contacts
message_template = read_template('message.txt')
###img_data = open('sea_photo.jpg', 'rb').read()


# Enviar o email para cada contato.
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # Adicionar o nome de cada um à variável nome no arquivo de texto da mensagem.
    message = message_template.substitute(PERSON_NAME=name.title())

    # Arrumar os parâmetros para a mensagem.
    msg['From']="testandoemail@mail.com"
    msg['To']=email
    msg['Subject']="Sim, isso é um teste."

    msg.attach(MIMEText(message, 'plain'))
    

    # Enviar o email através do servidor.
    sent = s.send_message(msg)
    for sent in range(10):
        if sent == True:
            time.sleep(2)

    del msg
