from datetime import date

from users.models import CustomUser


def birthday(request):
    return {
        'birthday': CustomUser.objects.filter(birthday=date.today()),
        }
