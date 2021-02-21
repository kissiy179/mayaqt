# mayaqt
MayaでPysideを使いやすくするパッケージ  
Qt、qtpyモジュールの読み込みやMaya独自オブジェクトの定義を行う

| 変数名 | 概要 |
| ---- | ---- |
| maya_win | Mayaメインウィンドウポインタ. parentに設定することでMayaウィンドウの子として動作する |
| maya_base_mixin | 基本Mixin. これを継承することで簡単にMayaツールウィンドウとしての動作をさせることができる |
| maya_dockable_mixin | ドッカブル用Mixin. これを継承することで簡単にMaya内でドックに結合できるウィンドウとして動作させることができる |
