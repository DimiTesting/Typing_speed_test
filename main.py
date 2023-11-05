from tkinter import *
import math

reps = 0
WORK_MIN = 1
timer = None


def stop_timer():
    window.after_cancel(timer)
    seconds = int(timer.replace("after#", ""))
    result = round((60*5)/seconds)
    text = f"It took you {seconds} seconds for 5 words, your average speed is {result} words per minute"
    print(text)


def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    count_down(work_sec)

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()


def start():

    word = entry.get()

    if word in text:
        print("True")
        entry.delete(0, 100)
    else:
        print("False")
        entry.delete(0, 100)


#Not finished GUI

window = Tk()
window.title("Typing speed test")
window.config(padx=100, pady=100)

canvas = Canvas(width=50, height=20)
timer_text = canvas.create_text(25, 10, text="00:00")
canvas.grid(column=0, row=0)

start_timer = Button(text="Start timer", command=start_timer)
start_timer.grid(column=1, row=4)

stop_timer = Button(text="Stop timer", command=stop_timer)
stop_timer.grid(column=2, row=4)

starting_text = Label(text="Please insert words you see from below:")
starting_text.grid(column=0, row=1)

text = "first second third forth fifth"

msg = Message(window, text=text, width=200)
msg.grid(column=0, row=2)

entry = Entry(width=40)
entry.grid(column=0, row=3)

enter = Button(text="Enter", command=start)
enter.grid(column=0, row=4)

word = entry.get()

window.mainloop()

