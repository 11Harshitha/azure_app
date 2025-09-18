from services.blob_storage import *
from utils.data_processing import * 
from services.llm_connectivity import *

print("before function call")
# call blob connection function from tools.py
# response = blob_storage_connectivity("genaidemo", "genaidemo.docx")

blob_content = blob_storage_excel("genaidemo", "GenerativeAI_100_Questions.xlsx")
df = read_excel(blob_content)

for i,j in df.iterrows():
    print(i+1)
    print(j['Question'])
    print(azure_openai(j['Question']))

# print(df)
print("after function call")