"""
game_core.py

隕石避けゲーム全体を管理する MeteorGame クラスを定義するモジュールです。
このファイルは、主に run_game.py から import されて使われます。

重要:
- game_core.py はゲーム本体の「部品」を定義するモジュールです。
- このファイルを import しても、ゲームは自動では始まりません。
- このファイルを python game_core.py と直接実行しても、ゲームは起動しません。
- ゲームを起動する正式な入口は run_game.py です。
"""

print(f"[game_core.py] 読み込まれました。__name__ = {__name__}")

import random
import pygame

from player import Player
from meteor import Meteor


class MeteorGame:
    """隕石避けゲーム全体を管理するクラス。"""

    def __init__(self, screen_width: int = 640, screen_height: int = 480) -> None:
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Meteor Dodge Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 24)

        self.player = Player(screen_width, screen_height)
        self.meteors: list[Meteor] = []
        self.spawn_timer = 0
        self.score = 0
        self.running = True
        self.game_over = False

    def handle_events(self) -> None:
        """ウィンドウを閉じるなどのイベントを処理する。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.game_over and event.key == pygame.K_SPACE:
                    self.reset()

    def update(self) -> None:
        """ゲーム内の状態を更新する。"""
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        self.player.move(keys)

        self.spawn_timer += 1
        if self.spawn_timer >= max(15, 35 - self.score // 5):
            self.meteors.append(Meteor(self.screen_width))
            self.spawn_timer = 0

        for meteor in self.meteors[:]:
            meteor.update()
            if meteor.is_out_of_screen(self.screen_height):
                self.meteors.remove(meteor)
                self.score += 1
            elif meteor.rect.colliderect(self.player.rect):
                self.game_over = True

    def draw(self) -> None:
        """画面全体を描画する。"""
        self.screen.fill((18, 18, 30))

        for meteor in self.meteors:
            meteor.draw(self.screen)
        self.player.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (240, 240, 240))
        self.screen.blit(score_text, (20, 20))

        help_text = self.small_font.render("Move: LEFT / RIGHT", True, (200, 200, 200))
        self.screen.blit(help_text, (20, 58))

        if self.game_over:
            message = self.font.render("GAME OVER", True, (255, 90, 90))
            retry = self.small_font.render("Press SPACE to restart", True, (240, 240, 240))
            self.screen.blit(message, message.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 20)))
            self.screen.blit(retry, retry.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20)))

        pygame.display.flip()

    def reset(self) -> None:
        """ゲームを最初からやり直す。"""
        self.player = Player(self.screen_width, self.screen_height)
        self.meteors = []
        self.spawn_timer = 0
        self.score = 0
        self.game_over = False

    def run(self) -> None:
        """ゲームループを実行する。run_game.py から呼び出される。"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()


class MeteoGame_2(MeteorGame):
    """
    2ステージ制の隕石避けゲーム。

    追加仕様:
    - Score が 10 になると次のステージに進む
    - ステージは 2 ステージだけ
    - ステージ2をクリアすると「Misson Complete」と大きく表示する
    - ステージ2はステージ1の 1.1 倍の落下スピードにする
    """

    CLEAR_SCORE = 10
    MAX_STAGE = 2
    STAGE2_SPEED_MULTIPLIER = 1.1

    def __init__(self, screen_width: int = 640, screen_height: int = 480) -> None:
        super().__init__(screen_width, screen_height)
        self.stage = 1
        self.mission_complete = False
        self.big_font = pygame.font.SysFont(None, 72)

    def handle_events(self) -> None:
        """ウィンドウを閉じる、またはクリア後・ゲームオーバー後のリスタートを処理する。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if (self.game_over or self.mission_complete) and event.key == pygame.K_SPACE:
                    self.reset()

    def update(self) -> None:
        """ゲーム内の状態を更新する。ステージ進行もここで管理する。"""
        if self.game_over or self.mission_complete:
            return

        keys = pygame.key.get_pressed()
        self.player.move(keys)

        self.spawn_timer += 1
        if self.spawn_timer >= max(15, 35 - self.score // 5):
            meteor = Meteor(self.screen_width)

            # ステージ2では、隕石の落下スピードをステージ1の1.1倍にする。
            if self.stage == 2:
                meteor.speed *= self.STAGE2_SPEED_MULTIPLIER

            self.meteors.append(meteor)
            self.spawn_timer = 0

        for meteor in self.meteors[:]:
            meteor.update()
            if meteor.is_out_of_screen(self.screen_height):
                self.meteors.remove(meteor)
                self.score += 1
                self.check_stage_clear()
            elif meteor.rect.colliderect(self.player.rect):
                self.game_over = True

    def check_stage_clear(self) -> None:
        """Score が CLEAR_SCORE に到達したら、次ステージまたはミッションクリアに進む。"""
        if self.score < self.CLEAR_SCORE:
            return

        if self.stage < self.MAX_STAGE:
            self.stage += 1
            self.score = 0
            self.meteors = []
            self.spawn_timer = 0
        else:
            self.mission_complete = True
            self.meteors = []

    def draw(self) -> None:
        """画面全体を描画する。"""
        self.screen.fill((18, 18, 30))

        for meteor in self.meteors:
            meteor.draw(self.screen)
        self.player.draw(self.screen)

        stage_text = self.font.render(f"Stage: {self.stage}", True, (240, 240, 240))
        self.screen.blit(stage_text, (20, 20))

        score_text = self.font.render(f"Score: {self.score}", True, (240, 240, 240))
        self.screen.blit(score_text, (20, 58))

        help_text = self.small_font.render("Move: LEFT / RIGHT", True, (200, 200, 200))
        self.screen.blit(help_text, (20, 96))

        if self.game_over:
            message = self.font.render("GAME OVER", True, (255, 90, 90))
            retry = self.small_font.render("Press SPACE to restart", True, (240, 240, 240))
            self.screen.blit(message, message.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 20)))
            self.screen.blit(retry, retry.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20)))

        if self.mission_complete:
            message = self.big_font.render("Misson Complete", True, (255, 230, 120))
            retry = self.small_font.render("Press SPACE to restart", True, (240, 240, 240))
            self.screen.blit(message, message.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 20)))
            self.screen.blit(retry, retry.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40)))

        pygame.display.flip()

    def reset(self) -> None:
        """ゲームを最初からやり直す。"""
        self.player = Player(self.screen_width, self.screen_height)
        self.meteors = []
        self.spawn_timer = 0
        self.score = 0
        self.stage = 1
        self.game_over = False
        self.mission_complete = False


if __name__ == "__main__":
    print(f"[game_core.py] if __name__ == '__main__' の中に入りました。__name__ = {__name__}")
    print("[game_core.py] このモジュールは、隕石避けゲーム全体を管理する MeteorGame クラスを定義します。")
    print("[game_core.py] ただし、このファイルを直接実行してもゲームは起動しません。")
    print("[game_core.py] ゲームを起動する正式な入口は run_game.py です。")
