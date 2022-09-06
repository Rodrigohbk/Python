import math

class Triangulo:

    
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimetro(self):
        return (self.a + self.b + self.c)

    def tipo_lado(self):            #VERIFICA TIPO DE TRIANGULO
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        
        if (self.a == self.b and self.a != self.c) or (
            self.a == self.c and self.a != self.b) or (
            self.b == self.c and self.b != self.a):

            return 'isósceles'

        if self.a != self.b and self.b != self.c and self.a != self.c:

            return 'escaleno'

    def verifica_triangulo(self):

    #   Verifica valor positivos e 
    # se o valores informados respeitam a desigualdade
    #  triangular:
    #    | b - c | < a < b + c
    #    | a - c | < b < a + c
    #    | a - b | < c < a + b
       

        if  self.a > 0 and self.b > 0 and self.c > 0:
            
            if ((math.fabs((self.b - self.c)) < self.a) and (  
                self.a < (self.b + self.c))) or (              
                (math.fabs((self.a - self.c)) < self.b) and (   
                self.b < (self.a + self.c))) or (               
                (math.fabs((self.a - self.b)) < self.c) and (
                self.c < (self.a + self.b))):

                return True
            
            else:
                print("Não compre desigualdade triangular!")
                return False
        else:
            print("Apresenta valor negativo!")
            return False

    def retangulo(self):
                              
        Triangulo.verifica_triangulo(self)
        
        a_aux = self.a
        b_aux = self.b
        c_aux = self.c

        if self.a > self.b and self.a > self.c:
            
            if (a_aux**2) == ((b_aux**2) + (c_aux**2)):
                return True
            
        if self.b > self.a and self.b > self.c:

            if (b_aux**2) == ((a_aux**2) + (c_aux**2)):

                return True

        if self.c > self.a and self.c > self.b:

            if (c_aux**2) == ((a_aux**2) + (b_aux**2)):

                return True

        return False


    def semelhantes(self, t2):

        Triangulo.verifica_triangulo(self)
        Triangulo.verifica_triangulo(t2)
        
        if (self.a / t2.a == self.b/t2.b) and (
            self.b / t2.b == self.c/t2.c):

            return True
        else:
            return False
    

class TestClasse:

    def test_verifica(self):

        triangulo = Triangulo(4, 12, 9)
        assert triangulo.verifica_triangulo() == True

    def test_triangulo_retangulo(self):

        triangulo = Triangulo(3, 5, 4)
        assert triangulo.retangulo() == True

    def test_triangulo_escaleno(self):

        triangulo = Triangulo(3, 5, 4)
        assert triangulo.tipo_lado() == 'escaleno'

    def test_triangulo_equilatero(self):

        triangulo = Triangulo(5, 5, 5)
        assert triangulo.tipo_lado() == 'equilátero'

    def test_triangulo_isosceles(self):

        triangulo = Triangulo(3.61, 3.61, 4)
        assert triangulo.tipo_lado() == 'isósceles'

    def test_triangulo_semelhanca(self):

        triangulo_1 = Triangulo(4, 6, 8)
        triangulo_2 = Triangulo(2, 3, 4)
        
        assert triangulo_1.semelhantes(triangulo_2) == True
        







        
