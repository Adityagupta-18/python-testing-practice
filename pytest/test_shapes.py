import pytest
from shapes import Circle,Rectangle
from math import pi

class TestCirle():

    def setup_method(self,method):
        self.circle=Circle(7)

    # def teardown_method(self,method):
    #     pass

    def test_area(self):
        assert self.circle.area()==pi*self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter()==2*pi*self.circle.radius



class TestRectangle():

    @pytest.fixture
    def rectangle(self):
        return Rectangle(10,45)

    def test_area_rectangle(self,rectangle):
        assert rectangle.area()==rectangle.length*rectangle.breadth

    def test_perimeter(self,rectangle):
        assert rectangle.perimeter()==2*(rectangle.length+rectangle.breadth)

