from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = True
window.exit_button.visible = True

blocks = [
    load_texture('/grass.png'),
    load_texture('/grass.png'),
    ]

block_id = 1

def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]

sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('/sky.jpg'),
    scale=500,
    double_sided=True
)

hand = Entity(
    model='blade',
    texture='/block.obj',
    rotation=(30, -40),
    position=(0.5, -0,6),
    parent=camera.ui,
    scale=(0.2, 0.15)
)

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()

app.run()
