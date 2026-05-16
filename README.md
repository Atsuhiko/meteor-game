import と if name == "main" 教材：隕石避けゲーム
この教材は、Python の `.py` ファイルが「モジュール」として import できること、そして直接実行されたときだけ `if \_\_name\_\_ == "\_\_main\_\_":` の中が実行されることを確認するための教材です。
セットアップ
```bash
pip install -r requirements.txt
cd meteor\_game
```
1. import されたときの `\_\_name\_\_` を確認
```bash
python demo\_imports.py
```
`player.py`, `meteor.py`, `game\_core.py` が import されますが、ゲームや単体デモは起動しません。
2. player.py を直接実行
```bash
python player.py
```
`player.py` の `\_\_name\_\_` が `\_\_main\_\_` になり、プレイヤー単体デモが起動します。
3. meteor.py を直接実行
```bash
python meteor.py
```
`meteor.py` の `\_\_name\_\_` が `\_\_main\_\_` になり、隕石単体デモが起動します。
4. game_core.py を直接実行
```bash
python game\_core.py
```
`game\_core.py` の `\_\_name\_\_` は `\_\_main\_\_` になりますが、ゲームは起動しません。  
このファイルは `MeteorGame` クラスを定義する中核モジュールだからです。
5. ゲーム本体を起動
```bash
python run\_game.py
```
`run\_game.py` が実行ファイルとして動き、`game\_core.py` から `MeteorGame` クラスを import してゲームを起動します。
ファイルの役割
ファイル	役割
`player.py`	プレイヤー部品。単独実行するとプレイヤーデモが起動します。
`meteor.py`	隕石部品。単独実行すると隕石デモが起動します。
`game\_core.py`	ゲーム全体を管理する `MeteorGame` クラスを定義します。直接実行してもゲームは起動しません。
`run\_game.py`	ゲームを起動する正式な入口です。
`demo\_imports.py`	import 時の `\_\_name\_\_` の変化を確認するためのデモです。
