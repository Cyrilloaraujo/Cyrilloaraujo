import tkinter as tk
from tkinter.font import Font
import speech_recognition as sr
import threading

# Define a mapping of checklist items to their trigger words
trigger_words = {
    "1. Lines and Tubes": ["lines", "tubes"],
    "2. Lower Neck, Thyroid and Thoracic Inlet": ["neck", "thyroid", "inlet"],
    "3. Heart and Great Vessels": ["heart", "vessels"],
    "4. Trachea and Central Airways": ["trachea", "airways"],
    "5. Esophagus": ["esophagus"],
    "6. Lungs and Pleural Spaces": ["lungs", "pleural"],
    "7. Chest Wall and Axilla": ["chest wall", "axilla"],
    "8. Liver and Biliary System": ["liver", "biliary"],
    "9. Spleen": ["spleen"],
    "10. Pancreas": ["pancreas"],
    "11. Adrenals": ["adrenals"],
    "12. Kidneys and Ureters": ["kidneys", "ureters"],
    "13. GI Tract": ["gi tract"],
    "14. Peritoneum/Mesentery and Retroperitoneum": ["peritoneum", "mesentery", "retroperitoneum"],
    "15. Abdominal Aorta and IVC": ["aorta", "ivc"],
    "16. Bladder": ["bladder"],
    "17. Reproductive Organs": ["reproductive organs"],
    "18. Pelvic Sidewall": ["pelvic sidewall"],
    "19. Rectum": ["rectum"],
    "20. Bones and Soft Tissues": ["bones", "soft tissues"],
}

def toggle_button(item):
    var = var_dict[item]
    var.set(not var.get())
    update_state(item)

def update_state(item):
    if var_dict[item].get():
        btns[item].config(bg="#90ee90")  # Light green when active
    else:
        btns[item].config(bg="#add8e6")  # Light blue as default

def clear_all():
    for item, var in var_dict.items():
        var.set(False)
        update_state(item)

def highlight_word(speech):
    for item, keywords in trigger_words.items():
        if any(keyword.lower() in speech for keyword in keywords):
            var_dict[item].set(True)
            update_state(item)

def adjust_font_size(event=None):
    new_size = max(8, min(root.winfo_width() // 80, root.winfo_height() // 25))
    font.config(size=new_size)
    for btn in btns.values():
        btn.config(font=font)

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            try:
                speech = r.recognize_google(audio).lower()
                print("You said: " + speech)
                highlight_word(speech)
            except sr.UnknownValueError:
                print("Google Web Speech could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech service; {e}")
    except KeyboardInterrupt:
        pass

# Initialize the root window
root = tk.Tk()
root.title("Checklist Overlay")
root.geometry("1200x200")
root.configure(bg='#add8e6')  # Set the window background to light blue
root.attributes("-topmost", 1)
root.attributes('-alpha', 0.8)  # Set the transparency to 20%

font = Font(family="Helvetica", size=12)

var_dict = {}
btns = {}
items = list(trigger_words.keys())  # Use the keys from the trigger_words dict as the items

for index, item in enumerate(items):
    row = index // 4
    column = index % 4
    var = tk.BooleanVar()
    btn = tk.Button(root, text=item, bg="#add8e6", font=font, command=lambda i=item: toggle_button(i))
    btn.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(column, weight=1)
    var_dict[item] = var
    btns[item] = btn

clear_button = tk.Button(root, text="Clear All", bg="#add8e6", font=font, command=clear_all)
clear_button.grid(row=5, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

root.bind('<Configure>', adjust_font_size)

# Start speech recognition in a background thread
threading.Thread(target=listen, daemon=True).start()

root.mainloop()