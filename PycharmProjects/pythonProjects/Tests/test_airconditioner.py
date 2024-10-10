import unittest

from pythonProjects.multiples.airconditioner import AirConditioner


class AirConditionerTest(unittest.TestCase):
    def test_ac_is_off_initially(self):
        ac = AirConditioner()
        self.assertFalse(ac.check_status())

    def test_turn_on_ac(self):
        ac = AirConditioner()
        ac.turn_on()
        self.assertTrue(ac.check_status())

    def test_turn_off_ac(self):
        ac = AirConditioner()
        ac.turn_on()
        ac.turn_off()
        self.assertFalse(ac.check_status())

    def test_increase_temperature(self):
        ac = AirConditioner()
        ac.turn_on()
        initial_temperature = ac.get_temperature()
        ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), initial_temperature + 1)

    def test_decrease_temperature(self):
        ac = AirConditioner()
        ac.turn_on()
        ac.increase_temperature()
        initial_temperature = ac.get_temperature()
        ac.decrease_temperature()
        self.assertEqual(ac.get_temperature(), initial_temperature - 1)

    def test_temperature_limit_when_increased_beyond_30(self):
        ac = AirConditioner()
        ac.turn_on()
        ac.temperature = 30
        ac.increase_temperature()
        self.assertEqual(ac.get_temperature(), 30)

    def test_temperature_limit_when_decreased_below_16(self):
        ac = AirConditioner()
        ac.turn_on()
        ac.temperature = 16
        ac.decrease_temperature()
        self.assertEqual(ac.get_temperature(), 16)



