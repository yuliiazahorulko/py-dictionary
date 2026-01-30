class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.threshold = 5
        self.size = 0
        self.dictionary = [None] * self.capacity

    def calculation_algorithm(self, key: str | int, value: str | int) -> None:
        temp_not_none = [i for i in self.dictionary if i is not None]
        for d_list in temp_not_none:
            if key == d_list[0]:
                d_list[2] = value
                return None
        index = hash(key) % self.capacity
        if self.size <= self.threshold and self.dictionary[index] is None:
            self.dictionary[index] = [key, hash(key), value]
            self.size += 1
        elif self.dictionary[index] is not None:
            if self.dictionary[index][0] == key:
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
        not_empty = [k for k in self.dictionary if k is not None]
        if item in [k[0] for k in self.dictionary if k is not None]:
            return [i[2] for i in not_empty if i[0] == item][0]
        else:
            raise KeyError("Key outside the dictionary!")

    def __len__(self) -> int:
        return len([i for i in self.dictionary if i is not None])

    def __repr__(self) -> str:
        return f"{{{[key_value for key_value in self.dictionary]}}}"
