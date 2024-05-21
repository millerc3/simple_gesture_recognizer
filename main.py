import argparse
import pygame
import time

import recognizer
from recognizer import Point, Template

def main():





    # parser = argparse.ArgumentParser(description="Recognizer prototype")
    # parser.add_argument('--template', type=str, action='store')
    # parser.add_argument('--point', type=str, action='store')
    # args = parser.parse_args()


    # if args.point:
    #     print(Point.from_str(args.point))

    # target_template = None

    # if args.template:
    #     target_template = args.template

    templates = list()
    templates.append(Template.generate_template("Circle", recognizer.CIRCLE))
    templates.append(Template.generate_template("Square", recognizer.SQUARE))
    templates.append(Template.generate_template("Triangle", recognizer.TRIANGLE))
    templates.append(Template.generate_template("Down V", recognizer.DOWN_V))
    templates.append(Template.generate_template("Carrot", recognizer.CARROT))
    templates.append(Template.generate_template("Fish", recognizer.FISH))
    
    pygame.init()

    fps = 90

    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    
    running = True
    drawing = False
    record = list()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

                chosen_template, score = recognizer.recognize(record, templates)
                print(chosen_template.name)
                print(f"   score: {score}")

                record = recognizer.resample(record)
                for point in record:
                    pygame.draw.circle(screen, (255, 0, 0), (point.x+250, point.y+250), 2)
                pygame.draw.circle(screen, (0, 255, 0), (record[0].x+250, record[0].y+250), 4)

                pygame.display.update()
                pygame.time.wait(1500)

                # clear screen
                screen.fill((0, 0, 0))

                # # print record
                # print(record)
                # clear record
                record = list()
        
        if drawing:
            x, y = pygame.mouse.get_pos()
            record.append(Point(x, y))
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 2)
        
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()