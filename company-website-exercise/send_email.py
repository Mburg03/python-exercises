import smtplib, ssl, os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "marioua289@gmail.com"
    password = os.getenv("PASSWORD")    
    receiver = "marioua289@gmail.com"
    my_context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host=host, port=port, context=my_context) as server:
        server.login(user=username, password=password)
        server.sendmail(from_addr=username, to_addrs=receiver, msg=message) 
               