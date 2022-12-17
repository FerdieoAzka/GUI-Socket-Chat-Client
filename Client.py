import socket
from threading import *
from tkinter import *


s = socket.socket()

hostIp = "10.6.135.93"
portNumber = 2000

s.connect((hostIp, portNumber))

window = Tk()
window.title("Connected To: " + hostIp + ":"+str(portNumber))

txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

user_name = Label(window, text="Username").grid(
    row=1, column=0, padx=1, pady=1)

username = Entry(window, width=50)
username.grid(row=2, column=0, padx=10, pady=10)

user_name = Label(window, text="Messages").grid(
    row=3, column=0, padx=1, pady=1)

txtYourMessage = Entry(window, width=50)
txtYourMessage.grid(row=4, column=0, padx=10, pady=10)


def sendMessage():
    _username = username.get()
    _username += " : "
    clientMessage = txtYourMessage.get()
    txtMessages.insert(END, "\n" + _username + clientMessage)
    s.send((_username+clientMessage).encode())


btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=5, column=0, padx=10, pady=10)


def recvMessage():
    while True:
        serverMessage = s.recv(1024).decode()
        print(serverMessage)
        txtMessages.insert(END, "\n"+serverMessage)


recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()


window.mainloop()
