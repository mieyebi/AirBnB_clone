#!/usr/bin/python3
"""runs the initialization code for package"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
