from tkinter import *
from wonderwords import RandomWord

r = RandomWord()

TIME_LIMIT = 60
user_words = []
generated_words = []
correct_words = []

def generate_word():
    rw = r.word(word_max_length=10).lower()
    generated_words.append(rw)
    return rw

def countdown(count):
    canvas.itemconfig(countdown_text, text=f"Time left: {count}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        check_result(user_words, generated_words)

def start_test():
    start_button.destroy()
    user_input.pack()
    user_input.focus()
    countdown(TIME_LIMIT)
    random_word = generate_word()
    canvas.itemconfig(word_text, text=f"{random_word}")


def check_result(list_1, list_2):

    user_input.destroy()

    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            correct_words.append(list_1[i])

    correct_chars = "".join(correct_words)
    corrected_cpm = len(correct_chars)
    wpm = corrected_cpm / 5

    result_text = f"Your result:\n\nCorrected CPM: {corrected_cpm}\nWPM: {wpm}"
    canvas.itemconfig(word_text, text=result_text)

    # print(f"Corrected CPM: {corrected_cpm}")
    # print(f"WPM: {wpm}")

def save_user_input():
    user_word = user_input.get().strip(" ")
    user_words.append(user_word)
    # print(user_words)
    # print(generated_words)

def next_word(event):
    save_user_input()
    user_input.delete(0, "end")
    new_word = generate_word()
    canvas.itemconfig(word_text, text=f"{new_word}")

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=800, height=500)
window.config(padx=20, pady=20, bg="#00ff7f")

canvas = Canvas(width=600, height=300, bg="#00ff7f", highlightthickness=0)
countdown_text = canvas.create_text(550, 20, text=f"Time left: 00", font=("Arial", 12, "normal"))
word_text = canvas.create_text(300, 150, text=f"Typing Speed Test\nPress Start", justify="center", font=("Arial", 28, "bold"))
canvas.pack()

user_input = Entry(font=("Arial", 12), fg="black", bg="white")
user_input.bind("<space>", next_word)

start_button = Button(padx=3, pady=3, text="Start", font=("Arial", 12), command=start_test)
start_button.pack()

window.mainloop()









