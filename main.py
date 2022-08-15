import tkinter as tk
from probability_gui import *


def main():
    root = tk.Tk()
    root.title("Binomial Probability")
    root.geometry("1200x300")
    root['bg'] = "#323232"

    header(root)
    p_success, p_step, p_tries = probability_input(root)
    t_success, t_step, t_prob = tries_input(root)
    stone, leap, fusion = materials_needed(root)
    imgs(root)

    probability_tries = func.Probability(p_success, p_step, p_tries, root)
    calc_prob = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: probability_tries.process_input())
    calc_prob.grid(row=4, column=1, pady=10)

    tries_for_probability = func.Tries(t_success, t_step, t_prob, root)
    calc_tries = tk.Button(root, bg="#323232", fg="#f0f0f0", text="Calculate", command=lambda: tries_for_probability.process_input())
    calc_tries.grid(row=4, column=3, pady=10)

    root.mainloop()

if __name__=="__main__":
    main()