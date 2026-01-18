class Calling:
    def feature1(self):
        print("Calling feature")

class Camera:
    def feature2(self):
        print("Camera feature")

class SmartPhone(Calling, Camera):
    def explore(self):
        print("Exploring SmartPhone features")

phone = SmartPhone()
phone.feature1()
phone.feature2()
phone.explore()
