import unittest
from datetime import datetime

# Entity class to manage a single record of energy consumption
class EnergyConsumption:
    def __init__(self, energy_id, data_center_id, consumption_value, timestamp=None):
        self.energy_id = energy_id
        self.data_center_id = data_center_id
        self.consumption_value = consumption_value
        self.timestamp = timestamp or datetime.now()

# Entity class to represent a suggested energy-saving measure
class EnergySavingMeasure:
    def __init__(self, measure_id, description, effectiveness):
        self.measure_id = measure_id
        self.description = description
        self.effectiveness = effectiveness

# Manager class for managing CRUD operations related to energy consumption
class EnergyConsumptionManager:
    def __init__(self):
        self.energy_consumptions = {}  # Store energy consumption records in a dictionary

    # Create a new energy consumption record
    def add_energy_consumption(self, energy_id, data_center_id, consumption_value):
        new_consumption = EnergyConsumption(energy_id, data_center_id, consumption_value)
        self.energy_consumptions[energy_id] = new_consumption
        return new_consumption

    # Read/Retrieve energy consumption by ID
    def get_energy_consumption(self, energy_id):
        return self.energy_consumptions.get(energy_id)

    # Update an energy consumption record
    def update_energy_consumption(self, energy_id, new_value):
        if energy_id in self.energy_consumptions:
            self.energy_consumptions[energy_id].consumption_value = new_value
            return True
        return False

    # Delete an energy consumption record
    def delete_energy_consumption(self, energy_id):
        if energy_id in self.energy_consumptions:
            del self.energy_consumptions[energy_id]
            return True
        return False

# Manager class for handling CRUD operations related to energy-saving measures
class EnergySavingMeasureManager:
    def __init__(self):
        self.measures = {}  # Store energy-saving measures

    # Add a new energy-saving measure
    def add_measure(self, measure_id, description, effectiveness):
        new_measure = EnergySavingMeasure(measure_id, description, effectiveness)
        self.measures[measure_id] = new_measure
        return new_measure

    # Get a specific energy-saving measure by its ID
    def get_measure(self, measure_id):
        return self.measures.get(measure_id)

    # Delete an energy-saving measure
    def delete_measure(self, measure_id):
        if measure_id in self.measures:
            del self.measures[measure_id]
            return True
        return False

# Unit testing using Python's unittest framework
class TestEnergyConsumptionManager(unittest.TestCase):

    def setUp(self):
        self.manager = EnergyConsumptionManager()

    def test_add_energy_consumption(self):
        record = self.manager.add_energy_consumption(1, 'DC1', 500)
        self.assertEqual(record.energy_id, 1)
        self.assertEqual(record.consumption_value, 500)

    def test_get_energy_consumption(self):
        self.manager.add_energy_consumption(2, 'DC2', 600)
        record = self.manager.get_energy_consumption(2)
        self.assertIsNotNone(record)
        self.assertEqual(record.data_center_id, 'DC2')

    def test_update_energy_consumption(self):
        self.manager.add_energy_consumption(3, 'DC3', 700)
        self.manager.update_energy_consumption(3, 800)
        record = self.manager.get_energy_consumption(3)
        self.assertEqual(record.consumption_value, 800)

    def test_delete_energy_consumption(self):
        self.manager.add_energy_consumption(4, 'DC4', 900)
        self.assertTrue(self.manager.delete_energy_consumption(4))
        self.assertIsNone(self.manager.get_energy_consumption(4))

class TestEnergySavingMeasureManager(unittest.TestCase):

    def setUp(self):
        self.manager = EnergySavingMeasureManager()

    def test_add_measure(self):
        measure = self.manager.add_measure(1, "Use LED lights", 0.15)
        self.assertEqual(measure.measure_id, 1)
        self.assertEqual(measure.effectiveness, 0.15)

    def test_get_measure(self):
        self.manager.add_measure(2, "Optimize cooling system", 0.25)
        measure = self.manager.get_measure(2)
        self.assertIsNotNone(measure)
        self.assertEqual(measure.description, "Optimize cooling system")

    def test_delete_measure(self):
        self.manager.add_measure(3, "Turn off idle servers", 0.35)
        self.assertTrue(self.manager.delete_measure(3))
        self.assertIsNone(self.manager.get_measure(3))

if __name__ == '__main__':
    unittest.main()
