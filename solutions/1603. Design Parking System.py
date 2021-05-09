class ParkingSystem:
​
    def __init__(self, big: int, medium: int, small: int):
        self.d = [big, medium, small]
​
    def addCar(self, carType: int) -> bool:
        self.d[carType - 1] -= 1
        return self.d[carType - 1] >= 0
    
            
​
            
​
​
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
