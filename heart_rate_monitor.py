''' Heart rate monitor program software testing

    language: python
    version: 3.5.2
'''

import random
import sys, time

class Monitor:
    def __init__(self, pulse_start, oxygen_start, blood_low, blood_high):
        self.pulse = pulse_start
        self.oxygen = oxygen_start
        self.blood_low = blood_low
        self.blood_high = blood_high

    def step(self):
        self.pulse += random.uniform(-5, 5)
        if(self.pulse < 0.0):
            self.pulse = 0.0
        self.oxygen += random.uniform(-3, 3)
        if(self.oxygen > 100.0):
            self.oxygen = 100.0
        self.blood_low += random.uniform(-5, 5)
        if(self.blood_low < 40.0):
            self.blood_low = 40.0
        elif(self.blood_low > 100.0):
            self.blood_low = 100.0
        self.blood_high += random.uniform(-5, 5)
        if(self.blood_high < 70.0):
            self.blood_high = 70.0
        elif(self.blood_high > 200):
            self.blood_high = 200

    def print_values(self):
        # Prints over last line if possible
        print(str(round(self.pulse)) + " , " + str(round(self.oxygen)) + " , " +
            str(round(self.blood_low)) + " , " + str(round(self.blood_high)), end="\r")

    def check_values(self):
        pulse_feedback = self.check_pulse()
        oxygen_feedback = self.check_oxygen()
        blood_pressure_feedback = self.check_blood_pressure()
        if(pulse_feedback != "normal"):
            print('\n')
            print('pulse:' + pulse_feedback)
        if(oxygen_feedback != "normal"):
            print('\n')
            print('oxygen:' + oxygen_feedback)
        if(blood_pressure_feedback != "normal"):
            print('\n')
            print('blood pressure:' + blood_pressure_feedback)

    def check_pulse(self):
        # print(self.pulse)
        if(self.pulse >= 60.0 and self.pulse <= 100.0):
            return "normal"
        elif(self.pulse > 100.0 and self.pulse <= 130.0):
            return "high"
        elif(self.pulse > 130.0):
            return "very high"
        elif(self.pulse < 60.0 and self.pulse >= 40.0):
            return "low"
        elif(self.pulse < 40.0):
            return "very low"

    def check_oxygen(self):
        if(self.oxygen < 80.0):
            return "very low"
        elif(self.oxygen < 90.0):
            return "low"
        else:
            return "normal"

    def check_blood_pressure(self):
        ''' http://www.bloodpressureuk.org/BloodPressureandyou/Thebasics/Bloodpressurechart
        '''
        if(self.blood_low < 60.0):
            if(self.blood_high < 90.0):
                return "low"
            elif(self.blood_high < 120.0):
                return "normal"
            elif(self.blood_high < 140.0):
                return "high"
            else:
                return "very high"
        elif(self.blood_low < 80.0):
            if(self.blood_high < 120.0):
                return "normal"
            elif(self.blood_high < 140.0):
                return "high"
            else:
                return "very high"
        elif(self.blood_low < 90.0):
            if(self.blood_high < 140.0):
                return "high"
            else:
                return "very high"
        else:
            return "very high"

    def run(self):
        i = 0
        print("Pulse, Oxygen level, lower blood pressure, higher blood pressure")
        while(i < 5):
            self.step()
            self.print_values()
            self.check_values()
            time.sleep(0.3)
            i += 1
        sys.stdout.write("\n")
if __name__ == '__main__':
    monitor = Monitor(70.0, 90.0, 70.0, 100.0)
    monitor.run()
