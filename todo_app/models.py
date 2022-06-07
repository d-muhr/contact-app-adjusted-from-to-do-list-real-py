# todo_list/todo_app/models.py
from django.utils import timezone

from django.db import models
from django.urls import reverse

from datetime import date

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


# todo: The fields "phone" and "email" currently have to be # filled on the 2 webpages("contact/id/info/id" and 
# "contact/id/inf/add") although it should be possible to 
#  leave them empty. 

# ToDo: Creating birthday as models.DateField(...) is more
# comple than expected which is why I will do this another 
# time_7.6.22. The way it is currently tried results in 
# the follwing error "ValueError: invalid literal for int() with base 10: b'a'"

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    birthday = models.DateField(default = date.today())
    address = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    notes = models.TextField(null = True, blank = True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
