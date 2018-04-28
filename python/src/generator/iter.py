class Slicer:
    def __getitem__(self, index): print(index)
    def __getslice__(self, i, j): print(i, j)
    def __setslice__(self, i, j,seq): print(i, j,seq)

Slicer()[1]
Slicer()[1:9]
Slicer()[1:9:2]
