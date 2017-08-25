class Map:

    def __init__(self):
        n = 18
        self.map_tiles = [[[(k,j,i) for k in range(n)] for j in range(n)] for i in range(n)]
        print(self.map_tiles)




if __name__ == "__main__":
    Map()