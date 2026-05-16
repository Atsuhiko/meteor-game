# import と if name == "main" 教材：隕石避けゲーム
この教材は、Python の `.py` ファイルが「モジュール」として import できること、そして直接実行されたときだけ `if __name__ == "__main__":` の中が実行されることを確認するための教材です。
セットアップ
```bash
pip install -r requirements.txt
cd meteor_game
```
1. import されたときの `__name__` を確認
```bash
python demo_imports.py
```
`player.py`, `meteor.py`, `game_core.py` が import されますが、ゲームや単体デモは起動しません。
2. player.py を直接実行
```bash
python player.py
```
`player.py` の `__name__` が `__main__` になり、プレイヤー単体デモが起動します。
3. meteor.py を直接実行
```bash
python meteor.py
```
`meteor.py` の `__name__` が `__main__` になり、隕石単体デモが起動します。
4. game_core.py を直接実行
```bash
python game_core.py
```
`game_core.py` の `__name__` は `__main__` になりますが、ゲームは起動しません。  
このファイルは `MeteorGame` クラスを定義する中核モジュールだからです。
5. ゲーム本体を起動
```bash
python run_game.py
```
`run_game.py` が実行ファイルとして動き、`game_core.py` から `MeteorGame` クラスを import してゲームを起動します。
ファイルの役割
ファイル	役割
`player.py`	プレイヤー部品。単独実行するとプレイヤーデモが起動します。
`meteor.py`	隕石部品。単独実行すると隕石デモが起動します。
`game_core.py`	ゲーム全体を管理する `MeteorGame` クラスを定義します。直接実行してもゲームは起動しません。
`run_game.py`	ゲームを起動する正式な入口です。
`demo_imports.py`	import 時の `__name__` の変化を確認するためのデモです。
