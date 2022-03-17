class Methods_list:
    list_ = []

    def get(self):
        return self.list_

    def create(self):
        pass

    def add(self, data):
        self.list_.append(data)

    def remove(self, id_, key):
        item = self.search_for(id_, key)
        self.list_.pop(item)

    def search_for(self, id_, key):
        item = [item for item in self.list_ if item[key] == id_][0]
        return item
