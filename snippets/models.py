from django.db import models

# Create your models here.
from django.conf import settings


class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('コード', blank=True)
    description = models.TextField('説明', blank=True)
    #created_by = models.ForeignKey('settings.AUTH_USER_MODEL',
    #                               verbose_name="投稿者",
    #                               on_delete=models.CASCADE) # ユーザが削除された際に、そのユーザへの参照をもつスニペットレコードも自動的に削除される。障害発生時にユーザが削除されると自動でスニペットモデルも削除されるのは痛いなぁ。不整合が発生しなくなるけど。。。
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now_add=True)

    def __str__(self):
        return self.title