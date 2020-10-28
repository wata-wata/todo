from django.db import models

# Create your models here.

# 選択肢の定義('画面に保存される文字列(bootstrapで使う)', '呼び出される名前')
PRIORITY = (('danger','high'),('info','normal'),('success','low'))

# データベースを定義する(models.Modelを継承する)
class TodoModel(models.Model):
    # CharField: 文字列を入れるフィールド
    title = models.CharField(max_length=100)
    # TextField: 長い文字列を入れるフィールド
    memo = models.TextField()
    # 優先度
    priority = models.CharField(
        max_length = 50,
        # 選択肢を表示する
        choices = PRIORITY
    )
    # 日付
    duedate = models.DateField()
    # オブジェクトを文字列に変えて表示する
    def __str__(self):
        # オブジェクトのタイトルを表示する
        return self.title