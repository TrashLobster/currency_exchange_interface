import tkinter as tk
from tkinter import ttk, Entry, Label, Button, Frame, Canvas
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from sqlalchemy import column
from currency_converter import CurrencyConverter as converter
import collections
from string import ascii_uppercase


class ExchangeUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title = "Currency Converter"
        self.geometry("540x400")
        self.config(bg="#3E3E3E")
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        self.currency_supported_dict = {
            (k + " - " + v): k for (k, v) in converter.get_supported_currency()["currencies"].items()}
        self.currency_supported_dict = collections.OrderedDict(
            sorted(self.currency_supported_dict.items()))
        self.currency_supported_list = [
            k for (k, v) in self.currency_supported_dict.items()]

        self.title = tk.Label(
            self, text="What do you want to exchange?", font=("Arial", 13, "bold"), bg="#3E3E3E", fg="white", pady=20)
        self.title.grid(column=0, row=0, columnspan=2)

        self.info_block = tk.Label(
            self, text="PLACEHOLDER", font=("Arial", 13, "bold"), bg="#3E3E3E", fg="white", width=20, height=7)
        self.info_block.grid(column=0, row=1, columnspan=2)

        self.base_currency_var = tk.StringVar()
        self.base_currency_code = ""
        self.goal_currency_var = tk.StringVar()
        self.goal_currency_code = ""

        self.base_currency_label = tk.Label(
            self, text="Select base currency: ", bg="#3E3E3E", fg="white", pady=10)
        self.base_currency_label.grid(column=0, row=2, sticky="w", ipadx=20)
        self.base_currency = ttk.Combobox(
            self, textvariable=self.base_currency_var, width=35)
        self.base_currency['values'] = self.currency_supported_list
        self.base_currency['state'] = 'normal'
        self.base_currency.grid(column=1, row=2)

        self.goal_currency_label = tk.Label(
            self, text="Select currency to convert to: ", bg="#3E3E3E", fg="white", pady=10)
        self.goal_currency_label.grid(column=0, row=3, sticky="w", ipadx=20)
        self.goal_currency = ttk.Combobox(
            self, textvariable=self.goal_currency_var, width=35)
        self.goal_currency['values'] = self.currency_supported_list
        self.goal_currency['state'] = 'readonly'
        self.goal_currency.grid(column=1, row=3)
        # self.goal_currency.bind("<Key>", self.findInBox)

        self.exchange_rate_label = tk.Label(
            self, text="Enter how much you want to exchange: ", bg="#3E3E3E", fg="white", pady=10)
        self.exchange_rate_label.grid(column=0, row=4, sticky="w", ipadx=20)
        self.exchanged_amount = Entry(width=38)
        self.exchanged_amount.grid(column=1, row=4)

        self.base_currency.bind('<<ComboboxSelected>>',
                                self.base_currency_changed)
        self.base_currency.bind("<KeyRelease>", self.check_key)
        self.goal_currency.bind('<<ComboboxSelected>>',
                                self.goal_currency_changed)

        self.currency_exchange_icon = Image.open("icons\currency.png")
        self.resized_icon = self.currency_exchange_icon.resize((50, 50))
        self.icon = ImageTk.PhotoImage(self.resized_icon)
        self.exchange_button = Button(
            self, command=self.currency_entered, borderwidth=0, image=self.icon, bg="#3E3E3E", activebackground="#6D6D6D")
        self.exchange_button.grid(column=0, row=5, columnspan=2, pady=10)

    def base_currency_changed(self, event):
        self.base_currency_code = self.currency_supported_dict[self.base_currency_var.get(
        )]

    def goal_currency_changed(self, event):
        self.goal_currency_code = self.currency_supported_dict[self.goal_currency_var.get(
        )]

    def currency_entered(self, event):
        currency_converter = converter(
            self.base_currency_code, self.goal_currency_code)
        print(currency_converter.currency_conversion(
            self.exchanged_amount.get()))
    
    def check_key_base(self, event):
        value = event.widget.get()
        print(value)

        if value == '':
            data = self.currency_supported_list
        else:
            data = []
            for item in self.currency_supported_list:
                if value.lower() in item.lower():
                    data.append(item)
        self.base_currency['values'] = data
    
    def check_key(self, event):
        value = event.widget.get()
        
        if value == '':
            data = self.currency_supported_list
        else:
            data = []
            for item in self.currency_supported_list:
                if value.lower() in item.lower():
                    data.append(item)
        self.base_currency['values'] = data


if __name__ == "__main__":
    window = ExchangeUI()
    window.mainloop()
