import os
site_env = os.getenv('SITE_TYPE', "staging")

if site_env == 'production':
    from .production import *  # NOQA
elif site_env == 'staging':
    from .staging import *  # NOQA




