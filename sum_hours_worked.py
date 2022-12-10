from tkinter import *
from tkinter import ttk

import math

dates = []
e_hours = {'total' : 0}
m_hours = {'total' : 0}
h_hours = {'total' : 0}

def Initialization():
    dates = []
    e_hours = {'total' : 0}
    m_hours = {'total' : 0}
    h_hours = {'total' : 0}


def record():
    date = str(ent_date.get())
    dates.append(date)
    e_h, e_m = map(float, ent_e.get().split())
    m_h, m_m = map(float, ent_m.get().split())
    h_h, h_m = map(float, ent_h.get().split())

    e_hours[date]= "{:02d}시간 {:02d}분".format(int(e_h), int(e_m))
    e_hours['total'] += round(e_h + (e_m/60),1)
    m_hours[date]= "{:02d}시간 {:02d}분".format(int(m_h), int(m_m))
    m_hours['total'] += round(m_h + (m_m/60),1)
    h_hours[date]= "{:02d}시간 {:02d}분".format(int(h_h), int(h_m))
    h_hours['total'] += round(h_h + (h_m/60),1)
    toplevel = Toplevel(win)
    toplevel.geometry("1500x1000")

    frame1=Frame(toplevel, relief="solid", bd=2)
    
    txt = Text(frame1, width = 700, height = 1000)
    for date in dates:
        txt.insert(END, f"{date} : {e_hours[date]} | {m_hours[date]} | {h_hours[date]}\n")
    txt.pack()
    frame1.pack(side="left", fill="both", expand=True)
   
def calculate():
    price_e = round(e_hours['total'] * 15000,)
    price_m = round(m_hours['total'] * 20000,)
    price_h = round(h_hours['total'] * 25000,)
    total_price = round((price_e + price_m + price_h) * 0.967 ,1)
    toplevel = Toplevel(win)
    toplevel.geometry("1500x1000")
    frame2=Frame(toplevel, relief="solid", bd=2)
    
    txt2 = Text(frame2, width=700, height=1000)
    txt2.insert(1.0, '초등학생 급여 : ￦{:,}\n'.format(price_e))
    txt2.insert(2.0, '중학생 급여 : ￦{:,}\n'.format(price_m))
    txt2.insert(3.0, '고등학생 급여 : ￦{:,}\n'.format(price_h))
    txt2.insert(4.0, '월급 : ￦{:,}\n'.format(total_price))
    txt2.pack()
    frame2.pack(side="right", fill="both", expand=True)
    print('초등학생 급여 : ￦{:,}'.format(price_e))
    print('중학생 급여 : ￦{:,}'.format(price_m))
    print('고등학생 급여 : ￦{:,}'.format(price_h))
    print('월급 : ￦{:,}'.format(total_price))


    


win = Tk()
win.geometry("1000x500")
win.title("청담바름학원 시급 계산기")
win.option_add("*Font", "맑은고딕 25")

# 날짜 입력창
ent_date = Entry(win)
ent_date.config(text = "날짜")
ent_date.place(relx=0.5, rely=0.1)

# 초등시간 입력창
ent_e = Entry(win)
ent_e.config(text = "초등수업 시간")
ent_e.place(relx=0.5, rely=0.2)

# 중등시간 입력창
ent_m = Entry(win)
ent_m.get()
ent_m.place(relx=0.5, rely=0.3)

# 고등시간 입력창
ent_h = Entry(win)
ent_h.get()
ent_h.place(relx=0.5, rely=0.4)


# 기록 버튼
btn_record =Button(win)
btn_record.config(width = 3, height = 1)
btn_record.config(text = "기록")
btn_record.config(command=record)
btn_record.place(relx=0.5, rely=0.7)
# 정산 버튼
btn_cal =Button(win)
btn_cal.config(width = 3, height = 1)
btn_cal.config(text = "정산")
btn_cal.config(command=calculate)
btn_cal.place(relx=0.6, rely=0.7)
# 초기화 버튼
btn_reset = Button(win)
btn_reset.config(width = 3, height = 1)
btn_reset.config(text = "초기화")
btn_reset.config(command=Initialization)
btn_reset.place(relx=0.7, rely=0.7)

# 날짜, 초등, 중등, 고등 입력창 라벨 
label_date = Label(win, text="날짜")
label_date.place(relx=0.45, rely=0.1)
label_e = Label(win, text="초등수업시간")
label_e.place(relx=0.36, rely=0.2)
label_m = Label(win, text="중등수업시간")
label_m.place(relx=0.36, rely=0.3)
label_h = Label(win, text="고등수업시간")
label_h.place(relx=0.36, rely=0.4)

win.mainloop()