# Question 1: Abstract class SmartDevice with constructor, abstract method operate(), and concrete method show_status()

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_name):
        self.device_name = device_name
        self.__is_on = False

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self.device_name} is {status}")

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def is_on(self):
        return self.__is_on

# Question 2: Implement SmartLight, SmartFan, SmartAC using inheritance and encapsulation

class SmartLight(SmartDevice):
    def __init__(self, device_name):
        super().__init__(device_name)
        self.__brightness = 0

    def operate(self):
        self.turn_on()
        self.set_brightness(70)
        print(f"{self.device_name} turned on with brightness {self.__brightness}%")

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.__brightness = level
        else:
            print("Brightness should be between 0 and 100")

    def get_brightness(self):
        return self.__brightness

class SmartFan(SmartDevice):
    def __init__(self, device_name):
        super().__init__(device_name)
        self.__speed = "off"

    def operate(self):
        self.turn_on()
        self.set_speed("medium")
        print(f"{self.device_name} turned on with speed {self.__speed}")

    def set_speed(self, speed):
        if speed.lower() in ["low", "medium", "high"]:
            self.__speed = speed.lower()
        else:
            print("Speed must be 'low', 'medium', or 'high'")

    def get_speed(self):
        return self.__speed

class SmartAC(SmartDevice):
    def __init__(self, device_name):
        super().__init__(device_name)
        self.__temperature = 0

    def operate(self):
        self.turn_on()
        self.set_temperature(24)
        print(f"{self.device_name} turned on with temperature {self.__temperature}°C")

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Temperature should be between 16°C and 30°C")

    def get_temperature(self):
        return self.__temperature

# Question 3: Demonstrate the usage

# Create objects
light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
ac = SmartAC("Office AC")

# Call operate() and show_status()
light.operate()
light.show_status()

fan.operate()
fan.show_status()

ac.operate()
ac.show_status()

# Question 4: Attempt to directly modify private attributes (should raise AttributeError)
print("\nTrying to access private attributes directly:")
try:
    print(light.__brightness)
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(fan.__speed)
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(ac.__temperature)
except AttributeError as e:
    print(f"Error: {e}")

# Question 5: Use setters and getters
print("\nUsing setters and getters to modify and view internal states:")
light.set_brightness(85)
print(f"Updated Brightness: {light.get_brightness()}%")

fan.set_speed("high")
print(f"Updated Fan Speed: {fan.get_speed()}")

ac.set_temperature(22)
print(f"Updated Temperature: {ac.get_temperature()}°C")
