"""Generate SECRET_KEY for re-create.
    - When lost SECRET_KEY.
    - When leak SECRET_KEY by commit and push SECRET_KEY info to git repository.
"""
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
print(f'SECRET_KEY = {secret_key}')
