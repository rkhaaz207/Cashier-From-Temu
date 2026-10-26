import pygame
from dynamic import DynamicQueue, DynamicStack
import pics

class QueueSystem:
    def __init__(self):
        self.data = DynamicQueue()
        self.no = 1
        
    def tambah(self):
        self.data.enqueue(f"P-{self.no}")
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
            img_pelanggan = pics.get_img_pelanggan()
            for i, orang in enumerate(items):
                pos_x = x + 20 + (i * 90)
                pos_y = y + 40
                
                screen.blit(img_pelanggan, (pos_x, pos_y))
                screen.blit(font.render(orang, True, text_color), (pos_x, pos_y + 45))
                
                if i < len(items) - 1:
                    screen.blit(font.render("<-", True, title_color), (pos_x + 60, pos_y + 10))

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
            img_box = pics.get_img_box()
            for i, barang in enumerate(items):
                pos_y = y + 40 + (i * 35)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, title_color), (x + 130, pos_y + 5))
                
                screen.blit(img_box, (x + 20, pos_y))
                screen.blit(font.render(f" {barang}", True, text_color), (x + 60, pos_y + 5))

class StockSystem:
    def __init__(self):
        self.data = DynamicStack()
        self.no = 1
        
    def tambah(self):
        self.data.push(f"Stok-{self.no}")
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
            img_box = pics.get_img_box()
            for i, barang in enumerate(items):
                pos_y = y + 40 + (i * 35)
                if i == 0:
                    screen.blit(font.render("<- TOP", True, title_color), (x + 150, pos_y + 5))
                
                screen.blit(img_box, (x + 20, pos_y))
                screen.blit(font.render(f" {barang}", True, text_color), (x + 60, pos_y + 5))