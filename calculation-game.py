from tkinter import *
import tkinter.messagebox as msg
import random

# make the calculater game In which the user press Enter for start game. when the game start the time is also start there is the max 60 seconds
# There is the two number with +,-,*,% sings and the Entey wigit the user Enter the number which is calcualte the two number if the calculation
# is right then the score is impliment by 1 point if it is wrong calculation then the score is decriment by 1...


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x230')
        self.name = 'Welcome to Calculation Game'
        self.Count = 0
        self.title('Calculater Game...')
        self.Sign = StringVar()
        self.Count1 = 0
        self.new_Name1 = ''
        self.name1 = 'Press Enter to Contiune...'

        # self.resizable(0, 0)
        self.new_Name = ''
        self.introLabel = Label(self, text='', font='arial 20 bold')
        self.introLabel.place(x=38, y=10)

        self.l1 = Label(self,text='',font='red')
        self.l1.place(x=152,y=150)

        
        self.l2 = Label(self,text='',font='red')
        self.l2.place(x=150,y=150)
        
        self.Count3 = 0
        self.new_Name3 = ''
        self.name3 = 'Please Enter the Vaild Sign...'
        self.randomNumber_End = 100
        self.randomNumber_Start = 5
        self.Plus_Output = StringVar()
        self.Plus_Output.set(0)

        self.number1 = random.randint(1,20)
        self.number2 = random.randint(1,30)
        self.score = 0

        self.Count4 = 0
        self.Name4 = 'Enter To Start the Game...'
        self.New_Name4 = ''
        self.L4 = Label(self,text='',font='default 12 bold')
        self.L4.place(x=150,y=200)




        # Now Build Some Code...
        # lets take the break...
        # well went to code this project

    def introduction(self):
        if self.Count >= len(self.name):
            self.Count = -1
            self.new_Name = ''
            self.introLabel.config(text=self.new_Name)

        else:
            self.new_Name += self.name[self.Count]
            self.introLabel.config(text=self.new_Name)

        self.Count += 1
        self.introLabel.after(50, self.introduction)


    def main(self):
        global E1, L1
        __K = Label(self,text='---------------------------------------------------------------------------',font='arial 13')
        __K.place(x=22,y=45)
        L1 = Label(self,text='Enter the Sigh of Calcutation :- ',font='arial 16 bold')
        L1.place(x=20,y=70)
        E1 = Entry(self,textvariable=self.Sign,width=1,font='courier 14 bold')
        E1.place(x=250,y=103)
        E1.focus()
        self.bind('<Return>',self.LogicFunc) # if you want to add time function in this calculation game then '<Return>',self.LogicFunc' call the another fuction called time Start...

    def LogicFunc(self,event):
        global E1
        # print('well...')
        if self.Sign.get() == '+':
            self.PlusFuction()

        elif self.Sign.get() == '-':
            self.LessFuction()
        
        elif self.Sign.get() == '*':
            self.MultiplyFuction()
        
        elif self.Sign.get() == '/':
            self.DivideFuction()
        
        else:
            print('right...')
            msg.showerror('Error','Please enter the valid Canculation sign :-\n (+), (-), (*), (/)')
            E1.delete(0,END)
         
        
    def degin(self):
        global E1
        if self.Count1 > len(self.name1):
            self.new_Name1 = ''
            self.l1.config(text='')
            self.Count1 = -1

        else:
            self.new_Name1 += self.name1[:self.Count1]
            self.l1.config(text=self.new_Name1,fg='red',font='default 12 bold')
            
        
        self.Count1 += 27
        self.l1.after(500,self.degin)

    def degin2(self):
        if self.Count4 > len(self.Name4):
            self.New_Name4 = ''
            self.Count4 = -1
            self.L4.config(text=self.New_Name4)

        else:
            self.New_Name4 += self.Name4[:self.Count4]
            self.L4.config(text=self.New_Name4)

        self.Count4 += 23
        self.L4.after(200,self.degin2)


    def PlusFuction(self):
        global number_1, number_2,Number1Label,Plus_LabelL,Plus_Label1, score

        L1.place(x=324234,y=324324)
        E1.place(x=324234,y=432342)
        self.l1.place(x=4534534,y=342342342)

        info = Label(self,text='Enter The Correct Answer By Your Calculation :-',font='default 12 bold')
        info.place(x=40,y=80)

        F1 = Frame(self,bg='grey',borderwidth=3)
        F1.pack(side=BOTTOM, padx=10, pady=40, anchor='e',fill=X)


        F2 = Frame(F1,bg='black',borderwidth=5,width=16)
        F2.pack(side=LEFT,padx=10,pady=3)

        Number1Label = Label(F2, text=f'-----',font='default 19 bold',bg='grey')
        Number1Label.grid(row=1,column=1)

        F3 = Frame(F1,bg='black',borderwidth=5,width=16)
        F3.pack(side=LEFT,padx=30,pady=3)
        
        Plus_Label = Label(F3, text=f'{self.Sign.get()}',font='default 19 bold',fg='white',bg='grey')
        Plus_Label.grid(row=1,column=1)

        F4 = Frame(F1,bg='black',borderwidth=5,width=16)
        F4.pack(side=LEFT,padx=10,pady=3)

        Plus_LabelL = Label(F4, text=f'-----',font='default 19 bold',bg='grey')
        Plus_LabelL.grid(row=1,column=1)

        F5 = Frame(F1,bg='black',borderwidth=5,width=16)
        F5.pack(side=LEFT,padx=10,pady=3)

        Plus_Label = Label(F5, text=f'=',font='default 19 bold',bg='grey',fg='white')
        Plus_Label.grid(row=1,column=1)

        F6 = Frame(F1,bg='black',borderwidth=5,width=16)
        F6.pack(side=LEFT,padx=10,pady=3)

        Plus_Label1 = Entry(F6,font='default 19 bold',textvariable=self.Plus_Output,bg='white',fg='black',width=6)
        Plus_Label1.grid(row=1,column=1)
        Plus_Label1.focus()

        score = Label(self,text='',font='default 12 bold')
        score.place(x=150,y=200)
        self.degin2()

        self.bind('<Return>',self.Plus_F)


    def Plus_F(self,event):
        self.L4.place(x=32424,y=43234)

        print(f'before - {self.number1+self.number2}')

        if int(self.Plus_Output.get()) == int(self.number2+self.number1):
            print('yes its work')
            print(self.number1+self.number2)
            self.score += 1
            

        score.config(text=f'Score ---- {self.score}')
        Plus_Label1.delete(0,END)
        self.number3 = random.randint(1,20)
        self.number4 = random.randint(1,30)
        
        Number1Label.config(text=f'{self.number3}')
        Plus_LabelL.config(text=f'{self.number4}')
        
        self.number1 = self.number3
        self.number2 = self.number4
        print(f'Total {self.number1+self.number2}')


if __name__ == "__main__":
    main = GUI()
    main.introduction()
    main.main()
    main.degin()

    main.mainloop()