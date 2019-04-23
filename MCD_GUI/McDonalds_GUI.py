
from Tkinter import *
from random import choice
import io
import smtplib
from email.mime.text import MIMEText

#Node Class Declared
class Node(object):

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

#Class Declared For Queue and enqueue and de-queue methods

class Queue(object):

    def __init__(self,front=None,rear=None):
        self.front = None
        self.rear = None

#En-queue declared for adding the Back

    def enqueue(self,data):
        NewNode = Node(data)

        if self.front==None and self.rear==None:
            self.front=self.rear=NewNode
            return

        temp = self.front
        c = 0
        max = NewNode.data[1]
        while temp!=self.rear:
            if temp.data[1]>max:
                current = temp
                c = c+1
                temp=temp.next    
                continue

            elif c == 0:
                NewNode.next=self.front
                self.front=NewNode
                print("New Customer Order Placed Successfully")
                return

            else:
                current.next=NewNode
                NewNode.next=temp
                print("New Customer Order Placed Successfully")
                return

        if self.front==self.rear:
            if self.front.data[1]>max:
                self.front.next=NewNode
                self.rear=NewNode
                print("New Customer Order Placed Successfully")
                return

            else:
                NewNode.next=self.front
                self.front=NewNode
                print("New Customer Order Placed Successfully")
                return

        if temp== self.rear:
            if temp.data[1]<max:
                current.next=NewNode
                NewNode.next=temp
                print("New Customer Order Placed Successfully")
                return

            elif self.rear.data[1] >max:
                self.rear.next=NewNode
                self.rear=NewNode
                print("New Customer Order Placed Successfully")
                return

#De-queue method declared to delete from front

    def dequeue(self):
        current=self.front
        if self.front==None:
            print("No Customer")  #Queue Empty                   
            return

        if self.front==self.rear:
            self.front=self.rear=None
            print ("Customer Deleted Successfully")
        else:
            self.front=self.front.next
            print("Customer Deleted Successfully") 

#Method to display all customer and orders

    def display(self):
        front1 = self.front
        if ((front1==None) and (self.rear==None)):
            print("No Customers")
            return
        print("Customer Name  \t Customer Order Priority") 

        while(front1!=self.rear):
            print ("Customer Name",front1.data[0],"Customer Order Priority",front1.data[1])
            front1 = front1.next

        if (front1==self.rear):
            print("Customer Name",front1.data[0],"Customer Order Priority",front1.data[1])


"""
GUI Code HERE
"""
top = Tk()
top.title("My Burger Shop")
top.geometry("500x500")
top.configure(background='orange')

"""
top.grid_rowconfigure(1,weight=1)
top.grid_rowconfigure(2,weight=1)
top.grid_columnconfigure(0,weight=1)
top.grid_columnconfigure(2,weight=1)
"""

 
ll = Label(top,text="Welcome To My Burger Pune",font=('Times New Roman ',18,'bold'),foreground='red')

l1 = Label(top,text="Please select type of burger",font=('Times New Roman',14,'bold'),foreground='red')

def save_info():
   customer_name_info = customer_name.get()
   customer_priority_info = customer_priority.get()
   customer_priority_info = str(customer_priority_info)
   customer_email_info = customer_email.get()
   print str(customer_name_info)
   print str(customer_priority_info) 
   print str(customer_email_info)

   file = open("user.text","w")
   file.write(customer_name_info)
   file.write(customer_priority_info)
   file.write(customer_email_info)
   file.close()
   print("Customer",customer_name_info,"Order is placed will get shortly...!!!")

def send_email():
    customer_email = StringVar()

    msg = MIMEText('Welcome to My Burger Shop Alandi')
    msg['Subject']='Burger Order Confirmation'
    msg['From']='kedar@mitaoe.ac.in'     
    msg['To']=customer_email
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login(msg['From'],'kedar1023')

    s.sendmail(msg['From'],[msg['To']],msg.as_string())
    print('Sending Mail.......................................')

    s.quit()


   



customer_name = StringVar()
customer_priority = IntVar()
customer_email = StringVar()

def details():

    top1 = Toplevel(top)
    top1.title("Welcome To My Burger Shop")
    top1.geometry("500x500")
    top1.configure(background='orange') #Background color given
    l3 = Label(top1,text="Enter Customer Details Here...",font=('Times New Roman',14,'bold')).pack()
    l4 = Label(top1,text="Enter Customer Name").pack()
    t1 = Entry(top1,textvariable=customer_name,font=('Calibri',13)).pack()
    l5 = Label(top1,text="Enter Customer Priority").pack()
    t2 = Entry(top1,textvariable=customer_priority).pack()
    l6 = Label(top1,text="Enter Customer Email").pack()
    t3 = Entry(top1,textvariable=customer_email).pack()
    #SpinBox declared
   
    b3 = Button(top1,text="OK!Done!",command=save_info).pack()

w = Spinbox(top,from_=0,to=10)

b1 = Button(top,text="Place Order",command=details)

lb1 = Listbox(top,width=40)
lb1.insert(1,"Veg Burger            Price--60")
lb1.insert(2,"Veg Aloo Tikki Burger Price--80")
lb1.insert(3,"McVeggie              Price--120")
lb1.insert(4,"Panner Salsa Wrap     Price--140")
lb1.insert(5,"Veg McCurry Pan       Price--170")
lb1.insert(6,"Pizza McPuff          Price--150")
lb1.insert(7,"Chicken Maharaj Mac   Price--200")
lb1.insert(8,"McChicken             Price--250")
lb1.insert(9,"Chicken McGrill       Price--300")
lb1.insert(10,"Chicken McCurry Pan  Price--450")

ll.pack()#Heading label

l1.pack() #Select type of burger label
lb1.pack() #Listbox 
w.pack() #SpinBoox
b1.pack() #Place order button

top.mainloop() #Frame added



