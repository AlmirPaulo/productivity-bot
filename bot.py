from flask import Flask
from flask_mail import Mail, Message
import time, random

app = Flask(__name__)
mail = Mail()

msgs = ["blabla", "bleble","bbloblbo", "bleoblei"]



@app.route('/', methods=['POST'])
def email():
    while True:
        time.sleep(15)
        reminder = random.choice(msgs)
        print(reminder)
        #Getting data
        email = config.EMAIL
        subject = "Productivity bot"
        text = reminder

        #Sending email
        msg = Message(subject)
        msg.body = text
        msg.recipients = [config.MAIL_DEFAULT_SENDER]
        mail.send(msg)

        logging.info('email sent')





#Factorization
#Configuration
app.config['SECRET_KEY'] = '...'
app.config['MAIL_SERVER'] = config.MAIL_SERVER
app.config['MAIL_PORT'] = config.MAIL_PORT
app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER
app.config['MAIL_MAX_EMAILS'] = config.MAIL_MAX_EMAILS
app.config['MAIL_ASCII_ATTACHMENTS'] = config.MAIL_ASCII_ATTACHMENTS

#Initializations
mail.init_app(app) 


if __name__=='__main__':
    app.run(debug=True)

