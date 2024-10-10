import unittest

from pythonProjects.multiples.automatic_bike import AutomaticBike


class TestAutomaticBike(unittest.TestCase):
    def test_new_bike_is_off(self):
        bike = AutomaticBike()
        self.assertFalse(bike.get_is_on())

    def test_new_bike_gear_is_zero(self):
        bike = AutomaticBike()
        self.assertEqual(bike.get_gear(), 0)

    def test_new_bike_speed_is_zero(self):
        bike = AutomaticBike()
        self.assertEqual(bike.get_speed(), 0)

    def test_turn_on_bike(self):
        bike = AutomaticBike()
        bike.turn_on()
        self.assertTrue(bike.get_is_on())

    def test_turn_off_bike(self):
        bike = AutomaticBike()
        bike.turn_on()
        bike.turn_off()
        self.assertFalse(bike.get_is_on())

    def test_accelerate_bike(self):
        bike = AutomaticBike()
        bike.turn_on()
        bike.accelerate()
        self.assertEqual(bike.get_speed(), 1)
        self.assertEqual(bike.get_gear(), 1)

    def test_decelerate_bike(self):
        bike = AutomaticBike()
        bike.turn_on()
        bike.accelerate()
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 0)

    def test_multiple_accelerations(self):
        bike = AutomaticBike()
        bike.turn_on()
        for _ in range(5):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 5)
        self.assertEqual(bike.get_gear(), 1)

    def test_multiple_decelerations(self):
        bike = AutomaticBike()
        bike.turn_on()
        bike.accelerate()
        bike.accelerate()
        bike.decelerate()
        bike.decelerate()
        self.assertEqual(bike.get_speed(), 0)
        self.assertEqual(bike.get_gear(), 0)

    def test_gear_shift(self):
        bike = AutomaticBike()
        bike.turn_on()
        for _ in range(21):
            bike.accelerate()
        self.assertEqual(bike.get_speed(), 22)
        self.assertEqual(bike.get_gear(), 2)
