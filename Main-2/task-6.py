import json
import pickle
import csv
import os

class Asset:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def calculate_value(self):
        return self._price

class CryptoCoin(Asset):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def calculate_value(self):
        return self._price * self.amount

class NFT(Asset):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_value(self):
        return self._price

class Portfolio:
    def __init__(self):
        self.assets = []
        self.config = {}

    # 1. Зовнішні налаштування (JSON)
    def load_config(self, filepath="config.json"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"[System] Запущено: {self.config.get('app_name', 'Tracker')}")
            print(f"[System] Базова валюта: {self.config.get('base_currency', 'USD')}")
        except FileNotFoundError:
            print("[System] Файл конфігурації не знайдено, використовуються стандарти.")

    def add_asset(self, asset):
        self.assets.append(asset)
        print(f"[+] Додано актив: {asset.name}")

    # 2. Повний бекап системи (Pickle)
    def save_state(self, filepath="portfolio_backup.pkl"):
        with open(filepath, 'wb') as f:
            pickle.dump(self.assets, f)
        print(f"\n[System] Стан портфеля ({len(self.assets)} активів) збережено у {filepath}")

    def load_state(self, filepath="portfolio_backup.pkl"):
        try:
            with open(filepath, 'rb') as f:
                self.assets = pickle.load(f)
            print(f"\n[System] Успішно відновлено {len(self.assets)} активів із бекапу.")
        except FileNotFoundError:
            print(f"\n[Error] Файл бекапу {filepath} не знайдено.")

    # 3. Табличний звіт (CSV)
    def export_to_csv(self, filepath="portfolio_report.csv"):
        currency = self.config.get('base_currency', 'USD')
        # utf-8-sig допомагає Excel правильно читати кирилицю
        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';') # Крапка з комою краще для Excel
            writer.writerow(['Назва активу', 'Тип', 'Поточна вартість'])
            
            for asset in self.assets:
                asset_type = "Crypto" if isinstance(asset, CryptoCoin) else "NFT"
                writer.writerow([asset.name, asset_type, f"{asset.calculate_value()} {currency}"])
                
        print(f"[System] Звіт CSV успішно згенеровано: {filepath}")

    def show_portfolio(self):
        print("\n--- Поточний стан портфеля ---")
        if not self.assets:
            print("Портфель порожній.")
        for asset in self.assets:
            print(f" - {asset.name}: {asset.calculate_value()}")

if __name__ == "__main__":
    manager = Portfolio()
    manager.load_config()

    print("\n--- Сценарій 1: Додавання та Збереження ---")
    btc = CryptoCoin("Bitcoin", 60000, 0.5)
    eth = CryptoCoin("Ethereum", 3000, 2)
    nft = NFT("CryptoPunk", 15000)

    manager.add_asset(btc)
    manager.add_asset(eth)
    manager.add_asset(nft)
    
    manager.show_portfolio()
    manager.save_state()
    manager.export_to_csv()

    print("\n--- Сценарій 2: Імітація перезапуску програми ---")
    # Створюємо повністю новий, порожній менеджер
    new_manager = Portfolio()
    new_manager.load_config()
    new_manager.show_portfolio() # Має бути порожнім

    print("\n--- Сценарій 3: Відновлення даних ---")
    new_manager.load_state()
    new_manager.show_portfolio() # Дані повернулися!