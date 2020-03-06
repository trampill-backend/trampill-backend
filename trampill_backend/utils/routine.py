from django.contrib.auth import get_user_model

User = get_user_model()


def is_member(user: User, member: str):
    return user.groups.filter(name=member).exists()
