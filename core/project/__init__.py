import os
from pathlib import Path

# decouple
from decouple import Csv, config
from dotmap import Dotmap

# init enviroment
ENV = Dotmap({'config': config, 'csv': Csv})

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Admin path
ADMIN_PATH = ENV.config('ADMIN_PATH')