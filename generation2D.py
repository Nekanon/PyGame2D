import random

class structure():
    def __init__(self):
        self.dict_type = {1: "поле",
                          2: "Кирпичная стена",
                          3: "Бетонная стена",
                          4: "Вода"}
    def set_type(self, type):
        self.type = type
    def get_type(self):
        return self.type

class generator():
    def __init__(self, level, size):
        self.level = level
        self.size = size

    def __generate_iteration(self, matrix, border, iterators):
        for time in range(0, iterators):
            for i in range(1, self.size-1):
                for j in range(1, self.size-1):
                    count = 0
                    for i1 in range(-1, 2):
                        for j1 in range(-1, 2):
                            if i == j:
                                continue
                            if matrix[i+i1][j+j1] == type:
                                count += 1
                    if count >= border:
                        matrix[i][j] = type
        return matrix

    def __generate_layer(self, out, percent, type):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if random.random() < percent:
                    out[i][j] = type
        self.__generate_iteration(out, 2, 4)
        return out

    def mapGenerate(self):
        out = []
        for i in range(0, self.size):
            out1 = []
            for j in range(0, self.size):
                    out1.append(1)
            out.append(out1)
        for i in range(4, 1, -1):
            out = self.__generate_layer(out, (0.025*float(self.level)), i)
        return out

    def enemyGeneration(self):
            return 1