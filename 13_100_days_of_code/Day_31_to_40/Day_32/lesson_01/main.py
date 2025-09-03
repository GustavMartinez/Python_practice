import smtplib

my_email = 'gustavo.a.t.m.12345@hotmail.com'
password = ''


try:
    connection = smtplib.SMTP("smtp.office365.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="destinatario@hotmail.com",
        msg="Subject: Prueba\n\nEste es un correo enviado con contraseña de aplicación."
    )
    print("Correo enviado exitosamente.")
except smtplib.SMTPAuthenticationError as e:
    print("Error de autenticación:", e)
finally:
    connection.quit()