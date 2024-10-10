class AutomaticBike:
    def __init__(self):
        self.__is_on = False
        self.__speed = 0
        self.__gear = 0

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False
        self.__speed = 0
        self.__gear = 0

    def accelerate(self):
        if not self.__is_on:
            return
        if self.__gear == 0:
            self.__speed += 1
            self.__gear = 1
        elif self.__gear == 1 and self.__speed < 20:
            self.__speed += 1
        elif self.__gear == 1 and self.__speed >= 20:
            self.__speed += 2
            self.__gear = 2
        elif self.__gear == 2 and self.__speed < 30:
            self.__speed += 2
        elif self.__gear == 2 and self.__speed >= 30:
            self.__speed += 3
            self.__gear = 3
        elif self.__gear == 3 and self.__speed < 40:
            self.__speed += 3
        elif self.__gear == 3 and self.__speed >= 40:
            self.__speed += 4
            self.__gear = 4
        elif self.__gear == 4:
            self.__speed += 4

    def decelerate(self):
        if not self.__is_on:
            return
        if self.__speed == 0:
            return
        if self.__gear == 1:
            self.__speed -= 1
            if self.__speed == 0:
                self.__gear = 0
        elif self.__gear == 2:
            self.__speed -= 2
            if self.__speed < 20:
                self.__gear = 1
        elif self.__gear == 3:
            self.__speed -= 3
            if self.__speed < 30:
                self.__gear = 2
        elif self.__gear == 4:
            self.__speed -= 4
            if self.__speed < 40:
                self.__gear = 3

    def get_is_on(self):
        return self.__is_on

    def get_speed(self):
        return self.__speed

    def get_gear(self):
        return self.__gear



