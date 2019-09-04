import os

site_env = os.getenv('SITE_TYPE', 'local')

if site_env == 'staging':
    from .staging import *
else:
    from .production import *
