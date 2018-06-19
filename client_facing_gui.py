from tkinter import *
import speech_to_text as stt

root = Tk()
root.title('MediQ')
root.geometry('600x500')

def click():
    respond = stt.start_conversation()
    response = Label(root, text = respond,font = "none 12 bold", wraplength=root.winfo_width() // 1.5)
    response.pack()


def window(main):
    main.title("MediQ")
    main.update_idletasks()
    width = main.winfo_width()
    height = main.winfo_height()
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height //2)
    main.geometry('{}x{}+{}+{}'.format(width,height,x,y))

# ADD Widgets here
text = Label(root, text = "Xiao Bai GUI on Python",font="none 12 bold")
button = Button(root, text = "", width = 20,height = 10, anchor = CENTER, command = click)



window(root)
text.pack()
button.pack()
root.mainloop()
