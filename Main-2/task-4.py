import time


# --- Базовий клас ---
class Asset:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.status = "New"

    def calculate_value(self):
        return self._price

    def __add__(self, other):
        if isinstance(other, Asset):
            return self.calculate_value() + other.calculate_value()
        elif isinstance(other, (int, float)):
            return self.calculate_value() + other
        return NotImplemented

    def __str__(self):
        return f"{self.name}: {self.calculate_value()}$ (status: {self.status})"

    def __repr__(self):
        return f"Asset({self.name}, {self._price})"

    # --- Context Manager ---
    def __enter__(self):
        self.start_time = time.time()
        self.status = "Active"
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        elapsed = time.time() - self.start_time
        if elapsed > 3:
            self.status = "Expired"
        else:
            self.status = "Closed"


# --- Криптовалюта ---
class CryptoCoin(Asset):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def calculate_value(self):
        return self._price * self.amount


# --- NFT ---
class NFT(Asset):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_value(self):
        return self._price


# --- Портфель ---
class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def __iter__(self):
        # сортування від дешевих до дорогих
        return iter(sorted(self.assets, key=lambda x: x.calculate_value()))


# --- Тест ---
if __name__ == "__main__":
    btc = CryptoCoin("Bitcoin", 30000, 0.1)
    eth = CryptoCoin("Ethereum", 2000, 1)
    nft = NFT("CoolNFT", 500)

    # Перевантаження +
    print("Сума BTC + ETH:", btc + eth)

    # Портфель
    portfolio = Portfolio()
    portfolio.add_asset(btc)
    portfolio.add_asset(eth)
    portfolio.add_asset(nft)

    print("\nАктиви (від дешевих до дорогих):")
    for asset in portfolio:
        print(asset)

    # Context manager
    print("\nПеревірка Time-Out:")
    with btc as a:
        time.sleep(4)

    print(btc)