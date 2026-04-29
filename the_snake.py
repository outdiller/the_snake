from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс, от котоого наследуются все объекты.
    Содержит общие атрибуты: позиция и цвет.
    """

    def __init__(self, position=None, body_color=None):

        if position is None:
            self.position = (320, 240)
        else:
            self.position = position
    
    def draw(self, surface):
        """
        Абстрактный метод для отрисовки объекта на экране.
        Аргумент: surface (поверхность, на которой рисуем)
        """
        pass

class Apple(GameObject):
    apple_color = (255, 0, 0)

    super()__init__(position=None , body_color=apple_color)

        self.randomize_position()

    def randomize_position()
    
        max_x = 640 - 20
        max_y = 480 - 20
    
        x.random.randrage(o, max_x + 1, 20)
        y.random.randrage(o, max_y + 1, 20)
        self.position = (x,y)
    def draw(self, surface):
        rect = pygame.Rect(
            self.position[0],
            self.position[1],
            20,
            20
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку."""

    def __init__(self):
        """Инициализация начального состояния змейки."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позицию змейки."""
        # Получаем текущую позицию головы
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction

        # Вычисляем новую позицию головы с учетом оборачивания
        new_head = (
            (head_x + dx) % SCREEN_WIDTH,
            (head_y + dy) % SCREEN_HEIGHT
        )

        # Проверяем столкновение с собой
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            self.reset()
        else:
            # Добавляем новую голову в начало списка
            self.positions.insert(0, new_head)

            # Если длина змейки превышает установленную, удаляем хвост
            if len(self.positions) > self.length:
                self.last = self.positions.pop()
            else:
                self.last = None

    def draw(self, surface):
        """Отрисовывает змейку на экране."""
        # Отрисовка тела змейки (кроме головы)
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        if self.positions:
            head_rect = pygame.Rect(
                self.positions[0],
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, self.body_color, head_rect)
            pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = choice([RIGHT, LEFT, UP, DOWN])
        self.next_direction = None
        self.last = None
        # Очищаем экран
        screen.fill(BOARD_BACKGROUND_COLOR)


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    ...

    # while True:
    #     clock.tick(SPEED)

        # Тут опишите основную логику игры.
        # ...


if __name__ == '__main__':
    main()


