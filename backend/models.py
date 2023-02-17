from django.db import models

# Create your models here.
class Documents(models.Model):
    CHOISE_SUBJECT = (
        (1, 'Архитектура предприятия'),
        (2, 'Интеллектуальный анализ данных'),
        (3, 'Информационная безопасность IT инфраструктуры'),
        (4, 'Гибкие технологии Agile'),
        (5, 'Информационные системы и информационно-коммуникационные технологии управления бизнесом'),
        (6, 'Проектирование бизнес-процессов'),
        (7, 'Проектная деятельность'),
    )
    CHOISE_STATE = (
        (1, 'stable'),
        (2, 'writing')
    )
    owner_id = models.CharField(max_length=50)
    subject_type = models.IntegerField(choices=CHOISE_SUBJECT)
    state = models.IntegerField(choices=CHOISE_STATE)