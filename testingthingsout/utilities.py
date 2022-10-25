from turtle import update
import pygame as pg
from generator import get_captcha_image


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROWS, COLS = 28, 28



pg.init()
screen = pg.display.set_mode((600, 400))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

# Fonts
OPEN_SANS = "assets/fonts/OpenSans-Regular.ttf"
smallFont = pg.font.Font(OPEN_SANS, 20)
largeFont = pg.font.Font(OPEN_SANS, 40)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


class CaptchaBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.solution = get_captcha_image(4)
        self.imp = pg.image.load("out.png").convert()
        self.resetButton = pg.Rect(x, y+100, w, h)
        self.resetText = smallFont.render("Reset", True, BLACK)
        self.resetTextRect = self.resetText.get_rect()
        self.resetTextRect.center = self.resetButton.center

    def update(self):
        # Resize the box if the text is too long.
        self.solution = get_captcha_image(4)
        self.imp = pg.image.load("out.png").convert()
        
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.resetButton.collidepoint(event.pos):
            self.update()
            pg.time.wait(100)
        

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.imp, self.rect)
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        pg.draw.rect(screen, WHITE, self.resetButton)
        screen.blit(self.resetText, self.resetTextRect)



def main():
    clock = pg.time.Clock()
    box = InputBox(350, 100, 140, 32)
    cbox = CaptchaBox(100, 100, 160, 60)
    noMatchBox = pg.Rect(350, 150, 100, 32)
    matchBox = pg.Rect(450, 150, 100, 32)
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            box.handle_event(event)
            cbox.handle_event(event)
            if event.type == pg.MOUSEWHEEL:
              cbox.update()

        box.update()
        screen.fill((30, 30, 30))
        box.draw(screen)
        cbox.draw(screen)
        if box.text == cbox.solution:
            pg.draw.rect(screen, GREEN, matchBox)
        else:
            pg.draw.rect(screen, RED, noMatchBox)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()