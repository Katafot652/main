from dataclasses import dataclass
from enum import Enum
import json

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

@dataclass
class Asset:
    name: str
    amount: float
    _price: float
    risk: RiskLevel

    def __post_init__(self):
        # This triggers the setter validation immediately upon object creation
        self.price = self._price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # ARCHITECTURAL CRASH-TEST: Validation for logically impossible price
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = value

    def calculate_value(self):
        raise NotImplementedError()

class CryptoCoin(Asset):
    def calculate_value(self):
        return self.amount * self.price

class NFT(Asset):
    def calculate_value(self):
        return self.price

class Portfolio:
    def __init__(self):
        self.__assets = []

    def add_asset(self, asset):
        self.__assets.append(asset)

    def load_prices_from_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            for asset in self.__assets:
                if asset.name in data:
                    asset.price = data[asset.name]
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    def total_value(self):
        return sum(asset.calculate_value() for asset in self.__assets)

    def show_assets(self):
        for asset in self.__assets:
            print(asset.name, "-", asset.calculate_value())

if __name__ == "__main__":
    try:
        btc_amount = float(input("Enter BTC amount: "))
        eth_amount = float(input("Enter ETH amount: "))
        nft_price = float(input("Enter NFT price: "))

        # Validation happens here thanks to __post_init__
        btc = CryptoCoin("BTC", btc_amount, 1, RiskLevel.HIGH)
        eth = CryptoCoin("ETH", eth_amount, 1, RiskLevel.MEDIUM)
        nft = NFT("CoolNFT", 1, nft_price, RiskLevel.LOW)

        portfolio = Portfolio()
        portfolio.add_asset(btc)
        portfolio.add_asset(eth)
        portfolio.add_asset(nft)

        portfolio.load_prices_from_json("Main-2/prices.json")

        print("\nTotal portfolio value:", portfolio.total_value())

        print("\nAssets:")
        portfolio.show_assets()

        print("\n--- Object inspection ---")
        print("BTC:", vars(btc))
        print("ETH:", vars(eth))
        print("NFT:", vars(nft))

    except ValueError as e:
        print("\n--- CRASH-TEST TRIGGERED ---")
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)