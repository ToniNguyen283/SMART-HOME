class SmartDevice:

    def __init__ (self,name):
        '''
        Parent class: Initializes the device with a given name and sets the status to False (off) by default.

        Parameters: name (string) — The name of the device

        Returns: None
        '''
        self.name = name
        self.status = False
    
    def turn_on (self):
        '''
        Turns the device on by setting the status attribute to True.

        Parameters: None

        Returns: None
        '''
        self.status = True
    
    def turn_off (self):
        '''
        Turns the device off by setting the status attribute to False.

        Parameters: None

        Returns: None
        '''
        self.status = False

    def __str__ (self):
        '''
        Returns a string representation of the device, showing the name and its current on/off status.

        Parameters: None

        Returns: str — A string that includes the device name and its current status (i.e., 
        “Living Room Light: ON” or “Living Room Light: OFF”).
        '''
        if self.status:
            return f'{self.name}: ON'
        else:
            return f'{self.name}: OFF'

class Light (SmartDevice):

    def __init__ (self,name):
        '''
        Initializes the device with a given name (inheritance from SmartDevice class) and add a new attribute
        brightness (integer): Represents the brightness level of the light (1 to 100). Default value should be 100.

        Parameters: None

        Returns: None
        '''
        super().__init__(name)
        self.brightness=100
    
    def adjust_brightness (self,level):
        '''
        Adjusts the brightness of the light. The brightness is only changed if the
        level is between 1 and 100 (inclusive). If the level is outside this range, the brightness
        remains unchanged.

        Parameters: level (integer) — The desired brightness level (between 1 and 100).

        Returns: None
        '''
        if 1<=level<=100:
            self.brightness=level
    
    def __str__ (self):
        '''
        Returns a string representation of the light, showing the name, its current
        on/off status, and its brightness level.

        Parameters: None

        Returns: str — A string that includes the device name, its on/off status, and the
        brightness level (e.g., “Living Room Light: ON, Brightness: 75”).
        '''
        return f'{super().__str__()}, Brightness: {self.brightness}'

class Thermostat (SmartDevice):

    def __init__ (self,name):
        '''
        Initializes the device with a given name (inheritance from SmartDevice class) and add a new attribute
        temperature (float): The current temperature setting (in degrees Fahrenheit). Default value
        should be 65.

        Parameters: None

        Returns: None
        '''
        super().__init__ (name)
        self.temperature = 65
    
    def adjust_temperature (self,temp):
        '''
        Adjusts the temperature of the thermostat. It uses the private helper
        method check temperature limits to ensure the temperature is within a reasonable
        range (e.g., 55°F to 80°F). If the temperature is within this range, it updates the
        temperature attribute. If not, it leaves the temperature unchanged.

        Parameters: temp (float) — The desired temperature setting (in degrees Fahrenheit).

        Returns: None
        '''
        if self._check_temperature_limits(temp):
            self.temperature=temp

    def __str__ (self):
        '''
        Returns a string representation of the thermostat, showing the name, its
        current on/off status, and the current temperature.

        Parameters: None

        Returns: str—A string that includes the device name, its on/off status, and the current
        temperature (e.g., “Thermostat: ON, Temperature: 68”).
        '''
        return f'{super().__str__()}, Temperature: {self.temperature}'
    
    def _check_temperature_limits (self,temp):
        '''
        Checks if the given temperature is within the acceptable range. This is a
        private method used internally to validate temperature adjustments.

        Parameters: temp (float) — The desired temperature setting.

        Returns: bool — True if the temperature is within the valid range (e.g., between 55°F
        and 80°F); False otherwise.
        '''
        if 55<=temp<=80:
            return True
        else:
            return False
    
class Speaker (SmartDevice):

    def __init__ (self,name):
        '''
        Initializes the device with a given name (inheritance from SmartDevice class) and add a new attribute
        volume (integer): Represents the volume of the speaker (1 to 10). Default value should be 3.

        Parameters: None

        Returns: None
        '''
        super().__init__(name)
        self.volume = 3
        
    def increase_volume (self):
        '''
        Increases the volume by 1, with a maximum volume of 10.

        Parameters: None

        Returns: None
        '''
        if self.volume<10:
            self.volume+=1
        
    def __str__ (self):
        '''
        Returns a string representation of the speaker, showing the name, its current
        on/off status, and its volume setting.

        Parameters: None

        Returns: str—A string that includes the device name, its on/off status, and the volume
        setting (e.g., “Outdoor Speaker: OFF, Volume: 5”).
        '''
        return f'{super().__str__()}, Volume: {self.volume}'
        
    def decrease_volume (self):
        '''
        Decreases the volume by 1, with a minimum volume of 1.

        Parameters: None

        Returns: None
        '''
        if self.volume>1:
            self.volume-=1
    
class SmartHome:

    def __init__ (self):
        '''
        Create a Smarthome class to manage all the smart devices with a new attribute
        devices (list): A list that stores instances of SmartDevice (lights, thermostats, cameras).

        Parameters: None

        Returns: None
        '''
        self.devices = []
    
    def __add__ (self,other):
        '''
        Overloads the + operator to allow devices to be added to the SmartHome
        instance. This method appends the device to the devices list in the SmartHome.

        Parameters: other (SmartDevice)—An instance of a SmartDevice (e.g., Light, Thermostat,
        or Speaker).

        Returns: None
        '''
        self.devices.append(other)
        return self
    
    def turn_off_all (self):
        '''
        Turns off all devices listed for the smart home instance.

        Parameters: None

        Returns: None
        '''
        for i in self.devices:
            i.turn_off()
    
    def __str__ (self):
        '''
        Returns a string listing the name and status of each device in the SmartHome instance.

        Parameters: None

        Returns: str — A string representation of the statuses of all devices in the smart home,
        showing the name and current status of each device (e.g., “Living Room Light: ON,
        Bedroom Thermostat: OFF”).
        '''
        answer = ''
        for i in self.devices:
            if i.status==True:
                answer+=f'{i.name}: ON, '
            else:
                answer+=f'{i.name}: OFF, '
        return answer.strip(', ')