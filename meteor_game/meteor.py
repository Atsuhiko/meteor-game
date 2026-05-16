"""
meteor.py

隕石避けゲームで使う Meteor クラスを定義するモジュールです。
このファイルは、run_game.py から import される部品として使えます。
また、python meteor.py と直接実行すると、隕石だけが落ちるデモが起動します。
"""

print(f"[meteor.py] 読み込まれました。__name__ = {__name__}")

import random
import pygame


class Meteor:
    """上から落ちてくる隕石を表すクラス。"""

    def __init__(self, screen_width: int) -> None:
        self.screen_width = screen_width
        self.radius = random.randint(12, 24)
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = -self.radius
        self.speed = random.randint(3, 8)
        self.color = (220, 110, 60)

    @property
    def rect(self) -> pygame.Rect:
        """当たり判定に使う長方形を返す。"""
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def update(self) -> None:
        """隕石を下方向に動かす。"""
        self.y += self.speed

    def is_out_of_screen(self, screen_height: int) -> bool:
        """画面下に消えたかどうかを返す。"""
        return self.y - self.radius > screen_height

    def draw(self, screen: pygame.Surface) -> None:
        """隕石を画面に描画する。"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def _run_meteor_demo() -> None:
    """meteor.py を直接実行したときだけ動く、隕石単体デモ。"""
    print("[meteor.py] 直接実行されたので、隕石単体デモを起動します。")
    print("[meteor.py] 隕石が上から落ちてきます。終了するにはウィンドウを閉じてください。")

    pygame.init()
    screen_width, screen_height = 640, 360
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Meteor module demo")
    clock = pygame.time.Clock()

    meteors: list[Meteor] = []
    spawn_timer = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        spawn_timer += 1
        if spawn_timer >= 20:
            meteors.append(Meteor(screen_width))
            spawn_timer = 0

        for meteor in meteors[:]:
            meteor.update()
            if meteor.is_out_of_screen(screen_height):
                meteors.remove(meteor)

        screen.fill((25, 25, 35))
        for meteor in meteors:
            meteor.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    print(f"[meteor.py] if __name__ == '__main__' の中に入りました。__name__ = {__name__}")
    print("[meteor.py] このモジュールは、隕石の生成・移動・描画を担当します。")
    _run_meteor_demo()
