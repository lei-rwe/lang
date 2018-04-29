class Mapping:
    def __init__(self, iterable):
        print('Mapping.__init__')
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        print('Mapping.update')
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        print('MappingSubclass.update')
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

if __name__ == '__main__':
    obj = MappingSubclass( range(10) )
    import pdb; pdb.set_trace()
