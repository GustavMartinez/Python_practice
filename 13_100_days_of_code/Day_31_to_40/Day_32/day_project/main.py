import datetime as dt
import pandas as pd
import random
import smtplib
from my_pass import password
from email.message import EmailMessage


MY_EMAIL = 'dibujo3dgt@gmail.com'
MY_PASS = password



DATA_PATH = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_32/day_project/birthdays.csv'

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv(DATA_PATH)

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f'/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_32/day_project/letter_templates/letter_{random.randint(1,3)}.txt'
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])



    msg = EmailMessage() # NUEVA CONFIGURACION
    msg['Subject'] = "Happy Birthday" # NUEVA CONFIGURACION
    msg['From'] = MY_EMAIL # NUEVA CONFIGURACION
    msg['To'] = birthday_person['email'] # NUEVA CONFIGURACION
    msg.set_content(contents) # NUEVA CONFIGURACION


    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls() # Make the connection secure
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.send_message(msg) # ADICION DEL msg CREADO


