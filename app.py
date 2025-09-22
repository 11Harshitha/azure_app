from services.blob_storage import *
from utils.data_processing import * 
from services.llm_connectivity import *
from services.logger import logger
# print("before function call")
# # call blob connection function from tools.py
# # response = blob_storage_connectivity("genaidemo", "genaidemo.docx")

blob_content = blob_storage_excel("genaidemo", "GenerativeAI_100_Questions.xlsx")
df = read_excel(blob_content)
logger.debug(df)
# for i,j in df.iterrows():
#     print(i+1)
#     print(j['Question'])
#     print(azure_openai(j['Question']))

# print(df)
print("after function call")

# from services.logger import logger  # import the shared logger

# def my_function():
#     logger.info("Inside my_function")
#     logger.error("Error in function")
#     logger.debug("Completed function")
# my_function()