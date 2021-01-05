import smtplib, turtle, time, webbrowser, random
from tkinter import *

loaduprandom = random.randrange(0, 100)

developerPassword = 'iamdev'
def sentAni():
    john = turtle.Turtle()
    john.hideturtle()
    john.penup()
    john.speed(0)
    john.left(120)
    john.forward(120)
    john.left(90)
    john.color("red")
    john.pendown()
    john.circle(140)
    for i in range(30):
        john.left(10)
        john.circle(140)
    john.penup()
    john.color("green")
    style1 = ("Times", 40, "bold")
    john.write("Email Sent!", font=style1, align='center')
def devSec():
    def rememberPassword():
        global passwordRemembered
        passwordRemembered = passR.get()
    if devPassword.get() == developerPassword:
        root.geometry('800x400')
        devF = Frame(root, background='#bfebff').place(x=0, y=250, width=800, height=200)
        devCB = Button(devF, text='Close Dev Section', command=lambda:root.geometry('800x250')).place(x=5, y=313, width=200, height=24)
        devCD = Button(devF, text='Terminate JATZ', command=lambda:root.destroy()).place(x=5, y=285, width=200, height=25)
        passR = StringVar()
        passRem = Entry(devF, textvariable=passR).place(x=210, y=255, width=200, height=24)
        passRemL = Label(devF, text='Enter password to remember (this session only)', bg='#bfebff').place(x=415, y=255)
        SPB = Button(devF, text='Save Password', command=rememberPassword).place(x=5, y=255, width=200, height=24)
    else:
        print('Invalid Developer password')
def sendOut():
    sender_email = 'eggowafflesarebadlmao123@gmail.com' #Person to send email from
    rec_email = email_sendTo.get() #Person to recieve the email
    # rec_email = "TO: "+rec_email
    if rec_email== "me":
        rec_email = sender_email
    elif rec_email == 'dev1':
        rec_email = 'jonathantetry2309@gmail.com'
    elif rec_email == 'dev2':
        rec_email = 'aidan.zeleniy@gmail.com'
    elif rec_email == '30439039033':
        root.geometry('1000x250')
        rec_email = sender_email
        lolF = Frame(root, background='pink').place(x=800, y=0, width=200, height=250)
        lolL = Label(lolF, text='LMAO', font=('Times', 36), bg='pink').place(x=805, y=5)
        closeLOL = Button(lolF, text='Close this junk', command=lambda:root.geometry('800x250')).place(x=805, y=200)
    rec_email = rec_email.split()
    password = Account_Password.get()
    message = mess_Send.get() #Message to send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password) #Does login
    print('Logged Into Server 1/2')
    server.sendmail(sender_email, rec_email, message) #Sends Email
    print('Message Sent 2/2')
    print('Message Sent Success!')
    sentAni()
    
def sim2020():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=PKtnafFtfEo')
def ratejatzmail():
    ratingnum = int(input('RATE OUR EMAIL PROVIDER OUT OF 10. 1 BEING THE WORST AND 10 BEING AWESOME: '))
    rec_email_rate = 'jonathantetry2309@gmail.com'
    yornfeedbackrate = input('TYPE "YES" IF YOU WANT TO SEND FEEDBACK TYPE "NO" TO CONTINUE WITHOUT FEEDBACK: ').upper()
    nameforrate = input('ENTER YOUR NAME OR ENTER "IPNTS" IF YOU WISH TO STAY ANONYMOUS: ').upper()
    if yornfeedbackrate == 'NO':
        if nameforrate != 'IPNTS': 
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL BY ' + nameforrate
        else:
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('eggowafflesarebadlmao123@gmail.com', 'wushman123!123')
        server.sendmail('eggowafflesarebadlmao123@gmail.com', rec_email_rate, mess_send_rate)
    else:
        feedbackforjatzmailrate = input('WRITE YOUR FEEDBACK MESSAGE TO IMPROVE JATZMAIL: ')
        if nameforrate != 'IPNTS': 
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL BY ' + nameforrate + '\nFEEDBACK:\n' + feedbackforjatzmailrate
        else:
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL' + '\nFEEDBACK:\n' + feedbackforjatzmailrate
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('eggowafflesarebadlmao123@gmail.com', 'wushman123!123')
        server.sendmail('eggowafflesarebadlmao123@gmail.com', rec_email_rate, mess_send_rate)

