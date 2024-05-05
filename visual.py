# модуль visual.py будет отвечать за отрисовку gui, logic.py - за логику: высчитывание ответа

import logic  # подключаем наш модуль logic
import customtkinter as ctk  # подключаем модуль customtkinter



def show_window_1():
    global lbl_start_message, entry_input, btn_done, score
    rows, columns = 4, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)

    score.grid(row=0, column=0, ipadx=0, ipady=4, padx=20, pady=20, sticky="nwes")
    lbl_start_message.grid(row=1, column=0, ipadx=4, ipady=4, padx=100, pady=100, sticky="nwes")
    entry_input.grid(row=2, column=0, ipadx=4, ipady=4, padx=500, pady=100, sticky="nsew")
    btn_done.grid(row=3, column=0,ipadx=4, ipady=4, padx=600, pady=100, sticky="nsew")

def show_window_2():
    global lbl_true_message, btn_ttn
    rows, columns = 2, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)


    lbl_true_message.grid(row=0, column=0, ipadx=4, ipady=4, padx=500, pady=150, sticky="nsew")
    btn_ttn.grid(row=1, column=0, ipadx=4, ipady=4, padx=650, pady=200, sticky="nsew")

def show_window_3():
    global lbl_false_message, btn_unttn
    rows, columns = 2, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=1)
    for i in range(columns):
        root.columnconfigure(index=i, weight=1)

    lbl_false_message.grid(row=0, column=0, ipadx=4, ipady=4, padx=500, pady=150, sticky="nsew")
    btn_unttn.grid(row=1, column=0, ipadx=4, ipady=4, padx=650, pady=200, sticky="nsew")

def forget_window_1():
    global lbl_start_message, entry_input, btn_done
    lbl_start_message.grid_forget()
    entry_input.grid_forget()
    btn_done.grid_forget()
    score.grid_forget()
    rows, columns = 4, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)

def forget_window_2():
    global lbl_true_message, lbl_start_message, btn_ttn
    lbl_true_message.grid_forget()
    lbl_start_message.grid_forget()
    btn_ttn.grid_forget()

    rows, columns = 2, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)

def forget_window_3():
    global lbl_false_message, btn_done
    lbl_false_message.grid_forget()
    btn_unttn.grid_forget()

    rows, columns = 2, 1
    for i in range(rows):
        root.rowconfigure(index=i, weight=0)
    for i in range(columns):
        root.columnconfigure(index=i, weight=0)


def handler_btn_done():
    global answers, my_scores
    new_answer = entry_input.get()
    entry_input.delete(0, "end")
    forget_window_1()

    if new_answer in answers:
        my_scores += 1
        score.configure(text="Ваш текущий счёт:" + str(my_scores))
        show_window_2()
    else:
        show_window_3()


def handler_btn_ttn():
    global question, answers, lbl_start_message
    forget_window_2()
    question, answers = logic.choose_question()
    lbl_start_message.configure(text=question)
    show_window_1()

def handler_btn_unttn():
    global question, answers, lbl_start_message
    forget_window_3()
    question, answers = logic.choose_question()
    lbl_start_message.configure(text=question)
    show_window_1()



# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()  # создаём окно и привязываем его переменной root
root.title("console")  # устанавливаем заголовок окна
# root.wm_attributes('-fullscreen', True)
root.after(0, lambda:root.state('zoomed'))

#root.iconbitmap("C:/Users/rarlolgemas/Desktop/сайт/icon.ico")
root.geometry("1920x1080")  # устанавливаем размеры окна
my_font=ctk.CTkFont(family="Nunito", size=30)
#root.image = PhotoImage(file='C:/Users/rarlolgemas/Desktop/сайт/bg.png')
#bg_logo = Label(root, image=root.image)
#bg_logo.grid(row=0, column=0)



# виджеты для окна 1
lbl_start_message = ctk.CTkLabel(master=root,
                                 font=(my_font))
question, answers = logic.choose_question()
lbl_start_message.configure(text=question)


entry_input = ctk.CTkEntry(master=root,
                           font=(my_font))
entry_input.configure(justify="center")
btn_done = ctk.CTkButton(master=root,font=(my_font))
btn_done.configure(text="Ответить", command=handler_btn_done)
score = ctk.CTkLabel(master=root, font=(my_font))
score.configure(text="Ваш текущий счёт: 0")

my_scores = 0

# виджеты для окна 2
lbl_true_message = ctk.CTkLabel(master=root,
                                font=(my_font))
lbl_true_message.configure(text="Ответ верный", text_color="#00ff7f")
btn_ttn = ctk.CTkButton(master=root,
                        font=(my_font))
btn_ttn.configure(text="Перейти к слейдующему", command=handler_btn_ttn)

#окно 3
lbl_false_message = ctk.CTkLabel(master=root,
                                 font=(my_font))
lbl_false_message.configure(text="Ответ неверный", text_color="#dc143c")
btn_unttn = ctk.CTkButton(master=root,
                          font=(my_font))
btn_unttn.configure(text="Перейти к слейдующему", command=handler_btn_unttn)

show_window_1()


root.mainloop()  # отображаем окно и запускаем цикл обработки событий окна для взаимодействия c пользователем