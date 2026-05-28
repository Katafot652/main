import os
import json
from enum import Enum

# 1. Перелічуваний тип (Enum)
class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

# 2. Базовий клас
class Asset:
    def __init__(self, name: str, amount: float, price: float, risk: RiskLevel):
        self.name = name
        self.amount = amount
        self.price = price  # Автоматично викликає @price.setter
        self.risk = risk

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        # Архітектурний краш-тест
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = value

    def calculate_value(self) -> float:
        raise NotImplementedError("Цей метод має бути перевизначений у класах-нащадках")

# 3. Класи-нащадки
class CryptoCoin(Asset):
    def __init__(self, name: str, amount: float, price: float, risk: RiskLevel, blockchain: str):
        super().__init__(name, amount, price, risk)
        self.blockchain = blockchain

    def calculate_value(self) -> float:
        return self.amount * self.price

class NFT(Asset):
    def __init__(self, name: str, amount: float, price: float, risk: RiskLevel, collection: str):
        super().__init__(name, amount, price, risk)
        self.collection = collection

    def calculate_value(self) -> float:
        return self.price

# 4. Клас-менеджер (Композиція)
class Portfolio:
    def __init__(self):
        self._assets = []

    def add_asset(self, asset: Asset):
        self._assets.append(asset)
        print(f"Успішно додано актив: {asset.name}")

    def load_prices_from_json(self, file_name: str):
        # Автоматично знаходимо папку, в якій лежить цей скрипт (main.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Об'єднуємо шлях до папки зі специфічним ім'ям файлу
        full_path = os.path.join(current_dir, file_name)
        
        try:
            with open(full_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for asset in self._assets:
                    if asset.name in data:
                        asset.price = data[asset.name]
            print(f"Ціни успішно оновлено з файлу: {full_path}")
        except FileNotFoundError:
            print(f"\n[ПОМИЛКА] Не вдалося знайти файл за шляхом: {full_path}")
            print(f"Будь ласка, переконайся, що файл '{file_name}' лежить в ОДНІЙ папці з файлом програми.\n")

    def total_value(self) -> float:
        return sum(asset.calculate_value() for asset in self._assets)

    def show_assets(self):
        print("\n--- Склад портфеля ---")
        for asset in self._assets:
            det = f"({asset.blockchain})" if isinstance(asset, CryptoCoin) else f"({asset.collection})"
            print(f"{asset.name} {det} | Ризик: {asset.risk.value} | Вартість: {asset.calculate_value()} USD")

# Блок демонстрації
if __name__ == "__main__":
    print("--- Тестування системи трекера портфеля ---")
    try:
        btc_amount = float(input("Введіть кількість BTC: "))
        eth_amount = float(input("Введіть кількість ETH: "))
        nft_price = float(input("Введіть початкову ціну NFT: "))

        btc = CryptoCoin("BTC", btc_amount, 1.0, RiskLevel.HIGH, "Bitcoin Blockchain")
        eth = CryptoCoin("ETH", eth_amount, 1.0, RiskLevel.MEDIUM, "Ethereum Network")
        nft = NFT("CoolNFT", 1.0, nft_price, RiskLevel.LOW, "CryptoPunks Collection")

        portfolio = Portfolio()
        portfolio.add_asset(btc)
        portfolio.add_asset(eth)
        portfolio.add_asset(nft)

        # Передаємо лише назву файлу, шлях обчислиться автоматично всередині методу
        portfolio.load_prices_from_json("prices.json")

        portfolio.show_assets()
        print(f"\nЗагальна вартість портфеля: {portfolio.total_value()} USD")

    except ValueError as e:
        print("\n[CRASH-TEST TRIGGERED] Спрацював архітектурний захист!")
        print("Помилка валідації:", e)
    except Exception as e:
        print("\nНепередбачувана помилка:", e)