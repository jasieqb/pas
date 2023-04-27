import smtplib

with smtplib.SMTP("localhost", 8025) as smtp:
    smtp.sendmail("from@localhost", ["to@localhost"], "Hello world!")
