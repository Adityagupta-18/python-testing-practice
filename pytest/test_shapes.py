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

    @pytest.mark.parametrize("radius,perimeter_expected",[(5,31.41592653589793),(7,43.982297150257104)])
    def test_perimeter_param(self,radius,perimeter_expected):
        assert Circle(radius).perimeter()==perimeter_expected



class TestRectangle():

    @pytest.fixture
    def rectangle(self):
        return Rectangle(10,45)

    def test_area_rectangle(self,rectangle):
        assert rectangle.area()==rectangle.length*rectangle.breadth

    def test_perimeter(self,rectangle):
        assert rectangle.perimeter()==2*(rectangle.length+rectangle.breadth)

    @pytest.mark.parametrize("length,breadth,expected_area",[(12,5,60),(5,5,25),(10,30,300)])
    def test_area_rect_para(self,length,breadth,expected_area):
        assert Rectangle(length,breadth).area()==expected_area