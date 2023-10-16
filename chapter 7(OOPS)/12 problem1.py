class Vechile:
    def __init__(self, fare):
        self.fare = fare

    def getvechile_fare(self):
        return self.fare * 100


class Bus(Vechile):
    def __init__(self, fare):
        super().__init__(fare)

    def get_fare(self):
        self.bus_fare = super().getvechile_fare()
        self.maintainnance_fare = self.bus_fare * 0.1
        return self.bus_fare + self.maintainnance_fare


bus = Bus(70)
print(bus.getvechile_fare())
print(bus.get_fare())
