import smtplib
import random as rd
import datetime as dt
from my_pass import password
from email.message import EmailMessage


PATH_QUOTES = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_32/lesson_03/quotes.txt'
MY_EMAIL = 'dibujo3dgt@gmail.com'
MY_PASS = password



def send():



    with open(PATH_QUOTES, encoding='utf-8') as file: # adiccion de encoding
        all_quotes = file.readlines()
        quote = rd.choice(all_quotes)

    msg = EmailMessage() # NUEVA CONFIGURACION
    msg['Subject'] = "Motivational Quote" # NUEVA CONFIGURACION
    msg['From'] = MY_EMAIL # NUEVA CONFIGURACION
    msg['To'] = 'gustavo.arq.2016@hotmail.com' # NUEVA CONFIGURACION
    msg.set_content(quote) # NUEVA CONFIGURACION


    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls() # Make the connection secure
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.send_message(msg) # ADICION DEL msg CREADO



date = dt.datetime.now()
day_week = date.weekday()

if day_week == 2:
    send()





