from abc import ABC, abstractmethod

import requests
import tkinter as tk
from tkinter import ttk


class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        pass


class OpenExchangeRatesConverter(CurrencyConverter):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://openexchangerates.org/api/latest.json"

    def get_rates(self):
        response = requests.get(f"{self.api_url}?app_id={self.api_key}")
        data = response.json()
        return data['rates']

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rates = self.get_rates()
        if from_currency != "USD":
            amount = amount / rates[from_currency]
        return amount * rates[to_currency]


class USDAdapter(CurrencyConverter):
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        return self.converter.convert(amount, from_currency, to_currency)


class EURAdapter(CurrencyConverter):
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        return self.converter.convert(amount, from_currency, to_currency)


class CurrencyConverterManager:
    def __init__(self, api_key: str):
        self.converter = OpenExchangeRatesConverter(api_key)
        self.adapters = {
            'USD': USDAdapter(self.converter),
            'EUR': EURAdapter(self.converter),
            # Add other adapters here
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        adapter = self.adapters.get(from_currency)
        if adapter:
            return adapter.convert(amount, from_currency, to_currency)
        else:
            raise ValueError(f"Currency {from_currency} is not supported.")


class CurrencyConverterUI:
    def __init__(self, manager: CurrencyConverterManager):
        self.manager = manager
        self.root = tk.Tk()
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        ttk.Label(self.root, text="Amount:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.amount_var).grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.root, text="From Currency:").grid(column=0, row=1, padx=10, pady=10)
        ttk.Combobox(self.root, textvariable=self.from_currency_var, values=list(manager.adapters.keys())).grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.root, text="To Currency:").grid(column=0, row=2, padx=10, pady=10)
        ttk.Combobox(self.root, textvariable=self.to_currency_var, values=list(manager.adapters.keys())).grid(column=1, row=2, padx=10, pady=10)

        ttk.Button(self.root, text="Convert", command=self.convert).grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        ttk.Label(self.root, textvariable=self.result_var).grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def convert(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        try:
            result = self.manager.convert(amount, from_currency, to_currency)
            self.result_var.set(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        except ValueError as e:
            self.result_var.set(str(e))

    def run(self):
        self.root.mainloop()


api_key = "a0930a7138ab4736944152661a2b84b3"
manager = CurrencyConverterManager(api_key)
ui = CurrencyConverterUI(manager)
ui.run()
