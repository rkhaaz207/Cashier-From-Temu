import pygame
import sys
from store import QueueSystem, CashierSystem, StockSystem

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Sistem Kasir & Gudang Terintegrasi")

font = pygame.font.SysFont("consolas", 18)
title_font = pygame.font.SysFont("consolas", 22, bold=True)
BG_COLOR, TEXT_COLOR, ALERT_COLOR = (18, 18, 18), (220, 220, 220), (244, 67, 54)

antrean = QueueSystem()
kasir = CashierSystem()
gudang = StockSystem()

pesan_sistem = "Sistem Siap. Coba tambah stok gudang (E) dulu!"
clock = pygame.time.Clock()

while True:
    screen.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pesan_sistem = antrean.tambah()
            elif event.key == pygame.K_w:
                orang = antrean.panggil()
                if orang:
                    kasir.reset()
                    pesan_sistem = f"Melayani {orang}. Keranjang kosong, siap diisi."
                else:
                    pesan_sistem = "Antrean kosong!"
            
            elif event.key == pygame.K_e:
                pesan_sistem = gudang.tambah()

            elif event.key == pygame.K_a: 
                if antrean.data.front is None:
                    pesan_sistem = "Panggil pelanggan (W) dulu!"
                else:
                    barang_dari_gudang = gudang.ambil()
                    if barang_dari_gudang:
                        kasir.data.push(barang_dari_gudang)
                        pesan_sistem = f"Berhasil scan: {barang_dari_gudang} masuk Keranjang."
                    else:
                        pesan_sistem = "GAGAL SCAN! Stok di gudang kosong!"

            elif event.key == pygame.K_s: 
                batal = kasir.batal()
                if batal:
                    gudang.data.push(batal)
                    pesan_sistem = f"Batal: {batal} dikembalikan ke Gudang."
                else:
                    pesan_sistem = "Keranjang sudah kosong!"

    bantuan = [
        "KASIR  : [Q] Tambah Pelanggan | [W] Panggil Pelanggan | [A] Scan Barang | [S] Batal (Retur)",
        "GUDANG : [E] Tambah Stok Gudang (Supplier)"
    ]
    for i, teks in enumerate(bantuan):
        screen.blit(font.render(teks, True, TEXT_COLOR), (20, 20 + (i*25)))

    screen.blit(font.render(pesan_sistem, True, ALERT_COLOR), (20, 90))
    pygame.draw.line(screen, TEXT_COLOR, (20, 120), (980, 120))
    pygame.draw.line(screen, TEXT_COLOR, (20, 240), (980, 240)) 
    
    antrean.draw(screen, font, title_font)
    kasir.draw(screen, font, title_font)
    gudang.draw(screen, font, title_font)
    
    pygame.display.flip()
    clock.tick(30)