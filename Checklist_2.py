import tkinter as tk

def toggle_button(item):
    var = var_dict[item]
    var.set(not var.get())
    update_state(item)

def update_state(item):
    if var_dict[item].get():
        btns[item].config(state=tk.DISABLED, relief=tk.SUNKEN)
    else:
        btns[item].config(state=tk.NORMAL, relief=tk.RAISED)

def clear_all():
    for item, var in var_dict.items():
        var.set(False)
        update_state(item)

root = tk.Tk()
root.title("Checklist Overlay")
root.geometry("400x600") # Adjust the size as needed for visibility
root.attributes("-topmost", 1) # Makes the window stay on top

# Dictionaries to hold the variables and buttons associated with each item
var_dict = {}
btns = {}
# List of items for buttons
items = [
    "1. Lines and Tubes",
    "2. Lower Neck, Thyroid and Thoracic Inlet",
    "3. Heart and Great Vessels",
    "4. Trachea and Central Airways",
    "5. Esophagus",
    "6. Lungs and Pleural Spaces",
    "7. Chest Wall and Axilla",
    "8. Liver and Biliary System",
    "9. Spleen",
    "10. Pancreas",
    "11. Adrenals",
    "12. Kidneys and Ureters",
    "13. GI Tract",
    "14. Peritoneum/Mesentery and Retroperitoneum",
    "15. Abdominal Aorta and IVC",
    "16. Bladder",
    "17. Reproductive Organs",
    "18. Pelvic Sidewall",
    "19. Rectum",
    "20. Bones and Soft Tissues"
]

# Creating and placing buttons
for item in items:
    var = tk.BooleanVar()
    btn = tk.Button(root, text=item, command=lambda i=item: toggle_button(i))
    btn.pack(anchor=tk.W)
    var_dict[item] = var
    btns[item] = btn

# Create "Clear All" button
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack()

root.mainloop()