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

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
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

    def total_value(self):
        return sum(asset.calculate_value() for asset in self.__assets)

    def load_prices_from_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        for asset in self.__assets:
            if asset.name in data:
                asset.price = data[asset.name]


if __name__ == "__main__":
    try:
        btc = CryptoCoin("BTC", float(input("Enter BTC amount: ")), 1)
        eth = CryptoCoin("ETH", float(input("Enter ETH amount: ")), 1)
        nft = NFT("CoolNFT", 1, float(input("Enter NFT price: ")))

        portfolio = Portfolio()
        portfolio.add_asset(btc)
        portfolio.add_asset(eth)
        portfolio.add_asset(nft)

        portfolio.load_prices_from_json("Main-2/prices.json")

        print("Total portfolio value:", portfolio.total_value())

    except ValueError as e:
        print("Error:", e)
    except Exception:
        print("Invalid input")