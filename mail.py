import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "ashishjohn242@gmail.com"
host_pass = "*****"
guest_address = "adsk1469@gmail.com"
subject = "Regarding Succesfull completion for your model through  jenkins "
content = '''Hey there, 
                               Developer this is an email regarding to your model of CNN.Your model has been successfully created and trained with the best ever Accuracy.
                               For any further procedding,YOU ARE GOOD TO GO.
                                Congarts!~_~
                        THANK YOU ...'''
                        
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()

session.sendmail(host_address, guest_address, text)
session.quit()
print('Successfully sent your mail')
