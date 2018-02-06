class port():
    data_type = ""
    direction = ""
    size = 1
    name = ""

    def __init__(self, data_type, direction, size, name):
        self.data_type = data_type
        self.direction = direction
        self.size = size
        self.name = name

    def p(self):
        print("Name: " + self.name)
        if self.direction == 1:
            print("Direction: out")
        elif self.direction == 2:
            print("Direction: inout")
        else:
            print("Direction: in")
        print("Data Type: " + self.data_type)
        print("Size: " + str(self.size))

