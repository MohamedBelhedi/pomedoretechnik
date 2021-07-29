from tkinter import  *
import math
from tkinter import messagebox as mb
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
HACK="#2700–27BF "
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    fenster.after_cancel(mein_label_Text_1)
    canvas.itemconfig(timer_text, text="00:00")
    mein_label_Text_1.config(text="Zeit")
    mein_label_Text_4.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def star_time():
    global reps
    reps += 1

    work_sec = WORK_MIN* 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        mein_label_Text_1.config(text="Gr.Pause", fg=RED)
        große_pause()
    # elif countdown(work_sec)<=5:
    #      achtung()

    elif reps % 2==0:
        countdown(short_break_sec)
        mein_label_Text_1.config(text="irgendwas eintippen ", fg=PINK)
        kleine_pause()


    else:
        countdown(work_sec)
        mein_label_Text_1.config(text="irgendwas eintippen", fg=RED)
        aufpassen()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min=math.floor(int(count/ 60))
    count_sec=count%60
    if count_sec<10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    # if count_min >=5:
    #     achtung()
    #     fenster.after(1000,countdown)





    if count>0:
     fenster.after(1000, countdown, count - 1)



    else:
        star_time()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        mein_label_Text_4.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

fenster=Tk()
fenster.title("Lernen nach der Tomaten Technik")
fenster.minsize(height=200,width=300)
fenster.config(padx=100, pady=50,bg=GREEN)


canvas=Canvas(width=200, height=230,bg=GREEN, highlightthickness=0)
canvas.grid(column=1,row=1)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=tomato_image )

timer_text=canvas.create_text(102,130,text="00:00",fill="white", font=("Narrow",30,"bold"))
canvas.grid(column=1,row=1)
mein_label_Text_1=Label(text="Zeit",bg=GREEN,font=("Narrow",30,"bold"))
mein_label_Text_1.grid(column=1,row=0)


# input_feld=Entry(int())


# input_feld.grid(column=3,row=4)
mein_label_Text_2=Button(text="Start",font=("Narrow",12,"bold"),command=star_time)#start_timer
mein_label_Text_2.grid(column=0,row=2)
mein_label_Text_3=Button(text="Reset",font=("Narrow",12,"bold"),command=reset_timer)
mein_label_Text_3.grid(column=3,row=2)
mein_label_Text_4=Label(text="",fg=RED,bg=GREEN,font=("Narrow",12,"bold"),highlightthickness=0)
mein_label_Text_4.grid(column=1,row=4)




def aufpassen():
    mb.showinfo(title="Achtung",message="Los geht es nicht wundern die Uhrzeit ist um 5 min verkürzt für die Zusammenfassung am Ende +5 min")
def achtung ():
    mb.showinfo(title="Achtung",message="Zeit fast um")
    # fenster(1000, countdown)




def kleine_pause():
    mb.showinfo(title="Achtung",message="Zusammen fassen und auf das Buch verweisen verabschieden")
def große_pause():
    mb.showinfo(title="Stop",message="Bitte eine Große Pause mache, an die frische Luft bitte")








# from tkinter import messagebox as mb
#
# def answer():
#     mb.showerror("Answer", "Sorry, no answer available")
#
# def callback():
#     if mb.askyesno('Verify', 'Really quit?'):
#         mb.showwarning('Yes', 'Not yet implemented')
#     else:
#         mb.showinfo('No', 'Quit has been cancelled')
#
# tk.Button(text='Quit', command=callback).pack(fill=tk.X)
# tk.Button(text='Answer', command=answer).pack(fill=tk.X)
#
#






fenster.mainloop()