import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def Felsz(self):
        return 4 * math.pi * self.radius ** 2
    
    def Terf(self):
        return 4 / 3 * math.pi * self.radius ** 3
    
    def __str__(self):
        return f"Kör sugara {self.radius}"
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius


class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        
    def terulet(self):
        return math.pi * self.major_axis * self.minor_axis
    
    def kerulet(self):
        a, b = self.major_axis / 2, self.minor_axis / 2
        return 2 * math.pi * math.sqrt((a**2 + b**2) / 2)
    
    def __str__(self):
        return f"Elipszis főtengelye {self.major_axis} és a kistengelye {self.minor_axis}"

def main():
    Gömb = Sphere(5)
    Elipszis = Ellipse(10,14)
    
    
if __name__ == "__main__":
    main()
