from tkinter import*
from tkinter import messagebox
import random,os,tempfile,subprocess


def clear():
     bike1Entry.insert(0,0)
     bike2Entry.insert(0,0)
     bike3Entry.insert(0,0)
     bike4Entry.insert(0,0)
     bike5Entry.insert(0,0)
     bike6Entry.insert(0,0)

     car1Entry.insert(0,0)
     car2Entry.insert(0,0)
     car3Entry.insert(0,0)
     car4Entry.insert(0,0)
     car5Entry.insert(0,0)
     car6Entry.insert(0,0)

     other1Entry.insert(0,0)
     other2Entry.insert(0,0)
     other3Entry.insert(0,0)
     other4Entry.insert(0,0)
     other5Entry.insert(0,0)
     other6Entry.insert(0,0)


     bikktaxEntry.delete(0,END)
     bikkktaxEntry.delete(0,END)
     bikkkktaxEntry.delete(0,END)



     bikkEntry.delete(0,END)
     bikkkEntry.delete(0,END)
     bikkkkEntry.delete(0,END)





def send_email():
     #if textarea.get(1.0,END)=='\n':
      #    messagebox.showerror('Error','Bill is empty')
     #else:
          root1=Toplevel()
          root1.title('send gmail')
          root1.config(bg='white')
          root1.resizable(0,0)
         
          senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
          senderFrame.grid(row=0,colume=0)

          gamilIdLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'))
          gamilIdLabel.grid(row=0,column=0)

          root1.mainloop()




def print_bill():
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty')
     else:
          file=tempfile.mktemp('.txt')
          open(file,'w').write(textarea.get(1.0,END))
          subprocess.call(['open',file])


def search_bill():
     for i in os.listdir('bills/'):
          if i.split('.')[0]==billEntry.get():
               f=open(f'bills/{i}','r')
               textarea.delete(1.0,END)
               for data in f:
                    textarea.insert(END,data)
               f.close()
               break
          else:
      
            messagebox.showerror('Error','Invalid bill number')


if not os.path.exists('bills'):
      os.mkdir('bills')

