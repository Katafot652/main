class Asset:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def calculate_value(self):
        return self._price

    def __str__(self):
        return f"{self.name}: {self.calculate_value()} USD"


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


# Функтор для обчислення вартості активів
class ValueCalculator:
    def __init__(self):
        self.calls = 0
        self.total_calculated = 0

    def __call__(self, asset):
        value = asset.calculate_value()
        self.calls += 1
        self.total_calculated += value
        return value


# Власний ітератор: повертає лише активи дорожчі за мінімальне значення
class ExpensiveAssetIterator:
    def __init__(self, assets, min_value):
        self.assets = assets
        self.min_value = min_value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.assets):
            asset = self.assets[self.index]
            self.index += 1
            if asset.calculate_value() >= self.min_value:
                return asset
        raise StopIteration


# Менеджер портфеля
class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    # Використання власного ітератора
    def get_expensive_assets(self, min_value):
        return ExpensiveAssetIterator(self.assets, min_value)

    # Генератор: видає активи порціями по 3
    def paginate(self, page_size=3):
        for i in range(0, len(self.assets), page_size):
            yield self.assets[i:i + page_size]


# Тестування
if __name__ == "__main__":
    btc = CryptoCoin("Bitcoin", 30000, 0.1)   # 3000
    eth = CryptoCoin("Ethereum", 2000, 2)     # 4000
    nft1 = NFT("CryptoPunk", 5000)
    nft2 = NFT("BoredApe", 1500)

    portfolio = Portfolio()
    portfolio.add_asset(btc)
    portfolio.add_asset(eth)
    portfolio.add_asset(nft1)
    portfolio.add_asset(nft2)

    # Функтор
    calculator = ValueCalculator()
    print("Функтор:")
    print(calculator(btc))
    print(calculator(eth))
    print("Кількість викликів:", calculator.calls)
    print("Сумарно обчислено:", calculator.total_calculated)

    # Власний ітератор
    print("\nАктиви дорожчі за 3000 USD:")
    for asset in portfolio.get_expensive_assets(3000):
        print(asset)

    # Генератор
    print("\nПагінація по 3 активи:")
    for page in portfolio.paginate():
        print("Сторінка:")
        for asset in page:
            print(" ", asset)