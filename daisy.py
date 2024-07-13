class Daisy:
    def __init__(self, color, albedo,graph_color, start_area, optimal_temp=22.5):
        self.color = color
        self.albedo = albedo
        self.area = start_area
        self.temp = 0
        self.temp_data = []
        self.area_data = []
        self.graph_color = graph_color
        self.optimal_temp = optimal_temp

    def update_area(self, dw):
        self.area += dw
    
    def update_temp(self, new_temp):
        self.temp = new_temp

    def record_data(self):
        if (self.area <= 0):
            self.temp = 0
        self.temp_data.append(self.temp - 273)
        self.area_data.append(self.area*100)