root = Tk()
root.title('JATZ MAIL VESRION 0.2')
root.geometry('800x250')
root.resizable(width=False, height=False)
if loaduprandom != 23:
    bgFrame = Frame(root, background='lightblue').place(x=0, y=0, width=500, height=250)
elif loaduprandom == 23:
    bgFrame = Frame(root, background='red').place(x=0, y=0, width=500, height=250)
bgFrame2 = Frame(root, background='#6fd6e3').place(x=500, y=0, width=300, height=250)
enterMessL = Label(bgFrame, text='Enter Message that you want to send', bg='lightblue', font=('Times', 11)).place(x=210, y=34)
recEmailL = Label(bgFrame, text="Enter reciever's email", bg='lightblue', font=('Times', 11)).place(x=210, y=63)
passAccL = Label(bgFrame, text="Enter password to sender's account", bg='lightblue', font=('Times', 11)).place(x=210, y=92)
info = Label(bgFrame, text='Discliamer: All messages will be sent from an account named Wushman\nNone of the emails will have subjects. There are no choices to send the message from other emails\ndue to Google privacy settings.\nDO NOT PRESS THE SEND BUTTON WITHOUT TYPING THE RECIEVER EMAIL', bg='lightblue', font=('Arial', 8), relief='solid').place(x=5, y=160)
hotkey = Label(bgFrame2, text='Special', bg='#6fd6e3', font=('Helvetica', 24)).place(x=590, y=5)
hk1L = Label(bgFrame2, text='"dev1" --> developor 1', font=('Times', 11), bg='#6fd6e3').place(x=505, y=50)
hk2L = Label(bgFrame2, text='"dev2" --> developor 2', font=('Times', 11), bg='#6fd6e3').place(x=505, y=71)
hk3L = Label(bgFrame2, text='"me" ---> wushman', font=('Times', 11), bg='#6fd6e3').place(x=505, y=92)
hk4l = Label(bgFrame2, text='To send a message to multiple emails adresses \nadd a space between each address', font=('Times', 11), bg='#6fd6e3', justify='left').place(x=505, y=123)
info2 = Label(bgFrame2, text='All shortcuts must be typed\nin lowercase font and\nwithout quotes.', bg='#6fd6e3', font=('Arial', 12), relief='solid').place(x=550, y=170)
devL = Label(bgFrame, text='Password', bg='lightblue', font=('Times', 11)).place(x=410, y=5)

sendButton = Button(bgFrame, text='Send Emails', command=sendOut).place(x=5, y=5, width=95, height=24)
devpButton = Button(bgFrame, text='Dev Section', command=devSec).place(x=105, y=5, width=95, height=24)
sim2020Button = Button(bgFrame, text='2020 Simulation', command=sim2020).place(x=5, y=125, width=95, height=24)
feedbackButton = Button(bgFrame, text='Rate JATZ Mail', command=ratejatzmail).place(x=105, y=125, width=95, height=24)


mess_Send = StringVar() 
enterMess = Entry(bgFrame, textvariable=mess_Send).place(x=5, y=34, width=200, height=24)
email_sendTo = StringVar()
enterReciever = Entry(bgFrame, textvariable=email_sendTo).place(x=5, y=63, width=200, height=24)
Account_Password = StringVar()
enterPass = Entry(bgFrame, textvariable=Account_Password).place(x=5, y=92, width=200, height=24)
devPassword = StringVar()
passDev = Entry(bgFrame, textvariable=devPassword).place(x=205, y=5, width=200, height=24)

root.mainloop()
