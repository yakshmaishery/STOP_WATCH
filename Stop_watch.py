from tkinter import *
import threading
import time
# functions
def resizes(*args):
    try:
        # main label
        mly=int(ML.winfo_height())
        mlx=int(ML.winfo_width())
        sizes=int((mlx+mly)/12)
        ML.config(font=("arial",sizes,"bold"))
        # hrs mins secs
        hms_x=int(Hrs.winfo_width())
        hms_y=int(Hrs.winfo_height())
        sizes1=int((hms_x+hms_y)/6)
        Hrs.config(font=("arial",sizes1,"bold","underline"))
        Mins.config(font=("arial",sizes1,"bold","underline"))
        Sec.config(font=("arial",sizes1,"bold","underline"))
        # hrs mins secs labels
        hms_x_label=int(Sec_label.winfo_width())
        hms_y_label=int(Sec_label.winfo_height())
        sizes2=int((hms_x_label+hms_y_label)/10)
        Hrs_label.config(font=("arial",sizes2,"bold"))
        Mins_label.config(font=("arial",sizes2,"bold"))
        Sec_label.config(font=("arial",sizes2,"bold"))
    except:
        pass
    pass
startpoint=True
def clockwork(*args):
    try:
        h=0
        m=0
        s=0
        while startpoint:
            s=s+1
            if s>59:
                s=0
                m=m+1
            if m>59:
                m=0
                h=h+1
            Hrs.config(text=f"{h}".zfill(2))
            Mins.config(text=f"{m}".zfill(2))
            Sec.config(text=f"{s}".zfill(2))
            time.sleep(0.9)
    except:
        pass
    pass
def starts(*args):
    try:
        global startpoint
        startpoint=True
        threading.Thread(target=clockwork).start()
    except:
        pass
    pass
def stop(*args):
    try:
        global startpoint
        startpoint=False
    except:
        pass
    pass
def restarts(*args):
    try:
        global startpoint
        startpoint=False
        Hrs.config(text="00")
        Mins.config(text="00")
        Sec.config(text="00")
    except:
        pass
    pass
def closing(*args):
    try:
        global startpoint
        startpoint=False
        root.destroy()
    except:
        pass
    pass
root=Tk()
root.title("Stop Watch")
root.config(bg="#999999",borderwidth=1,relief=SOLID)
root.protocol("WM_DELETE_WINDOW",closing)
root.geometry("300x300+500+200")
# main frame
MainFrame=Frame(root,highlightthickness=1,highlightcolor="yellow",highlightbackground="yellow",padx=4,pady=4,bg="#282722")
for i in range(3):
    MainFrame.columnconfigure(i,weight=1)
for i in range(4):
    MainFrame.rowconfigure(i,weight=1)
# main label
ML=Label(MainFrame,text="Stop Watch",font=("arial",20,"bold"),bg="#8000ff",fg="yellow")
ML.grid(row=0,columnspan=3,sticky="nswe",padx=2,pady=2)
# hours
Hrs=Label(MainFrame,text="00",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Hrs.grid(row=1,column=0,sticky="nswe",padx=2,pady=2)
# Minutes
Mins=Label(MainFrame,text="00",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Mins.grid(row=1,column=1,sticky="nswe",padx=2,pady=2)
# Seconds
Sec=Label(MainFrame,text="00",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Sec.grid(row=1,column=2,sticky="nswe",padx=2,pady=2)
# hours label
Hrs_label=Label(MainFrame,text="Hours",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Hrs_label.grid(row=2,column=0,sticky="nswe",padx=2,pady=2)
# Minutes label
Mins_label=Label(MainFrame,text="Minutes",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Mins_label.grid(row=2,column=1,sticky="nswe",padx=2,pady=2)
# Seconds label
Sec_label=Label(MainFrame,text="Seconds",font=("arial",40,"bold"),bg="#8000ff",fg="yellow")
Sec_label.grid(row=2,column=2,sticky="nswe",padx=2,pady=2)
# Start Button
StartButton=Button(MainFrame,text="Start",font=("arial",20,"bold"),borderwidth=0,cursor="hand2",command=starts,bg="yellow",fg="#8000ff")
StartButton.grid(row=3,column=0,padx=2,pady=2,sticky="nswe")
# Stop Button
StopButton=Button(MainFrame,text="Stop",font=("arial",20,"bold"),borderwidth=0,cursor="hand2",command=stop,bg="yellow",fg="#8000ff")
StopButton.grid(row=3,column=1,padx=2,pady=2,sticky="nswe")
# Restart Button
RestartButton=Button(MainFrame,text="Reset",font=("arial",20,"bold"),borderwidth=0,cursor="hand2",command=restarts,bg="yellow",fg="#8000ff")
RestartButton.grid(row=3,column=2,padx=2,pady=2,sticky="nswe")

MainFrame.pack(fill=BOTH,expand=True,padx=4,pady=4)

root.bind("<Configure>",resizes)
root.bind("<Return>",starts)
root.mainloop()