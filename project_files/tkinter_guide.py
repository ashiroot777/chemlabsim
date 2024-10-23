from tkinter import *

 #The Tk() function creates the main window that appears on the screen.
 #here root is a container for all our widgets
root = Tk()

# mainloop() method is used to start the event loop, 
# which listens for user inputs (like button clicks or key presses) and updates the GUI accordingly.
#note USE THIS FUNCTION AT THE END TO START THE PROGRAM!!!

#This window can be customized with a title, size, and other attribute using root.<func>(<customisation>)
root.title("ashritha is trying")
root.geometry("300x300")

#Label is a widget used to display text or images in the GUI
#syntax: label = label(master,text = '',etc...)
#here master is the parent window
label = Label(root, text='wow ashritha you are amazing',font=('Arial',16),fg='black')
#while using Label just outside bracket make sure L is capital

#use pady in the following way 
#here, it Packs the label into the window with 20 pixels of padding vertically
label.pack(pady=20) 


button = Button(root,text='kill program',fg='blue',width=25,command=root.destroy)
button.pack(pady=20)
mainloop()