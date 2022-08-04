#!/usr/bin/python3
"""runs initialization code for package"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
