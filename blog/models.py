from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


class Post(models.Model):

    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})
