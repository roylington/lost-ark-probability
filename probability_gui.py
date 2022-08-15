
import tkinter as tk
from typing import Optional
import probability_func as func


root = tk.Tk()
root.title("Binomial Probability")
root.geometry("1200x300")
root['bg'] = "#323232"

tk.Label(root, bg="#323232", fg="#f0f0f0", text="Probability after x tries.", 
        font=("helvetica", 14, "bold")).grid(row=0,column=0)
tk.Label(root, bg="#323232", fg="#f0f0f0", text="Tries needed for p probability.", 
        font=("helvetica", 14, "bold")).grid(row=0, column=2, padx=50)

def probability_input():
    """Build left grid - Probability after x tries - input windows"""
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Chance of success").grid(row=1, column=0)
    success = tk.Entry(root)
    success.grid(row=1, column=1)

    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text=f"Success increase in each step").grid(row=2, column=0)
    step = tk.Entry(root)
    step.grid(row=2, column=1)

    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Tries to calculate").grid(row=3, column=0)
    tries = tk.Entry(root)
    tries.grid(row=3, column=1)

    return success, tries, step


def tries_input():
    """Build right grid - Tries needed for p probability - input windows"""
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Chance of success").grid(row=1,column=2)
    success = tk.Entry(root)
    success.grid(row=1, column=3)

    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Success increase in each step").grid(row=2, column=2)
    step = tk.Entry(root)
    step.grid(row=2, column=3)

    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Wanted approximate probability").grid(row=3, column=2)
    prob = tk.Entry(root)
    prob.grid(row=3, column=3)

    return success, step, prob


def materials_needed():
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Destruction/Guardian Stone cost").grid(row=5, column=2)
    stone = tk.Entry(root)
    stone.grid(row=5, column=3)
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Leapstone cost").grid(row=6, column=2)
    leap = tk.Entry(root)
    leap.grid(row=6, column=3)
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="Fusion material cost").grid(row=7, column=2)
    fusion = tk.Entry(root)
    fusion.grid(row=7, column=3)
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="On average you will need:").grid(row=8, column=2)
    tk.Label(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text="TBD").grid(row=8, column=3)
    return stone, leap, fusion

p_success, p_step, p_tries = probability_input()
t_success, t_step, t_prob = tries_input()
stone, leap, fusion = materials_needed()

probability_tries = func.Probability(p_success, p_step, p_tries, root)
calc_prob = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: probability_tries.process_input())
calc_prob.grid(row=4, column=1, pady=25)

tries_for_probability = func.Tries(t_success, t_step, t_prob, root)
calc_tries = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: tries_for_probability.process_input())
calc_tries.grid(row=4, column=3, pady=25)

root.mainloop()
