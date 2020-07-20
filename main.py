import requests                                      # used to send all kinds of http requests.The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
from tkinter import *                                # for the GUI
from tkinter.messagebox import showinfo, showerror   #For showing success or error messages


def send_sms(number, mssg):
    try:
        url = 'https://www.fast2sms.com/dev/bulk'      # the http request url

        #creating the params variable for the required parameters as specified by fast2sms for GET method
        params = { 'authorization' : 'nkIOqzY01wU53WRyQtg8sJrTudpcEjeP4XDZN2MSKa9GxflBbmERUHWB9QGgIkCPx3Vupfc1sMh6yq2X',  #API KEY
                  'sender_id': 'FSTSMS',
                  'message': mssg,
                   'language': 'english',
                   'route': 'p',
                   'numbers': number,   #can give multiple numbers separated by comma
                   'flash':'1'          #1 for flash message, 0 for normal message
        }

        response = requests.get(url, params=params)      #this will be the response
        dict = response.json()                     # this will create a dictionary of the response object which HTTP request returns
        print(dict)
        return dict.get('return')    #extracting the return parameter from the dictionary created in prev line
    except:
        print('Some error occured')



#Function for the action when button gets clicked
def button_click():
    number = textNumber.get()              # returns the value of textNumber variable
    message = textMessage.get('1.0', END)   # from the first text till the end
    r = send_sms(number, message)         # here we will get the value for the request key in the dictionary
    if r==True:
        showinfo('SUCCESS', 'SUCCESSFULLY SENT')
    else:
        showerror('ERROR', 'Something went wrong')


#creating the GUI
window = Tk()                       #creating object of Tk class
window.title('Message Sender')      #Setting title of GUI
window.geometry('400x550')          #size of GUI
font = ('Helvetica' , 16, 'bold')   # (Font family, font size, font style)

#Field for adding number
textNumber = Entry(window, font=font)            #Entry class allows only one line of text field
textNumber.pack(fill=X, padx = 20, pady = 20)

#Field for adding message
textMessage = Text(window)                        #Text class allows to write multiple line
textMessage.pack(fill=X, padx = 20, pady = 20)

#Button to send message
sendButton = Button(window, text = 'Send', command = button_click)        #Button class creates button
sendButton.pack()

window.mainloop()           # running the window


