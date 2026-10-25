import pygame
import sys
from store import QueueSystem, CashierSystem, StockSystem

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistem Kasir & Gudang")

font = pygame.font.SysFont("consolas", 18)
title_font = pygame.font.SysFont("consolas", 20, bold=True)
button_font = pygame.font.SysFont("consolas", 16, bold=True)

BG_COLOR = (18, 18, 18)
TEXT_COLOR = (220, 220, 220)
QUEUE_COLOR = (76, 175, 80)
STACK_COLOR = (33, 150, 243)
WAREHOUSE_COLOR = (255, 152, 0)
ALERT_COLOR = (244, 67, 54)
BTN_COLOR = (50, 50, 50)
BTN_HOVER = (100, 100, 100)

antrean = QueueSystem()
kasir = CashierSystem()
gudang = StockSystem()

pesan_sistem = ""
clock = pygame.time.Clock()

def draw_button(screen, text, x, y, w, h, mouse_pos):
    rect = pygame.Rect(x, y, w, h)
    color = BTN_HOVER if rect.collidepoint(mouse_pos) else BTN_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=5)
    pygame.draw.rect(screen, TEXT_COLOR, rect, 2, border_radius=5)
    text_surf = button_font.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect

while True:
    screen.fill(BG_COLOR)
    mouse_pos = pygame.mouse.get_pos()
    
    antrean.draw(screen, font, title_font, 70, 70, "ANTREAN KASIR", QUEUE_COLOR, TEXT_COLOR)
    btn_q = draw_button(screen, "+ Tambah Antrian", 50, 200, 180, 45, mouse_pos)
    btn_w = draw_button(screen, "Panggil Pelanggan", 240, 200, 180, 45, mouse_pos)
    
    kasir.draw(screen, font, title_font, 70, 350, "KERANJANG", STACK_COLOR, TEXT_COLOR)
    btn_a = draw_button(screen, "Scan Barang", 50, 550, 180, 45, mouse_pos)
    btn_s = draw_button(screen, "Cancel Barang", 240, 550, 180, 45, mouse_pos)
    
    gudang.draw(screen, font, title_font, 620, 350, "STOK GUDANG", WAREHOUSE_COLOR, TEXT_COLOR)
    btn_e = draw_button(screen, "Tambah Stok", 620, 550, 180, 45, mouse_pos)

    if pesan_sistem:
        screen.blit(font.render(pesan_sistem, True, ALERT_COLOR), (50, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_q.collidepoint(event.pos):
                pesan_sistem = antrean.tambah()
            elif btn_w.collidepoint(event.pos):
                orang = antrean.panggil()
                if orang:
                    kasir.reset()
                    pesan_sistem = f"Melayani {orang}"
                else:
                    pesan_sistem = "Antrean kosong"
            elif btn_a.collidepoint(event.pos):
                if antrean.data.front is None:
                    pesan_sistem = "Panggil pelanggan dulu"
                else:
                    brg = gudang.ambil()
                    if brg:
                        kasir.data.push(brg)
                        pesan_sistem = f"Scan: {brg}"
                    else:
                        pesan_sistem = "Gudang kosong"
            elif btn_s.collidepoint(event.pos):
                batal = kasir.batal()
                if batal:
                    gudang.data.push(batal)
                    pesan_sistem = f"Batal: {batal}"
                else:
                    pesan_sistem = "Keranjang kosong"
            elif btn_e.collidepoint(event.pos):
                pesan_sistem = gudang.tambah()

    pygame.display.flip()
    clock.tick(30)