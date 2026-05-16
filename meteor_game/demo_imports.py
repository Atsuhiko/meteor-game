"""
demo_imports.py

import されたモジュールの __name__ がどう変わるかを確認するためのデモファイルです。
このファイルを実行しても、ゲーム本体や単体デモは起動しません。
"""

print(f"[demo_imports.py] 読み込まれました。__name__ = {__name__}")

print("[demo_imports.py] これから player, meteor, game_core を import します。")
print("[demo_imports.py] import された側では __name__ が '__main__' ではなく、モジュール名になります。")

import player
import meteor
import game_core


if __name__ == "__main__":
    print(f"[demo_imports.py] if __name__ == '__main__' の中に入りました。__name__ = {__name__}")
    print("[demo_imports.py] import の確認が終わりました。")
    print("[demo_imports.py] player.py, meteor.py, game_core.py の単体実行用コードは実行されていません。")
