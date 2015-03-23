# Settings for {{ project_project }} project
#
# Local modifications will be overwritten.
#
import logging
from .{{ project_mode }} import *

MODE = "{{ project_mode }}"
DATABASES["default"]["HOST"] = "{{ project_dbhost }}"
DATABASES["default"]["NAME"] = "{{ project_dbname }}"
DATABASES["default"]["USER"] = "{{ project_dbuser }}"
DATABASES["default"]["PASSWORD"] = "{{ project_dbpassword }}"

CACHES["default"]["BACKEND"] = "redis_cache.cache.RedisCache"
CACHES["default"]["LOCATION"] = "{{ project_redishost }}:6379:1"
CACHES["default"]["KEY_PREFIX"] = '_'.join(("{{ project_project }}", MODE))

BROKER_URL = "amqp://{{ project_rabbitmquser }}:{{ project_rabbitmqpassword }}@{{ project_rabbitmqhost }}:5672/{{ project_rabbitmqvhost }}"

logging.info("Configured settings loaded.")
