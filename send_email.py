import smtplib
import os
from dotenv import load_dotenv
load_dotenv() 

print(os.getenv("Tomail"))
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(os.getenv("myemail"),os.getenv("mypassword"))
    server.sendmail(os.getenv("myemail"), os.getenv("Tomail") , 'email automation')
    server.close()

sendEmail()
#There will be many problems in this program as App password will be struck
#smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. For more information, go to\n5.7.8  https://support.google.com/mail/?p=BadCredentials 98e67ed59e1d1-2b628861e3bsm2786375a91.23 - gsmtp')
#smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required. For more information, go to\n5.7.9  https://support.google.com/mail/?p=InvalidSecondFactor 98e67ed59e1d1-2b671782d7bsm1076133a91.51 - gsmtp')