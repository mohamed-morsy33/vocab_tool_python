import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox

# Setting up the list of vocab and the counting index
vocab_in_language = []
vocab_translations = []
index = 0

# if true, we are translating
translate_mode = True

# Change this to True to debug
debug = False

def close_app():
    if messagebox.askokcancel("Close", "Are you sure you want to close Vocab Tool?"):
        messagebox.showinfo("Close", "Closing now...")
        root.destroy()
    else:
        messagebox.showinfo("Close", "Close operation cancelled.")

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', close_app)
root.resizable(False, False)
root.title("Vocabulary Tool")
root.iconbitmap('pencil-icon.ico')
root.geometry("800x600")
root.maxsize(800, 600)
root.minsize(800, 600)

def set_buttons():
    global button_r
    global button_l

    button_r = tk.Button(text="->", width=5, height=2, command=move_right)
    button_r.config(bg='gray', fg='white', font=text_font)
    button_l = tk.Button(text="<-", width=5, height=2, command=move_left)
    button_l.config(bg='gray', fg='white', font=text_font)

def show_translate():
    global index
    global translate_mode
    global vocab_translations
    global vocab_in_language

    if translate_mode:
        translate_mode = not translate_mode
        set_text(vocab_translations[index])
    else:
        translate_mode = not translate_mode
        set_text(vocab_in_language[index])

def move_right():
    global index
    global translate_mode

    if (index < len(vocab_in_language) - 1):
        index += 1
        translate_mode = True
        set_text(vocab_in_language[index])


def move_left():
    global index
    global translate_mode

    if (index > 0):
        index -= 1
        translate_mode = True
        set_text(vocab_in_language[index])


text_font = Font(family="Arial", size=32)
T1 = tk.Label(width=40, height=10, font=text_font, text="test")
set_buttons()
button_translate = tk.Button(text="Translate", width=5, height=2, command=show_translate)
button_translate.config(bg='gray', fg='white', font=text_font)


def set_text(txt):
    global T1
    global button_l
    global button_r
    global translate_mode
    T1.destroy()
    button_l.destroy()
    button_r.destroy()

    set_buttons()

    if (translate_mode):
        button_translate = tk.Button(text="Translate", width=10, height=2, command=show_translate)
        button_translate.config(bg='gray', fg='white', font=text_font)
    else:
        button_translate = tk.Button(text="Word", width=10, height=2, command=show_translate)
        button_translate.config(bg='gray', fg='white', font=text_font)

    T1 = tk.Label(width=21, height=10, font=text_font, text=txt)

    T1.grid(row=1, column=2)
    button_l.grid(row=1,column=1)
    button_r.grid(row=1, column=3)
    button_translate.grid(row=2, column=2)

with open('vocab.txt', 'r', encoding='utf-8') as file:
    line = file.readline()

    while line:
        language_word = line[0:line.index("(")-1]
        translation_word = line[line.index("(")+1:len(line)-2]

        if (debug):
            print(language_word + ", " + translation_word)

        vocab_in_language.append(language_word)
        vocab_translations.append(translation_word)

        line = file.readline()

set_text(vocab_in_language[0])

root.mainloop()



