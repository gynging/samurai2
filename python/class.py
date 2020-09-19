class Car:
    def __init__(self):
        self.name  = None
        self.morimoto = None
    def show(self):
        print(self.name)
    def kusano(self):
        print(self.morimoto)
# Carクラスのインスタンスを作成します。
car = Car()
# Carの変数nameにセダンという文字列を格納します。
car.name = "セダン"
# Carのメソッドであるshow()を実行します。
car.show()
# ターミナルには セダン と表示されます。