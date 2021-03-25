from django.db import models

class Pergunta(models.Model):
    enunciado = models.TextField()
    disponível = models.BooleanField(default=False)
    alternativas = models.JSONField()
    alternativa_correta = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])
