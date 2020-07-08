from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Tour(models.Model):
    tour_name= models.CharField(max_length=50)
    agency = models.CharField(max_length=50)
    tour_descrption = models.TextField()
    duration = models.CharField(max_length=100)
    payment = models.TextField()
    

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"

    def __str__(self):
        return self.tour_name


class Comment(models.Model):
    CType = (
        ('вопрос содержания тура', 'вопрос содержания тура'),
        ('вопрос об условиях оплаты', 'вопрос об условиях оплаты'),
        ('отзыв', 'отзыв')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_type = models.CharField(choices=CType, max_length=100)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
