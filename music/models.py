from django.db import models

from user.models import User


class MusicByValue(models.Model):
    VALUES = (
        ('Жанр', 'Жанр'),
        ('Группа', 'Группа'),
        ('Автор', 'Автор'),
        ('Альбом', 'Альбом'),
        ('Настроение', 'Настроение'),
        ('Год выпуска', 'Год выпуска'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music_by_genre')
    value = models.CharField(max_length=200, null=True, blank=True)
    _type = models.CharField(max_length=200, choices=VALUES)

    class Meta:
        db_table = 'music_by_value'
        verbose_name = 'Музыкальные предпочтения'
        verbose_name_plural = 'Музыкальные предпочтения'

    def __str__(self):
        return f'Музыкальные предпочтения ({self._type}) для пользователя {self.user.username}'


# class UserLikedMusic(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_musics')
#     music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='liked_users')
#
#     class Meta:
#         db_table = 'user_liked_music'
#         verbose_name = 'Понравившаяся музыка'
#         verbose_name_plural = 'Понравившаяся музыка'
#
#     def __str__(self):
#         return f'Понравившаяся музыка для пользователя {self.user.username}'
