#Udemy day 32
import smtplib

# my_email ="sneha.patel1@aliansoftware.com"
# password ="Sneha1@alian"
# connection =smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="sneha.patel1@aliansoftware.com",msg="hello")

my_email = "abcd1234567sp@gmail.com"
password = "unjggoojpipszyqr"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abcd1234567sp@gmail.com",
                        msg="Subject:hello \n\nthis the email body.")
    connection.close()
