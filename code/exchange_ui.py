import tkinter as tk
from tkinter import ttk, Entry, Label, Button, Frame, Canvas
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from currency_converter import CurrencyConverter as converter
import collections


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
            self, text="", font=("Arial", 13, "bold"), bg="#3E3E3E", fg="white", width=20, height=7)
        self.info_block.grid(column=0, row=1, columnspan=2)

        # label generation
        self.labels_dict = {
            "base_currency_label": ["Select base currency: "],
            "goal_currency_label": ["Select currency to convert to: "],
            "exchanged_rate_label": ["Enter how muich you want to exchange: "]
        }
        label_row = 0
        for key in self.labels_dict:
            lb = Label(self, text=self.labels_dict[key][0], bg="#3E3E3E", fg="white", pady=10).grid(
                row=(2+label_row), column=0, sticky="w", ipadx=20)
            label_row += 1

        # combobox generation
        self.combobox_dict = {
            "base_currency": [tk.StringVar(), ""],
            "goal_currency": [tk.StringVar(), ""],
        }

        combobox_row = 0
        for key in self.combobox_dict:
            cb = ttk.Combobox(
                self, textvariable=self.combobox_dict[key][0], width=35, values=self.currency_supported_list, state="normal")
            cb.grid(column=1, row=(combobox_row+2))
            # cb.bind('<<ComboboxSelected>>', self.combobox_dict[key][2])
            cb.bind('<<ComboboxSelected>>', lambda event,
                    key=key: self.currency_changed(event, key))
            cb.bind("<KeyRelease>", lambda event,
                    key=key: self.check_key(event, key))
            self.combobox_dict[key].append(cb)
            combobox_row += 1

        # TODO: loop through and add functions indicating which combobox it should attach to

        self.exchanged_amount = Entry(width=38)
        self.exchanged_amount.grid(column=1, row=4)

        self.currency_exchange_icon = Image.open("icons\currency.png")
        self.resized_icon = self.currency_exchange_icon.resize((50, 50))
        self.icon = ImageTk.PhotoImage(self.resized_icon)
        self.exchange_button = Button(
            self, command=self.currency_entered, borderwidth=0, image=self.icon, bg="#3E3E3E", activebackground="#6D6D6D")
        self.exchange_button.grid(column=0, row=5, columnspan=2, pady=10)

    def currency_changed(self, event, key):
        self.combobox_dict[key][1] = self.currency_supported_dict[self.combobox_dict[key][0].get()]

    def currency_entered(self):
        base_currency_code = self.combobox_dict["base_currency"][1]
        goal_currency_code = self.combobox_dict["goal_currency"][1]
        exchanged_amount = self.exchanged_amount.get()
        exchanger = converter(base_currency_code, goal_currency_code)
        content = exchanger.currency_conversion(exchanged_amount)
        self.info_block["text"] = base_currency_code + " " + exchanged_amount + " : " + \
            goal_currency_code + " " + \
            content["rates"][goal_currency_code]["rate_for_amount"] + \
            "\n\nRate of exchange:" + \
            content["rates"][goal_currency_code]["rate"]

    def check_key(self, event, key):
        value = event.widget.get()
        if value == '':
            data = self.currency_supported_list
        else:
            data = []
            for item in self.currency_supported_list:
                if value.lower() in item.lower():
                    data.append(item)
        self.combobox_dict[key][2]['values'] = data
