import random
import smtplib
import Sender_data

def generateOTP(size):
    digits = "0123456789"
    OTP = ""
    for i in range(size):
        OTP += digits[random.randint(0,9)]
    return OTP

def verifyOTP(otp):
    otp_1 = input("Enter your OTP >> ")
    if otp_1 == otp:
        print("Verified!")
    else:
        print("Incorrect OTP!")

sender_email=Sender_data.email
sender_password=Sender_data.password

def sendOTP():
    # Connect to server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Login to gmail account of sender
    s.login(sender_email, sender_password)   

    # Generate OPT
    size=int(input("Enter length of OTP: "))
    OTP=generateOTP(size)

    #Generate message to be sent
    msg = str(OTP)+" is your OTP"

    # Send email
    receiver_email = input("Enter your email: ")
    s.sendmail(sender_email, receiver_email, msg)
    print("OTP sent!")  

    # Disconnect server
    s.quit()
    return OTP


# Send OTP
OTP=sendOTP()

# Verify OTP
verifyOTP(OTP)
