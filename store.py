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
        
    def draw(self, screen, font, title_font):
        screen.blit(title_font.render("ANTREAN KASIR", True, QUEUE_COLOR), (20, 140))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("- Kosong -", True, TEXT_COLOR), (20, 180))
        else:
            for i, orang in enumerate(items):
                screen.blit(font.render(f"[{orang}]", True, TEXT_COLOR), (20 + (i * 150), 180))
                if i < len(items) - 1:
                    screen.blit(font.render("<-", True, QUEUE_COLOR), (20 + (i * 150) + 125, 180))

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
        
    def draw(self, screen, font, title_font):
        screen.blit(title_font.render("KERANJANG", True, STACK_COLOR), (20, 260))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("- Kosong -", True, TEXT_COLOR), (20, 300))
        else:
            for i, barang in enumerate(items):
                pos_y = 300 + (i * 25)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, STACK_COLOR), (200, pos_y))
                screen.blit(font.render(f"| {barang.ljust(15)} |", True, TEXT_COLOR), (20, pos_y))
            screen.blit(font.render("-------------------", True, TEXT_COLOR), (20, 300 + (len(items) * 25)))

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
        
    def draw(self, screen, font, title_font):
        screen.blit(title_font.render("STOK GUDANG", True, WAREHOUSE_COLOR), (500, 260))
        items = self.data.get_all()
        if not items:
            screen.blit(font.render("- Kosong -", True, TEXT_COLOR), (500, 300))
        else:
            for i, barang in enumerate(items):
                pos_y = 300 + (i * 25)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, WAREHOUSE_COLOR), (700, pos_y))
                screen.blit(font.render(f"| {barang.ljust(17)} |", True, TEXT_COLOR), (500, pos_y))
            screen.blit(font.render("---------------------", True, TEXT_COLOR), (500, 300 + (len(items) * 25)))