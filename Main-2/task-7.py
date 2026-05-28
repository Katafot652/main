import sys
import pickle
import csv
import json

# --- Класи з попередніх лабораторних робіт ---
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
    pass

class Portfolio:
    def __init__(self):
        self.assets = []
        
    def add_asset(self, asset):
        self.assets.append(asset)
        print(f"\n[Success] Актив '{asset.name}' успішно додано до портфеля!")

    def show_portfolio(self):
        if not self.assets:
            print("\n[Info] Портфель порожній.")
            return
        print("\n--- Поточні активи ---")
        for asset in self.assets:
            asset_type = "Crypto" if isinstance(asset, CryptoCoin) else "NFT"
            print(f"[{asset_type}] {asset.name} | Вартість: {asset.calculate_value()} USD")

    def save_state(self, filepath="portfolio.pkl"):
        with open(filepath, 'wb') as f:
            pickle.dump(self.assets, f)
        print(f"\n[System] Стан портфеля успішно збережено у {filepath}")

    def load_state(self, filepath="portfolio.pkl"):
        try:
            with open(filepath, 'rb') as f:
                self.assets = pickle.load(f)
            print(f"[System] Відновлено {len(self.assets)} активів із резервної копії.")
        except FileNotFoundError:
            print("[System] Файл резервної копії не знайдено. Створено новий портфель.")

    def export_to_csv(self, filepath="report.csv"):
        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Назва', 'Тип', 'Вартість (USD)'])
            for asset in self.assets:
                asset_type = "Crypto" if isinstance(asset, CryptoCoin) else "NFT"
                writer.writerow([asset.name, asset_type, asset.calculate_value()])
        print(f"\n[System] Звіт успішно експортовано у {filepath}")

# --- Інтерфейс Користувача (CLI) ---
def show_menu():
    print("\n" + "="*35)
    print(" CRYPTO PORTFOLIO TRACKER v1.0")
    print("="*35)
    print("1. Показати всі активи")
    print("2. Додати новий актив")
    print("3. Зберегти стан (Pickle)")
    print("4. Експортувати звіт (CSV)")
    print("0. Зберегти та Вийти")
    print("="*35)

if __name__ == "__main__":
    manager = Portfolio()
    manager.load_state()

    while True:
        show_menu()
        try:
            choice = input("Оберіть дію (0-4): ").strip()
            
            # Диспетчеризація команд
            match choice:
                case "1":
                    manager.show_portfolio()
                
                case "2":
                    print("\nТип активу: 1 - Криптовалюта, 2 - NFT")
                    a_type = input("Оберіть тип (1 або 2): ").strip()
                    
                    if a_type not in ["1", "2"]:
                        print("[Увага] Невідомий тип активу. Операцію скасовано.")
                        continue
                        
                    name = input("Введіть назву (наприклад, BTC): ").strip()
                    if not name:
                        raise ValueError("Назва не може бути порожньою!")
                        
                    price = float(input("Введіть поточну ціну (USD): "))
                    if price < 0:
                        raise ValueError("Ціна не може бути від'ємною!")
                        
                    if a_type == "1":
                        amount = float(input("Введіть кількість монет: "))
                        if amount < 0:
                            raise ValueError("Кількість не може бути від'ємною!")
                        new_asset = CryptoCoin(name, price, amount)
                    else:
                        new_asset = NFT(name, price)
                        
                    manager.add_asset(new_asset)

                case "3":
                    manager.save_state()

                case "4":
                    manager.export_to_csv()

                case "0":
                    print("\n[System] Ініціалізація виходу...")
                    manager.save_state()
                    print("Програма завершує роботу. Гарного дня!")
                    sys.exit(0)

                case _:
                    print("\n[Warning] Невідома команда! Будь ласка, оберіть пункт від 0 до 4.")

        # Обробка помилок (Fault Tolerance)
        except ValueError as e:
            print(f"\n[Помилка введення даних]: {e}")
            print("Будь ласка, використовуйте лише цифри для вводу цін та кількості.")
        except Exception as e:
            print(f"\n[Критична помилка]: {e}")