import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    def __mul__(self, otro):
        if isinstance(otro, Vector):
            return self.x * otro.x + self.y * otro.y + self.z * otro.z
        else:
            return Vector(self.x * otro, self.y * otro, self.z * otro)
    
    def __xor__(self, otro):
        return Vector(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class AlgebraVectorial:
    @staticmethod
    def perpendicular1(a, b):
        #|a + b| = |a - b|
        return abs((a + b).magnitud() - (a - b).magnitud()) < 1e-10
    
    @staticmethod
    def perpendicular2(a, b):
        #|a - b| = |b - a|
        return abs((a - b).magnitud() - (b - a).magnitud()) < 1e-10
    
    @staticmethod
    def perpendicular3(a, b):
        #a · b = 0
        return abs(a * b) < 1e-10
    
    @staticmethod
    def perpendicular4(a, b):
        #|a + b|² = |a|² + |b|²
        suma = a + b
        return abs(suma.magnitud()**2 - (a.magnitud()**2 + b.magnitud()**2)) < 1e-10
    
    @staticmethod
    def paralelo1(a, b):
        #a = r * b
        if abs(b.magnitud()) < 1e-10:
            return False
        razonx = a.x / b.x if abs(b.x) > 1e-10 else None
        razony = a.y / b.y if abs(b.y) > 1e-10 else None
        razonz = a.z / b.z if abs(b.z) > 1e-10 else None
        razones = [r for r in [razonx, razony, razonz] if r is not None]
        if not razones:
            return False
        return all(abs(r - razones[0]) < 1e-10 for r in razones)
    
    @staticmethod
    def paralelo2(a, b):
        #a × b = 0
        cruz = a ^ b
        return cruz.magnitud() < 1e-10
    
    @staticmethod
    def proyeccion(a, b):
        #Proy_b a = (a·b / |b|²) * b
        if abs(b.magnitud()) < 1e-10:
            return None
        factor = (a * b) / (b.magnitud() ** 2)
        return b * factor
    
    @staticmethod
    def componente(a, b):
        #Comp_b a = (a·b) / |b|
        if abs(b.magnitud()) < 1e-10:
            return None
        return (a * b) / b.magnitud()
        
v1 = Vector(1, 0, 0)
v2 = Vector(0, 1, 0)
#perpendicularidad
print("Perpendicularidad")
print(AlgebraVectorial.perpendicular3(v1, v2))  # True (xq producto punto = 0)

#proyección
print("Proyeccion")
proy = AlgebraVectorial.proyeccion(Vector(3, 4, 0), Vector(1, 0, 0))
print(proy)
