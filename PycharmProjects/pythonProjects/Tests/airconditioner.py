class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def turn_on(self):
        self.is_on = True

    def is_on(self):
        return self.is_on

    def turn_off(self):
        self.is_on = False

    def increase_temperature(self):
        if self.is_on and self.temperature < 30:
            self.temperature += 1

    def decrease_temperature(self):
        if self.is_on and self.temperature > 16:
            self.temperature -= 1

    def get_temperature(self):
        return self.temperature

