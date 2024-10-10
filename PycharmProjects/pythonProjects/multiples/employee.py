from random import randint

class Employee:
    def __init__(self, name: str, age: int, role: str) -> None:
        self.__id = self.generate_id()
        self.__name = name.capitalize()
        self.__age = age
        self.__role = role

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, value):
        if value < 0:
            raise ValueError("Invalid age")
        self.__age = value

    @staticmethod
    def generate_id():
        return "011" + str(randint(1, 100))

    def __str__(self):
        return f"""
Id: {self.__id}
Name: {self.__name}
Age: {self.__age}
Role: {self.__role}
"""



