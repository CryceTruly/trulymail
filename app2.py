from flask_mail import Mail, Message
from flask import Flask
app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'crycetruly@gmail.com',
	MAIL_PASSWORD = 'Xvq6thC++'
	)
mail = Mail(app)

@app.route('/send-mail/')
def send_mail():	
    try:
         msg = Message("New Email Test",
         sender="aacryce@gmail.com",
         recipients=["chrisahebwa@gmail.com"])
         msg.body = "Heylo your order has been delivered"
         mail.send(msg)
         return 'Mail sent!'
    except Exception as identifier:
        pass
   

if __name__=="__main__":
     app.run(debug=True)