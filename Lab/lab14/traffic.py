import time

class TrafficLight:
    def __init__(self):
        self.color = "Red"
        self.timer = 4    

    def tick(self):
        if self.timer <= 0:
            if self.color == "Red":
                self.change_color("Green")
                self.setTimer(3)
            elif self.color == "Green":
                self.change_color("Yellow")
                self.setTimer(2)
            elif self.color == "Yellow":
                self.change_color("Red")
                self.setTimer(4)
        print(f"{self.color} with time remain {self.timer}")
        self.timer -= 1
    
    def setTimer(self, timers):
        self.timer = timers

    def change_color(self, color):
        self.color = color

traffic_light = TrafficLight()
while True:
    traffic_light.tick()
    time.sleep(1)
