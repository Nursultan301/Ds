from django.db import models


class IssykKul(models.Model):
    title = models.CharField("Называние", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField("Фото")

    class Meta:
        verbose_name = "Иссык-куль"
        verbose_name_plural = "Иссык-куль"

    def __str__(self):
        return self.title


class Naryn(models.Model):
    title = models.CharField("Называние", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField("Фото")

    class Meta:
        verbose_name = "Нарын"
        verbose_name_plural = "Нарын"

    def __str__(self):
        return self.title


class Chui(models.Model):
    title = models.CharField("Называние", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField("Фото")

    class Meta:
        verbose_name = "Чуй"
        verbose_name_plural = "Чуй"

    def __str__(self):
        return self.title


class Talas(models.Model):
    title = models.CharField("Называние", max_length=50)
    description = models.TextField("Описание")
    img = models.ImageField("Фото")

    class Meta:
        verbose_name = "Талас"
        verbose_name_plural = "Талас"

    def __str__(self):
        return self.title


class Gallery(models.Model):
    """ Галерея """
    img = models.ImageField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерии"


class Feedback(models.Model):
    """ Обратная связь """
    name = models.CharField("Имя", max_length=50)
    subject = models.CharField("Тема", max_length=100)
    messages = models.TextField("Сообщения")

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.name
