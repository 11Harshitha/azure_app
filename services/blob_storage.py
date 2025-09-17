import os
from azure.storage.blob import BlobServiceClient

def blob_storage_connectivity(container_name, blob_name):
    
    # Replace with your actual values or environment variables
    STORAGE_ACCOUNT_NAME = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    STORAGE_ACCOUNT_KEY = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY")
    CONNECTION_STRING = os.environ.get("AZURE_STORAGE_CONNECTION_STRING") # Alternatively, use connection string

    CONTAINER_NAME = container_name #"genaidemo"
    BLOB_NAME = blob_name #"genaidemo.docx"
    LOCAL_FILE_PATH = "genaidemo.docx"

    # Create a BlobServiceClient
    if CONNECTION_STRING:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

    with open(LOCAL_FILE_PATH, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    return f"Blob '{BLOB_NAME}' downloaded to '{LOCAL_FILE_PATH}'"

