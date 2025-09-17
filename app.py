from services.blob_storage import *

print("before function call")
# call blob connection function from tools.py
response = blob_storage_connectivity("genaidemo", "genaidemo.docx")

print("after function call")