def save_bill():
      global billnumber
      result=messagebox.askyesno('confirm','Do you want to save bill?')
      if result:
            bill_content=textarea.get(1.0,END)
            file=open(f'bills/{billnumber}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('success',f'{billnumber} is saved successfully')
            billnumber=random.randint(1,1000)
billnumber=random.randint(1,1000)


def bill_area():
      if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer details are required')
      elif bikkEntry.get()=='' and bikkkEntry.get()=='' and bikkkEntry.get()=='':
        messagebox.showerror('Error','No product are selected')
      elif bikkEntry.get()=='0 Rs' and bikkkEntry.get()=='0 Rs' and bikkkkEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Product are selected')
      else:

        textarea.delete(1.0,END)

    
        textarea.insert(END,'\t\t-Fossilex Engine Oil-\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nPhone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n========================================================')
        textarea.insert(END,'\n Products\t\t\tQty\t\t\tPrice')
        textarea.insert(END,'\n========================================================\n')
        if bike1Entry.get()!='0':
              textarea.insert(END,f'15W-50 SN(6*2.5lit)\t\t\t{bike1Entry.get()}\t\t\t{bikeprice1} Rs\n')
        if bike2Entry.get()!='0':
              textarea.insert(END,f'20W-40 SM(20*1lit)\t\t\t{bike2Entry.get()}\t\t\t{bikeprice2} Rs\n')
        if bike3Entry.get()!='0':
              textarea.insert(END,f'10W-30 SL(20*800ml)\t\t\t{bike3Entry.get()}\t\t\t{bikeprice3} Rs\n')
        if bike4Entry.get()!='0':
              textarea.insert(END,f'20W-40 SL(20*1lit)\t\t\t{bike4Entry.get()}\t\t\t{bikeprice4} Rs\n')
        if bike5Entry.get()!='0':
              textarea.insert(END,f'10W-30 SM(20*900ml)\t\t\t{bike5Entry.get()}\t\t\t{bikeprice5} Rs\n')
        if bike6Entry.get()!='0':
              textarea.insert(END,f'10W-40 SN(20*1lit)\t\t\t{bike6Entry.get()}\t\t\t{bikeprice6} Rs\n')

        if car1Entry.get()!='0':
              textarea.insert(END,f'5W-30 SN(4*3.5lit)\t\t\t{car1Entry.get()}\t\t\t{carprice1} Rs\n')

        if car2Entry.get()!='0':
              textarea.insert(END,f'5W-40 SN(6*3lit)\t\t\t{car2Entry.get()}\t\t\t{carprice2} Rs\n')

        if car3Entry.get()!='0':
              textarea.insert(END,f'20W-50 SL(6*3lit)\t\t\t{car3Entry.get()}\t\t\t{carprice3} Rs\n')

        if car4Entry.get()!='0':
              textarea.insert(END,f'15W-40 CF4(5lit)\t\t\t{car4Entry.get()}\t\t\t{carprice4} Rs\n')

        if car5Entry.get()!='0':
              textarea.insert(END,f'75W-90 GL4(6*2.5lit)\t\t\t{car5Entry.get()}\t\t\t{carprice5} Rs\n')

        if car6Entry.get()!='0':
              textarea.insert(END,f'COOLANT (20*1lit)\t\t\t{car6Entry.get()}\t\t\t{carprice6} Rs\n')



        if other1Entry.get()!='0':
              textarea.insert(END,f'DOT-4 (20*250ml)\t\t\t{other1Entry.get()}\t\t\t{otherprice1} Rs\n')

        if other2Entry.get()!='0':
              textarea.insert(END,f'ATF (20*1lit)\t\t\t{other2Entry.get()}\t\t\t{otherprice2} Rs\n')

        if other3Entry.get()!='0':
              textarea.insert(END,f'UTTO (10lit)\t\t\t{other3Entry.get()}\t\t\t{otherprice3} Rs\n')

        if other4Entry.get()!='0':
              textarea.insert(END,f'80W-90 GL-4(20*1lit)\t\t\t{other4Entry.get()}\t\t\t{otherprice4} Rs\n')

        if other5Entry.get()!='0':
              textarea.insert(END,f'______\t\t\t{other5Entry.get()}\t\t\t{otherprice5} Rs\n')

        if other6Entry.get()!='0':
              textarea.insert(END,f'________\t\t\t{other6Entry.get()}\t\t\t{otherprice6} Rs\n')
              
        textarea.insert(END,'\n--------------------------------------------------------')


        if bikkEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Bike  TAX\t\t\t\t{bikktaxEntry.get()}')
        if bikkkEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Car   TAX\t\t\t\t{bikkktaxEntry.get()}')
        if bikkkkEntry.get()!='0.0 Rs':
              textarea.insert(END,f'\n Other TAX\t\t\t\t{bikkkktaxEntry.get()}\n')
        textarea.insert(END,'\n--------------------------------------------------------')

        textarea.insert(END,f'\nTotal Bill: \t\t\t\t {Totalbill}')   

        save_bill()   



def total():
    global bikeprice1,bikeprice2,bikeprice3,bikeprice4,bikeprice5,bikeprice6
    global carprice1,carprice2,carprice3,carprice4,carprice5,carprice6
    global otherprice1,otherprice2,otherprice3,otherprice4,otherprice5,otherprice6
    global Totalbill
    bikeprice1=int(bike1Entry.get())*3900
    bikeprice2=int(bike2Entry.get())*4200
    bikeprice3=int(bike3Entry.get())*5000
    bikeprice4=int(bike4Entry.get())*3800
    bikeprice5=int(bike5Entry.get())*4200
    bikeprice6=int(bike5Entry.get())*4200

    totalbikeprice=bikeprice1+bikeprice2+bikeprice3+bikeprice4+bikeprice5+bikeprice6
    bikkEntry.delete(0,END)
    bikkEntry.insert(0,f'{totalbikeprice} Rs')
    biketax=totalbikeprice*0.0
    bikktaxEntry.delete(0,END)
    bikktaxEntry.insert(0,str(biketax)+'Rs')
    

    carprice1=int(car1Entry.get())*3940
    carprice2=int(car2Entry.get())*7800
    carprice3=int(car3Entry.get())*3600
    carprice4=int(car4Entry.get())*1150
    carprice5=int(car5Entry.get())*4500
    carprice6=int(car6Entry.get())*4000

    totalcarprice=carprice1+carprice2+carprice3+carprice4+carprice5+carprice6
    bikkkEntry.delete(0,END)
    bikkkEntry.insert(0,f'{totalcarprice} Rs')
    cartax=totalbikeprice*0.0
    bikkktaxEntry.delete(0,END)
    bikkktaxEntry.insert(0,str(cartax)+'Rs')


    otherprice1=int(other1Entry.get())*3900
    otherprice2=int(other2Entry.get())*3900
    otherprice3=int(other3Entry.get())*3900
    otherprice4=int(other4Entry.get())*3900
    otherprice5=int(other5Entry.get())*3900
    otherprice6=int(other6Entry.get())*3900

    totalotherprice=otherprice1+otherprice2+otherprice3+otherprice4+otherprice5+otherprice6
    bikkkkEntry.delete(0,END)
    bikkkkEntry.insert(0,f'{totalotherprice} Rs')
    othertax=totalbikeprice*0.0
    bikkkktaxEntry.delete(0,END)
    bikkkktaxEntry.insert(0,str(othertax)+'Rs')


    Totalbill=totalbikeprice+totalcarprice+totalotherprice+biketax+cartax+othertax      
    




    

#GUI part
root=Tk()
root.title('Fossilex Engine Oil')
root.geometry('1270x685')
root.iconbitmap('')
headlingLabel=Label(root,text='Fossilex Engine Oil',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=11,relief=GROOVE)
headlingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Deatils',font=('times new roman',15,'bold'),fg='gold',bd='8',relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,bg='white',fg='black',width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,bg='white',fg='black',width=18)
phoneEntry.grid(row=0,column=3,padx=8)


billLabel=Label(customer_details_frame,text='Bill  Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billLabel.grid(row=0,column=4,padx=20,pady=2)
billEntry=Entry(customer_details_frame,font=('arial',15),bd=7,bg='white',fg='black',width=18)
billEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)


productFrame=Frame(root)
productFrame.pack()


BikeOilFrame=LabelFrame(productFrame,text='Bike Oil',font=('times new roman',15,'bold'),fg='gold',bd='8',relief=GROOVE,bg='gray20')
BikeOilFrame.grid(row=0,column=0)

bike1Label=Label(BikeOilFrame,text='B 15W-50 SN(2.5lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike1Label.grid(row=0,column=0,pady=9)
bike1Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike1Entry.grid(row=0,column=1,pady=9)
bike1Entry.insert(0,0)


bike2Label=Label(BikeOilFrame,text='20W-40 SM(1lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike2Label.grid(row=1,column=0,pady=9)
bike2Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike2Entry.grid(row=1,column=1,pady=9)
bike2Entry.insert(0,0)

bike3Label=Label(BikeOilFrame,text='10W-30 SL/MB(800ml)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike3Label.grid(row=2,column=0,pady=9)
bike3Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike3Entry.grid(row=2,column=1,pady=9)
bike3Entry.insert(0,0)

bike4Label=Label(BikeOilFrame,text='20W-40 SL(1Lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike4Label.grid(row=3,column=0,pady=9)
bike4Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike4Entry.grid(row=3,column=1,pady=9)
bike4Entry.insert(0,0)

bike5Label=Label(BikeOilFrame,text='10W-30 SM(900ml)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike5Label.grid(row=4,column=0,pady=9)
bike5Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike5Entry.grid(row=4,column=1,pady=9)
bike5Entry.insert(0,0)

bike6Label=Label(BikeOilFrame,text='10W-40 SN(1lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bike6Label.grid(row=5,column=0,pady=9)
bike6Entry=Entry(BikeOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bike6Entry.grid(row=5,column=1,pady=9)
bike6Entry.insert(0,0)



CarOilFrame=LabelFrame(productFrame,text='Car Oil',font=('times new roman',15,'bold'),fg='gold',bd='8',relief=GROOVE,bg='gray20')
CarOilFrame.grid(row=0,column=1)

car1Label=Label(CarOilFrame,text='5W-30 F/SN(3.5lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car1Label.grid(row=0,column=0,pady=9,padx=10)
car1Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car1Entry.grid(row=0,column=1,pady=9,padx=10)
car1Entry.insert(0,0)


car2Label=Label(CarOilFrame,text='5W-40 F/SN(3lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car2Label.grid(row=1,column=0,pady=9,padx=10)
car2Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car2Entry.grid(row=1,column=1,pady=9,padx=10)
car2Entry.insert(0,0)


car3Label=Label(CarOilFrame,text='20W-50 SL(3lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car3Label.grid(row=2,column=0,pady=9,padx=10)
car3Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car3Entry.grid(row=2,column=1,pady=9,padx=10)
car3Entry.insert(0,0)

car4Label=Label(CarOilFrame,text='15W-40 CF4(5lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car4Label.grid(row=3,column=0,pady=9,padx=10)
car4Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car4Entry.grid(row=3,column=1,pady=9,padx=10)
car4Entry.insert(0,0)

car5Label=Label(CarOilFrame,text='75W-90 GL5(2.5lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car5Label.grid(row=4,column=0,pady=9,padx=10)
car5Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car5Entry.grid(row=4,column=1,pady=9,padx=10)
car5Entry.insert(0,0)

car6Label=Label(CarOilFrame,text='COOLANT(1lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
car6Label.grid(row=5,column=0,pady=9,padx=10)
car6Entry=Entry(CarOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
car6Entry.grid(row=5,column=1,pady=9,padx=10)
car6Entry.insert(0,0)


OtherOilFrame=LabelFrame(productFrame,text='Other Oil',font=('times new roman',15,'bold'),fg='gold',bd='8',relief=GROOVE,bg='gray20')
OtherOilFrame.grid(row=0,column=2)

other1Label=Label(OtherOilFrame,text='DOT-4 (250ml)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other1Label.grid(row=0,column=0,pady=9,padx=10)
other1Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other1Entry.grid(row=0,column=2,pady=9,padx=10)
other1Entry.insert(0,0)

other2Label=Label(OtherOilFrame,text='ATF (1lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other2Label.grid(row=1,column=0,pady=9,padx=10)
other2Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other2Entry.grid(row=1,column=2,pady=9,padx=10)
other2Entry.insert(0,0)

other3Label=Label(OtherOilFrame,text='UTTO (10lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other3Label.grid(row=2,column=0,pady=9,padx=10)
other3Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other3Entry.grid(row=2,column=2,pady=9,padx=10)
other3Entry.insert(0,0)

other4Label=Label(OtherOilFrame,text='80W-90 GL4(1lit)',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other4Label.grid(row=3,column=0,pady=9,padx=10)
other4Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other4Entry.grid(row=3,column=2,pady=9,padx=10)
other4Entry.insert(0,0)

other5Label=Label(OtherOilFrame,text='',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other5Label.grid(row=4,column=0,pady=9,padx=10)
other5Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other5Entry.grid(row=4,column=2,pady=9,padx=10)
other5Entry.insert(0,0)

other6Label=Label(OtherOilFrame,text='',font=('times new roman',15,'bold'),bg='gray20',fg='white')
other6Label.grid(row=5,column=0,pady=9,padx=10)
other6Entry=Entry(OtherOilFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
other6Entry.grid(row=5,column=2,pady=9,padx=10)
other6Entry.insert(0,0)

bill1frame=Frame(productFrame,bd=8,relief=GROOVE)
bill1frame.grid(row=0,column=3)

billareaLabel=Label(bill1frame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)


Scrollbar=Scrollbar(bill1frame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)


textarea=Text(bill1frame,height=22,width=56,bg='white',fg='black',yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)



billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',16,'bold'),fg='gold',bd='8',relief=GROOVE,bg='gray20')
billmenuFrame.pack()

bikkLabel=Label(billmenuFrame,text='Bike-Oil Price',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikkLabel.grid(row=0,column=0,pady=9,padx=10)
bikkEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bg='white',fg='black',bd='5')
bikkEntry.grid(row=0,column=1,pady=9,padx=10)

bikkkLabel=Label(billmenuFrame,text='Car-Oil Price',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikkkLabel.grid(row=1,column=0,pady=9,padx=10)
bikkkEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bikkkEntry.grid(row=1,column=1,pady=9,padx=10)

bikkkkLabel=Label(billmenuFrame,text='Other-Oil Price',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikkkkLabel.grid(row=2,column=0,pady=9,padx=10)
bikkkkEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bg='white',fg='black',bd='5')
bikkkkEntry.grid(row=2,column=1,pady=9,padx=10)



bikktaxLabel=Label(billmenuFrame,text='Bike-Oil Tax',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikktaxLabel.grid(row=0,column=2,pady=9,padx=10)
bikktaxEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bg='white',fg='black',bd='5')
bikktaxEntry.grid(row=0,column=3,pady=9,padx=10)

bikkktaxLabel=Label(billmenuFrame,text='Car-Oil Tax',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikkktaxLabel.grid(row=1,column=2,pady=9,padx=10)
bikkktaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bg='white',fg='black',bd='5')
bikkktaxEntry.grid(row=1,column=3,pady=9,padx=10)

bikkkktaxLabel=Label(billmenuFrame,text='Other-Oil Tax',font=('times new roman',16,'bold'),bg='gray20',fg='white')
bikkkktaxLabel.grid(row=2,column=2,pady=9,padx=10)
bikkkktaxEntry=Entry(billmenuFrame,font=('times new roman',16,'bold'),width=10,bg='white',fg='black',bd='5')
bikkkktaxEntry.grid(row=2,column=3,pady=9,padx=10)



buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='black',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=32,padx=17)


billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='black',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=32,padx=17)


emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='black',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=32,padx=17)


printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='black',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=32,padx=17)


clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='black',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=32,padx=17)







root.mainloop()