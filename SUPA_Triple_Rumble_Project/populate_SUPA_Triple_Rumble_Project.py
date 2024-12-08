import os
import django
import SUPA_Triple_Rumble_Tournament.models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SUPA_Triple_Rumble_Project.settings')

django.setup()


def populate():

    return None


if __name__ == '__main__':
    print('Starting rango population script...')
    populate()
