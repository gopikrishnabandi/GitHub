# opening the browser
# useful for automation
from string import Template
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # MIMEMultipart is a class
import webbrowser
# prints in terminal(used more as a success message in this program)
print("Deployment Completed")
webbrowser.open("http://google.com")  # then opens browser
# sending emails
# we need to import some classes
# one to create messages, other to connect to smtp server to send emails
# from email.mime.multipart import MIMEMultipart
# mime stands for multipurpose internet mail extensions
# stanard for defining emails
# can send emails with html as well as plain text
message = MIMEMultipart()
message["from"] = "Gopi Bandi"
message["to"] = "gopikrishnabandi.37@gmail.com"
message["subject"] = "Tḫis is a test"
# above are various headers supported by Mimemultipart object, it does not have a header for body
# we can use attach to resolve
# import email.mime.text import MIMEText
# message.attach(MIMEText("Call me Tufri "))
message.attach(MIMEText("Automated email message using python "))
# we now have a mail message object,now we need to send this using an smtp server
#import smtplib
# has method called SMTP
# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)  #returns an SMTP obj
# smtp.close()
# use with to avoid explicit closing
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # some steps to be followed for sending an email
    smtp.ehlo()  # this is hello, greeting to an smtp server
    smtp.starttls()  # puts smtp connection in tls mode, transport layer security, for encryption of message while sending to smtp
    smtp.login("gopikrishnabandi09@gmail.com", "sg437$s;;")
    # message is our email message object from above
    smtp.send_message(message)
    print("sent")  # for confirmation on terminal
# we can also send image
#from email.mime.image import MimeImage
#from pathlib import path
# message.attach(MimeImage(Path("gopi.png").read_bytes()))

# working with templates
# in real world in body we dont use plain text, we use html templates
# to quickly generate html code in the html file, press ! and tab
# from string import Template, Template class used for replacing parameters in html file
template = Template(Path("template.html").read_text())
# pass all key vaue pairs defined in html
body1 = Template.substitute({"name": "john"})
# body1 = Template.substitute(name="john")#also can pass keyword arguments instead of a dictionary for substitue method
message.attach(MIMEText(body1, "html"))
