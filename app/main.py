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
        else:
            raise KeyError
        if self.size <= self.threshold and self.dictionary[index] is None:
            self.dictionary[index] = [key, value]
        elif self.dictionary[index] is not None:
            if self.dictionary[index][0] == key:
                self.dictionary[index][1] = value
            else:
                while True:
                    temp_list = list(range(index + 1, len(self.dictionary))) \
                        + list(range(index))
                    for i in temp_list:
                        if self.dictionary[i] is not None:
                            continue
                        self.dictionary[i] = [key, value]
                        break
                    break

    def __setitem__(self, key: str | int, value: str | int) -> None:
        self.size += 1
        if self.size <= self.threshold:
            self.calculation_algorithm(key, value)
        elif self.size > self.threshold:
            self.dictionary += [None] * self.capacity
            self.capacity = self.capacity * 2
            self.threshold = 2 * self.capacity // 3
            self.calculation_algorithm(key, value)

    def __getitem__(self, item: str | int) -> None:
        try:
            if item in self.dictionary:
                return self.dictionary[item]
        except KeyError:
            raise KeyError

    def __len__(self) -> int:
        return len(self.dictionary)

    def __repr__(self) -> str:
        return f"{{{[key_value for key_value in self.dictionary]}}}"
