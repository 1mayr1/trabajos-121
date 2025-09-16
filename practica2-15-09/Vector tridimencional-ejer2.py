import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    # suma: a + b
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    #escalar: r * a
    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vector(self.x * escalar, self.y * escalar, self.z * escalar)
        return NotImplemented
    
    # escalar * vector (multiplicación por la izquierda)
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    #magnitud 
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    #normalizado
    def normalizar(self):
        mag = self.magnitud()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.x / mag, self.y / mag, self.z / mag)
    
    # producto punto
    def productopunto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
     
    # Producto cruz
    def productocruz(self, otro):
        return Vector(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    
    #operador^para producto cruz
    def __xor__(self, otro):
        return self.productocruz(otro)
   
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    #comparaciones
    def __eq__(self, otro):
        return (abs(self.x - otro.x) < 1e-10 and 
                abs(self.y - otro.y) < 1e-10 and 
                abs(self.z - otro.z) < 1e-10)

class AlgebraVectorial:
    #|a + b| = |a - b|
    @staticmethod
    def perpendicular1(a, b):
        return abs((a + b).magnitud() - (a - b).magnitud()) < 1e-10
    
    #|a - b| = |b - a|
    @staticmethod
    def perpendicular2(a, b):
        return abs((a - b).magnitud() - (b - a).magnitud()) < 1e-10
    
    #a · b = 0
    @staticmethod
    def perpendicular3(a, b):
        return abs(a.productopunto(b)) < 1e-10
    
    #|a + b|² = |a|² + |b|²
    @staticmethod
    def perpendicular4(a, b):
        suma = a + b
        return abs(suma.magnitud()**2 - (a.magnitud()**2 + b.magnitud()**2)) < 1e-10
    
    #a = r * b
    @staticmethod
    def paralelo1(a, b):
        if b.magnitud() == 0:
            return a.magnitud() == 0
        
        #a es múltiplo escalar de b
        if b.x != 0: razon_x = a.x / b.x
        else: razonx = None
        
        if b.y != 0: razon_y = a.y / b.y
        else: razony = None
        
        if b.z != 0: razon_z = a.z / b.z
        else: razonz = None
        
        razones = [r for r in [razonx, razony, razonz] if r is not None]
        
        if not razones: 
            return a.magnitud() == 0
        
        return all(abs(r - razones[0]) < 1e-10 for r in razones)
    
    #a × b = 0
    @staticmethod
    def paralelo2(a, b):
        cruz = a ^ b
        return cruz.magnitud() < 1e-10
    
    #Proy_b a = (a·b / |b|²) * b
    @staticmethod
    def proyeccion(a, b):
        if abs(b.magnitud()) < 1e-10:
            return None
        factor = a.productopunto(b) / (b.magnitud() ** 2)
        return b * factor
    
    #Comp_b a = (a·b) / |b|
    @staticmethod
    def componente(a, b):
        if abs(b.magnitud()) < 1e-10:
            return None
        return a.productopunto(b) / b.magnitud()

a = Vector(1, 2, 3)
b = Vector(4, 2, 1)
c = Vector(1, 0, 1)  
print("Vectores:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
   
print("Operaciones:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"2 * a = {2 * a}")
print(f"a * 3 = {a * 3}")
print(f"Magnitud de a: {a.magnitud():.2f}")
print(f"Producto punto a·b: {a.productopunto(b)}")
print(f"Producto cruz a×b: {a ^ b}")

print("¿Es perpendicular?")
print(f"a y b (método 3): {AlgebraVectorial.perpendicular3(a, b)}")
print(f"a y c (método 3): {AlgebraVectorial.perpendicular3(a, c)}")
    
proy = AlgebraVectorial.proyeccion(a, b)
comp = AlgebraVectorial.componente(a, b)
print(f"Proyección de a sobre b: {proy}")
print(f"Componente de a en b: {comp:.2f}")
