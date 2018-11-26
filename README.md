# Кубики

Образовательный проект для обучение детей программированию.

Данный проект распространяется вместе с уроками.
Чтобы программирование было интереснее результат работы программы
можно визуализировать в пространстве состоящеми из отдельных кубиков в стиле Minecraft.

За основу графического движка взять проект:
https://github.com/fogleman/Craft

## Как запустить

```shell
pip install pyglet
git clone https://github.com/fogleman/Minecraft.git
cd Minecraft
python main.py
```

```
sudo apt-get install freeglut3-dev
```

## Как играть

### Moving

- W: forward
- S: back
- A: strafe left
- D: strafe right
- Mouse: look around
- Space: jump
- Tab: toggle flying mode

### Building

- Selecting type of block to create:
    - 1: brick
    - 2: grass
    - 3: sand
- Mouse left-click: remove block
- Mouse right-click: create block

### Quitting

- ESC: release mouse, then close window
