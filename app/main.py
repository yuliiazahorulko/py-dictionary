class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = 5
        self.size = 0
        self.dictionary = [None] * self.capacity

    def calculation_algorithm(self, key: str | int, value: str | int) -> None:
        load_factor_index = hash(key) % self.capacity
        if 0 <= load_factor_index < self.capacity:
            index = load_factor_index
        if self.size <= self.threshold and self.dictionary[index] is None:
            self.dictionary[index] = [key, hash(key), value]
            self.size += 1
        elif self.dictionary[index] is not None:
            if self.dictionary[index][1] == hash(key):
                self.dictionary[index][2] = value
            else:
                while True:
                    temp_list = list(range(index + 1, len(self.dictionary))) \
                        + list(range(index))
                    for i in temp_list:
                        if self.dictionary[i] is not None:
                            continue
                        self.dictionary[i] = [key, hash(key), value]
                        self.size += 1
                        break
                    break

    def __setitem__(self, key: str | int, value: str | int) -> None:
        if self.size <= self.threshold:
            self.calculation_algorithm(key, value)
        elif self.size > self.threshold:
            self.dictionary += [None] * self.capacity
            temp = []
            for item in self.dictionary:
                if item is not None:
                    temp.append(item)

            self.capacity = self.capacity * 2
            self.dictionary = [None] * self.capacity
            self.threshold = 2 * self.capacity // 3

            for temp_item in temp:
                self.calculation_algorithm(temp_item[0], temp_item[2])

            self.calculation_algorithm(key, value)

    def __getitem__(self, item: str | int) -> None:
        try:
            if item in self.dictionary:
                return self.dictionary[item][1]
        except KeyError:
            raise KeyError("Key outside the dictionary!")

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f"{{{[key_value for key_value in self.dictionary]}}}"
