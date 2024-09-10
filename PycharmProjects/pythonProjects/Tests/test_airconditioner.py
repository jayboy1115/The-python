import unittest
from airconditioner import AirConditioner

class AirConditionerTest(unittest.TestCase):
    def setUp(self):
        self.airconditioner = AirConditioner()
        self.airconditioner.turn_on()

    def test_ac_can_be_turned_on(self):
        self.assertTrue(self.airconditioner.is_on())

    def test_ac_can_be_turned_off(self):
        self.airconditioner.turn_off()
        self.assertFalse(self.airconditioner.is_on())

    def test_temperature_increases_when_increased(self):
        self.airconditioner.increase_temperature()
        self.assertGreater(self.airconditioner.get_temperature(), 16)

    def test_temperature_decreases_when_decreased(self):
        self.airconditioner.increase_temperature()
        self.airconditioner.decrease_temperature()
        self.assertEqual(self.airconditioner.get_temperature(), 16)

    def test_temperature_limit_when_increased_beyond_30(self):
        self.airconditioner.temperature = 30
        self.airconditioner.increase_temperature()
        self.assertEqual(self.airconditioner.get_temperature(), 30)

    def test_temperature_limit_when_decreased_below_16(self):
        self.airconditioner.temperature = 16
        self.airconditioner.decrease_temperature()
        self.assertEqual(self.airconditioner.get_temperature(), 16)

if __name__ == '__main__':
    unittest.main()
