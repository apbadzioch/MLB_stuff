from utils import reverse_name

class Pitcher:
    def __init__(self, name, dataset):
        self.name == name
        self,data = dataset[dataset['last_name', 'first_name'] == name]
        if self.data.empty:
            raise ValueError(f'{reverse_name(name)} is not in the database.')