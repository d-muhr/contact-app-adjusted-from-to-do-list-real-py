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

# ToDo: When I create the same contact name or contact info # within 1 contact with the same name an error occurs. 
# Instead the user should be informed that ne name exists
# already_7.6.22



class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    birthday = models.DateField(default = date.today())
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null = True, blank = True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]
