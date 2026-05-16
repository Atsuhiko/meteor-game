"""
run_game.py

隕石避けゲームを起動するための実行専用ファイルです。
このファイルは、game_core.py から MeteorGame クラスを import して、ゲームを開始します。
"""

print(f"[run_game.py] 読み込まれました。__name__ = {__name__}")

from game_core import MeteorGame


if __name__ == "__main__":
    print(f"[run_game.py] if __name__ == '__main__' の中に入りました。__name__ = {__name__}")
    print("[run_game.py] このファイルはゲームを起動するための入口です。")
    print("[run_game.py] game_core.py から MeteorGame クラスを import して、ゲームを開始します。")
    game = MeteorGame()
    game.run()
