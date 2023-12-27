import pygame
from userCommunication import create_message
from constants import SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE, SCREEN_BACKGROUND_COLOR, SCREEN_BORDER, TICK, DIALOG_FONT


pygame.init()
clock = pygame.time.Clock()

# Screen
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGTH])
screen_background = pygame.image.load("./Images/hintergrund.png")

font = pygame.font.Font(DIALOG_FONT, 24)
snip1 = font.render("", True, "white")
text_counter = 0
text_speed = 3
level = 1


def draw_screen() -> None:
    screen.blit(screen_background, (0, 0))
    pygame.display.update()


# ++++++++++++++++++++++++++++++++++ Game loop +++++++++++++++++++++++++++++++++++++++
run = True
while run:
    pygame.draw.rect(screen, SCREEN_BACKGROUND_COLOR, [0, SCREEN_BORDER, SCREEN_WIDTH, SCREEN_HEIGTH])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # User communication
    messages, new_input = create_message("nein", level)
    # messages = ["Das ist die erste Zeile.", "Die zweite Zeile soll erst erscheinen, wenn die 1. fertig ist."]

    messages_lens = [len(m) for m in messages]
    len_all_messages = sum(messages_lens)
    text_counter_max = len_all_messages * text_speed

    # snips enthält einen Eintrag für jedes Elemten der Liste messges
    # snips = [font.render(message[0 : (text_counter // text_speed) + 1], True, "white") for message in messages]
    snips = []
    characters_to_plot = text_counter // text_speed + 1
    for message in messages:
        if characters_to_plot > len(message):
            text = message
            characters_to_plot -= len(message)
        elif characters_to_plot > 0:
            text = message[:characters_to_plot]
            characters_to_plot = 0
        else:
            text = ""
        snips.append(font.render(text, True, "white"))

    print(snips)
    # text_counter muss weiterlaufen, bis der gesamte Text ausgegeben wurde
    if text_counter < (len_all_messages * text_speed):
        text_counter += 1

    # text_counter_max = (text_speed * (len(messages[0])) + (text_speed * len(messages[1])))
    len_multiplicate_speed = text_speed * len(messages[0])
    if (text_counter >= len_multiplicate_speed) and (text_counter < text_counter_max):
        if text_counter - len_multiplicate_speed < (text_speed * len(messages[1])):
            text_counter += 1

    line_spacing = 0
    # while text_counter <= text_counter_max:

    for snip in snips:  # TODO Die Zeilen sollen nacheinander erscheinen
        screen.blit(snip, (20, (SCREEN_BORDER + line_spacing)))
        line_spacing += 25

    print(f"a: {messages_lens}, b: {len_all_messages}, c: {text_counter_max}")
    draw_screen()
    clock.tick(TICK)

pygame.quit()
