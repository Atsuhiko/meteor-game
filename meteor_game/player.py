"""
player.py

隕石避けゲームで使う Player クラスを定義するモジュールです。
このファイルは、run_game.py から import される部品として使えます。
また、python player.py と直接実行すると、プレイヤーだけを動かすデモが起動します。
"""

print(f"[player.py] 読み込まれました。__name__ = {__name__}")

import pygame


class Player:
    """画面下部を左右に動くプレイヤーを表すクラス。"""

    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.width = 50
        self.height = 30
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height - self.height - 20
        self.speed = 6
        self.color = (80, 170, 255)
        self.screen_width = screen_width

    @property
    def rect(self) -> pygame.Rect:
        """当たり判定に使う長方形を返す。"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys: pygame.key.ScancodeWrapper) -> None:
        """左右キーの入力に応じてプレイヤーを動かす。"""
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # 画面の外へ出ないようにする
        self.x = max(0, min(self.x, self.screen_width - self.width))

    def draw(self, screen: pygame.Surface) -> None:
        """プレイヤーを画面に描画する。"""
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)


def _run_player_demo() -> None:
    """player.py を直接実行したときだけ動く、プレイヤー単体デモ。"""
    print("[player.py] 直接実行されたので、プレイヤー単体デモを起動します。")
    print("[player.py] 左右キーで青いプレイヤーを動かせます。終了するにはウィンドウを閉じてください。")

    pygame.init()
    screen_width, screen_height = 640, 360
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Player module demo")
    clock = pygame.time.Clock()
    player = Player(screen_width, screen_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((25, 25, 35))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    print(f"[player.py] if __name__ == '__main__' の中に入りました。__name__ = {__name__}")
    print("[player.py] このモジュールは、プレイヤーの位置・移動・描画を担当します。")
    _run_player_demo()
