class dictionary_iter:
    def __init__(self, sample_dict: dict):
        self.sample_dict = list(sample_dict.items())
        self.current_kvp = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_kvp >= len(self.sample_dict):
            raise StopIteration

        index = self.current_kvp
        self.current_kvp += 1
        return self.sample_dict[index]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
