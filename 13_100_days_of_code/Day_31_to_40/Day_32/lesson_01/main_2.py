from my_pass import password as my_pasw
import smtplib


my_email = 'dibujo3dgt@gmail.com'


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # this line makes the connection secure
    connection.login(user=my_email, password=my_pasw)
    connection.sendmail(from_addr=my_email, 
                        to_addrs='gustavo.arq.2016@hotmail.com', 
                        msg='Subject:Email de prueba\n\nNuevo email con subject',
                        )

    connection.close()