from datetime import date

from users.models import CustomUser


def birthday(request):
    """
    :return: user with birthday today
    """
    return {
        'birthday': CustomUser.objects.filter(birthday=date.today()),
        }
