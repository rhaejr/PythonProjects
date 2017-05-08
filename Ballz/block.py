class Block:
    def __init__(self, x, y ,color, hits=1):
        self.x = x
        self.y = y
        self.w = block_size
        self.h = block_size
        self.color = color
        self.hits = hits

    def draw(self):
        if self.hits <= 0:
            self.destroy()
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.w, self.h])

    def destroy(self):
        self.color = background