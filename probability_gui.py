
import tkinter as tk
from typing import Optional
import probability_func as func
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Binomial Probability")
root.geometry("1200x300")
root['bg'] = "#323232"

tk.Label(root, bg="#323232", fg="#f0f0f0", text="Probability after x tries.", 
        font=("helvetica", 14, "bold")).grid(row=0,column=0)
tk.Label(root, bg="#323232", fg="#f0f0f0", text="Tries needed for p probability.", 
        font=("helvetica", 14, "bold")).grid(row=0, column=2, padx=50)

class Wrap(tk.Label):
    """Pretty much tk.Label - when creating a Label it presets new bg and fg color and a new font."""
    def __init__(self, root, text) -> tk.Label:
        super().__init__(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text=text)

def probability_input():
    """Build left grid - Probability after x tries - input windows"""
    Wrap(root, "Chance of success").grid(row=1, column=0)#tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Chance of success").grid(row=1, column=0)
    success = tk.Entry(root)
    success.grid(row=1, column=1)

    Wrap(root, text="Success increase in each step").grid(row=2, column=0)
    step = tk.Entry(root)
    step.grid(row=2, column=1)

    Wrap(root, text="Tries to calculate").grid(row=3, column=0)
    tries = tk.Entry(root)
    tries.grid(row=3, column=1)

    return success, tries, step


def tries_input():
    """Build right grid - Tries needed for p probability - input windows"""
    Wrap(root, text="Chance of success").grid(row=1,column=2)
    success = tk.Entry(root)
    success.grid(row=1, column=3)

    Wrap(root, text="Success increase in each step").grid(row=2, column=2)
    step = tk.Entry(root)
    step.grid(row=2, column=3)

    Wrap(root, text="Wanted approximate probability").grid(row=3, column=2)
    prob = tk.Entry(root)
    prob.grid(row=3, column=3)

    return success, step, prob


def materials_needed():
    Wrap(root, text="Destruction/Guardian Stone cost").grid(row=6, column=2)
    stone = tk.Entry(root)
    stone.grid(row=6, column=3)
    Wrap(root, text="Leapstone cost").grid(row=7, column=2)
    leap = tk.Entry(root)
    leap.grid(row=7, column=3)
    Wrap(root, text="Fusion material cost").grid(row=8, column=2)
    fusion = tk.Entry(root)
    fusion.grid(row=8, column=3)
    Wrap(root, text="On average you will need:").grid(row=9, column=2)
    Wrap(root, text="TBD").grid(row=9, column=3)
    return stone, leap, fusion

def imgs():
    stone = ImageTk.PhotoImage(Image.open(".\probability\pictures\destruc-stone.png").resize((30,30), Image.Resampling.LANCZOS))
    st = tk.Label(image=stone, borderwidth=0)
    st.image=stone
    st.grid(row=6, column=4)
    
    leap = ImageTk.PhotoImage(Image.open(".\probability\pictures\honor-stone.png").resize((30,30), Image.Resampling.LANCZOS))
    lp = tk.Label(image=leap, borderwidth=0)
    lp.image=leap
    lp.grid(row=7, column=4)
    
    fusion = ImageTk.PhotoImage(Image.open(".\probability\pictures\\fusion.png").resize((30,30), Image.Resampling.LANCZOS))
    fs = tk.Label(image=fusion,borderwidth=0)
    fs.image=fusion
    fs.grid(row=8, column=4)

p_success, p_step, p_tries = probability_input()
t_success, t_step, t_prob = tries_input()
stone, leap, fusion = materials_needed()
imgs()

probability_tries = func.Probability(p_success, p_step, p_tries, root)
calc_prob = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: probability_tries.process_input())
calc_prob.grid(row=4, column=1, pady=10)

tries_for_probability = func.Tries(t_success, t_step, t_prob, root)
calc_tries = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: tries_for_probability.process_input())
calc_tries.grid(row=4, column=3, pady=10)

root.mainloop()
