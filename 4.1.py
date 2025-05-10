class Computer:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")

my_computer = Computer("Dell", "XPS 13", 1200)
my_computer.display_specs()
