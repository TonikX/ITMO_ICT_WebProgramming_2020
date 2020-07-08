from django.db import models

# Create your models here.

class Hotel(models.Model):
    name=models.TextField(max_length=20)
    address=models.TextField(max_length=40)
    desc=models.TextField(max_length=20)
    places=models.IntegerField(max_length=4)
    types=models.TextField()
    facilities=models.TextField()
    owner=models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Hotel,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
