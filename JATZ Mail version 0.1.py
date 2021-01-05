import smtplib
from tkinter import *


def sendOut():
    for i in range(1):
        sender_email = '' #Person to send email from
        rec_email = email_sendTo.get() #Person to recieve the email
        password = input(str('Enter Password To Senders Account: ')) #Password to the sender's account
        print('Password Entered 1/3')
        message = mess_Send.get() #Message to send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password) #Does login
        print('Logged Into Server 2/3')
        server.sendmail(sender_email, rec_email, message) #Sends Email
        print('Message Sent 3/3')
        print('Message Sent Success!')

root = Tk()
root.title('JATZ MAIL')
root.geometry('500x200')
root.resizable(width=False, height=False)

bgFrame = Frame(root, background='lightblue').place(x=0, y=0, width=500, height=500)

enterMessL = Label(bgFrame, text='Enter Message that you want to send', bg='lightblue', font=('Times', 11)).place(x=210, y=34)
recEmailL = Label(bgFrame, text="Enter reciever's email", bg='lightblue', font=('Times', 11)).place(x=210, y=63)

sendButton = Button(bgFrame, text='Send Emails', command=sendOut).place(x=5, y=5, width=95, height=24)

mess_Send = StringVar()
enterMess = Entry(bgFrame, textvariable=mess_Send).place(x=5, y=34, width=200, height=24)
email_sendTo = StringVar()
enterReciever = Entry(bgFrame, textvariable=email_sendTo).place(x=5, y=63, width=200, height=24) 

