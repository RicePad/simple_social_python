from django.db import models
from django.coure.urlresolvers import reverse
from django.utils.text import slugify
# Create your GROUP models here.
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through="GroupMember")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
    ordering = ["name"]


    def __str__(self):
        return self.name

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships")
    user = models.ForeignKey(User, related_name="user_groups")
