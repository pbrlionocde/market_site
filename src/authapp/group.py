from django.contrib.auth.models import Group


def get_group_admin():
    group, _ = Group.objects.get_or_create(name='Admin')
    return group
