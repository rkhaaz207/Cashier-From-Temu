from dynamic import DynamicQueue, DynamicStack

TEXT_COLOR = (220, 220, 220)
QUEUE_COLOR = (76, 175, 80)
STACK_COLOR = (33, 150, 243)
WAREHOUSE_COLOR = (255, 152, 0)

class QueueSystem:
    def __init__(self):
        self.data = DynamicQueue()
        self.no = 1
        
    def tambah(self):
        self.data.enqueue(f"Pelanggan {self.no}")
        self.no += 1
        return f"Pelanggan {self.no - 1} masuk antrean."
        
    def panggil(self):
        return self.data.dequeue()
        
    def draw(self, screen, font, title_font, x, y, title, title_color, text_color):
        screen.blit(title_font.render(title, True, title_color), (x, y))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("Kosong", True, text_color), (x + 20, y + 40))
        else:
            for i, orang in enumerate(items):
                screen.blit(font.render(f"[{orang}]", True, text_color), (x + 20 + (i * 150), y + 40))
                if i < len(items) - 1:
                    screen.blit(font.render("<-", True, title_color), (x + 20 + (i * 150) + 125, y + 40))

class CashierSystem:
    def __init__(self):
        self.data = DynamicStack()
        self.no = 1
        
    def reset(self):
        self.data = DynamicStack()
        self.no = 1
        
    def scan(self):
        self.data.push(f"Item {self.no}")
        self.no += 1
        return f"Item {self.no - 1} masuk keranjang."
        
    def batal(self):
        return self.data.pop()
        
    def draw(self, screen, font, title_font, x, y, title, title_color, text_color):
        screen.blit(title_font.render(title, True, title_color), (x, y))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("Kosong", True, text_color), (x + 20, y + 40))
        else:
            for i, barang in enumerate(items):
                pos_y = y + 40 + (i * 25)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, title_color), (x + 180, pos_y))
                screen.blit(font.render(f"| {barang.ljust(15)} |", True, text_color), (x + 20, pos_y))

class StockSystem:
    def __init__(self):
        self.data = DynamicStack()
        self.no = 1
        
    def tambah(self):
        self.data.push(f"Box-Stok-{self.no}")
        self.no += 1
        return f"Box-Stok-{self.no - 1} ditumpuk di gudang."
        
    def ambil(self):
        return self.data.pop()
        
    def draw(self, screen, font, title_font, x, y, title, title_color, text_color):
        screen.blit(title_font.render(title, True, title_color), (x, y))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("Kosong", True, text_color), (x + 20, y + 40))
        else:
            for i, barang in enumerate(items):
                pos_y = y + 40 + (i * 25)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, title_color), (x + 200, pos_y))
                screen.blit(font.render(f"| {barang.ljust(17)} |", True, text_color), (x + 20, pos_y))