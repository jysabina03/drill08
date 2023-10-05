from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(5, 10)
        self.type = random.randint(0, 1)
        if (self.type):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        if self.type == 1:
            if self.y > 60:
                self.y -= self.speed

            if self.y < 60:
                self.y = 60
            else:
                pass
        else:
            if self.y > 70:
                self.y -= self.speed
            if self.y < 70:
                self.y = 70
            else:
                pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []

    grass = Grass()  # 클래스를 이용해 객체를 찍어냄
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    balls = [Ball() for i in range(20)]
    world += balls


def update_world():
    grass.update()
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # 객체들의 상호작용 결과 업데이트
    render_world()
    delay(0.05)

# finalization code

close_canvas()
