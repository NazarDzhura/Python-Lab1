class Refrigerator:
    refrigerator_count: int = 0

    def __init__(self, manufacturer="Not specified", volume: float = 0, weight: float = 0, power_consumption = 0, price: float = 0, model = "Not specified", model_year = 0):
        self.manufacturer = manufacturer
        self.volume = volume
        self.weight = weight
        self.power_consumption = power_consumption
        self.price = price
        self.model = model
        self.model_year = model_year
        Refrigerator.refrigerator_count += 1

    def __str__(self):
        return f"Manufacturer: {self.manufacturer}\nVolume: {self.volume}\nWeight: {self.weight}\nPower Consumption: {self.power_consumption}\nPrice: {self.price}\nModel: {self.model}\nModel year: {self.model_year}\n"

    @classmethod
    def get_count(cls):
        return cls.refrigerator_count

    def __del__(self):
        Refrigerator.refrigerator_count -= 1


ref1 = Refrigerator("LIEBHERR", 344, 70.3, 1000, 1925, "IKB 3560", 2021)
ref2 = Refrigerator("BOSCH", 745, 90.4, 1300, 1400, "KGN36XI35")
ref3 = Refrigerator("SAMSUNG", 344, 70.3, 1000, 1925)

print(ref1)
print(ref2)
print(ref3)
