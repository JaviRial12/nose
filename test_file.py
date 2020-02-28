class Foo:
    
    def hola(self):
        return "hola"
import unittest 
class FooTestCase(unittest.TestCase):

    def test_hola(self):
        """El metodo hola devuelve hola "hola" """
        assert Foo().hola() == "hola", "Debe devolver hola"
class FooTestMal(unittest.TestCase):

     def test_hola(self):
        """El metodo hola devuelve hola "hola" """
        assert Foo().hola() == "adios", "Debe devolver hola"