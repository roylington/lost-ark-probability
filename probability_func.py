import tkinter as tk
from typing import Optional

class Wrap(tk.Label):
    """Pretty much tk.Label - when creating a Label it presets new bg and fg color and a new font."""
    def __init__(self, root, text) -> tk.Label:
        super().__init__(root, bg="#323232", fg="#f0f0f0", font=("helvetica", 9, "normal"), text=text)

class Probability:
    def __init__(self, e_success, e_tries, e_step, root) -> None:
        self.e_success = e_success
        self.e_tries = e_tries
        self.e_step = e_step

        self.success: Optional[float] = None
        self.tries: Optional[int] = None
        self.step: Optional[float] = None

        self.label = None
        self.root = root

    def process_input(self):
        assert self.e_success is not None
        assert self.e_tries is not None

        self.success = float(self.e_success.get())
        assert 0 <= self.success <= 100

        self.tries = int(self.e_tries.get())
        assert 0 <= self.tries

        self.step = self.e_step.get()
        self.step = 0 if self.step is None else int(self.step)
        
        self.calculate_prob()

    def calculate_prob(self):
        clear_label(self.label)

        prob_of_loss = 1 - self.success / 100
        product = prob_of_loss
        for i in range(1, self.tries):
            incr = i if i < 10 else 10
            product *= prob_of_loss - incr * (self.step / 100)

        FINAL_PROB = 0 if self.tries == 0 else round((1 - product) * 100, 2)
        
        self.label = Wrap(self.root, text=f"Probability of success: {FINAL_PROB}%")
        self.label.grid(row=5, column = 1)
        print(f"Probability of success: {FINAL_PROB}%")


def clear_label(label):
    if label is not None:
        label.destroy()


class Tries:
    def __init__(self, e_success, e_step, e_prob, root) -> None:
        self.e_success = e_success
        self.e_step = e_step
        self.e_prob = e_prob
        self.success: Optional[float] = None
        self.step: Optional[float] = None
        self.prob: Optional[float] = None

        self.label = None
        self.root = root

    def process_input(self):
        assert self.e_success is not None
        assert self.e_prob is not None

        self.success = float(self.e_success.get())
        assert 0 <= self.success <= 100
        
        self.step = self.e_step.get()
        self.step = 0 if self.step is None else int(self.step)

        self.prob = int(self.e_prob.get())
        assert 0 <= self.prob <= 100
        
        self.calculate_tries()

    def calculate_tries(self):
        clear_label(self.label)

        prob_of_loss = 1 - self.success / 100
        product = prob_of_loss
        tries = 1
        while 1 - product < self.prob / 100:
            incr = tries if tries < 10 else 10
            product *= prob_of_loss - incr * (self.step / 100)
            tries += 1

        self.label = Wrap(self.root, text=f"You need {tries} tries to have above {self.prob}% chance of success.")
        self.label.grid(row=5, column = 3)
        print(f"You need {tries} tries to have above {self.prob}% chance of success.")
        return tries

