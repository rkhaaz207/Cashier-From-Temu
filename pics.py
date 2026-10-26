import pygame

_img_pelanggan = None
_img_box = None

def get_img_pelanggan():
    global _img_pelanggan
    if _img_pelanggan is None:
        try:
            img = pygame.image.load("4143107.png")
            _img_pelanggan = pygame.transform.scale(img, (40, 40))
        except FileNotFoundError:
            _img_pelanggan = pygame.Surface((40, 40))
            _img_pelanggan.fill((255, 100, 100))
    return _img_pelanggan

def get_img_box():
    global _img_box
    if _img_box is None:
        try:
            img = pygame.image.load("13-139411_box-png-free-download-cardboard-box-png-transparent.png")
            _img_box = pygame.transform.scale(img, (30, 30))
        except FileNotFoundError:
            _img_box = pygame.Surface((30, 30))
            _img_box.fill((100, 200, 100))
    return _img_box