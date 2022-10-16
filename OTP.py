import math
import random
import smtplib

# Generate OPT
digits = "0123456789"
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random() * 10)]

#Generate message to be sent
msg = str(OTP)+" is your OTP"

# Connect to server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# Login to gmail account of sender
s.login("jadhavanushka994@gmail.com", "gdabeyfoklrtpgip")

# Input receiver's email
emailid = input("Enter your email: ")

# Send email
s.sendmail("jadhavanushka994@gmail.com", emailid, msg)
print("OTP sent!")

# Disconnect from server
s.quit()


# Verify OTP
a = input("Enter your OTP >> ")
if a == OTP:
    print("Verified!")
else:
    print("Incorrect OTP")
