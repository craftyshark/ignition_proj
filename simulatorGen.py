import csv
import random

class Simulator:
    def __init__(self, num_records, filename):
        self.num_records = num_records
        self.filename = filename
        self.tank_level = 50.0
        self.pump_status = 0

    def change_pump_status(self):
        """Changes pump status based on tank level."""
        if self.pump_status == 0 and self.tank_level <= 50:
            self.pump_status = 1
        elif self.pump_status == 1 and self.tank_level >= 100:
            self.pump_status = 0

    def update_tank_level(self):
        """Updates tank level based on pump status."""
        if self.pump_status == 0:
            self.tank_level -= random.uniform(0.1, 0.5)  # level decreases
        else:
            self.tank_level += random.uniform(0.1, 0.5)  # level increases
        self.tank_level = max(0, min(100, self.tank_level))  # ensures tank level is within [0, 100]

    def generate_data(self):
        """Generates the data and writes it to a CSV file."""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Tank Level", "Pump Status"])  # writing header row
            for i in range(self.num_records):
                self.change_pump_status()
                self.update_tank_level()
                writer.writerow([i, round(self.tank_level, 2), self.pump_status])

# Usage
simulator = Simulator(num_records=1000, filename='simulator_data.csv')
simulator.generate_data()
