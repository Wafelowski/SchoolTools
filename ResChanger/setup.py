from distutils.core import setup # Need this to handle modules
import py2exe 
import os
import time
from PIL import Image

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "reschanger.py"}],
    zipfile = None,
)