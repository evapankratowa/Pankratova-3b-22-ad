class Figure:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def print_info(self):
        print(f'Площадь -  {self.area}, периметр - {self.perimeter}')
