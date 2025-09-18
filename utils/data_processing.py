from io import BytesIO
import pandas as pd

def read_excel(blob_data):
    # Read the bytes into a Pandas DataFrame
    df = pd.read_excel(BytesIO(blob_data))

    # Now you can work with your DataFrame
    # print(df.head())

    # with open(LOCAL_FILE_PATH, "wb") as download_file:
    #     download_file.write(blob_client.download_blob().readall())

    return df.head()