class Triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time


def print_details(self):
    print(f"{self.first_name} {self.last_name} {self.location} {self.swim_time} {self.cycle_time} {self.run_time} {self.total_time}")


a1 = Triathlon("A", "B", "Los Angeles", 20.5, 30.4, 25.2)
print_details(a1)