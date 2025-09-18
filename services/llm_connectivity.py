import os
from openai import AzureOpenAI

from dotenv import load_dotenv

load_dotenv()
# from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def azure_openai(query):
    endpoint = os.getenv("azure_openai_endpoint")
    model_name = "gpt-4o"
    deployment = "gpt-4o"

    subscription_key =os.getenv("azure_openai_key")
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who can answer user query based on your knowledge.",
            },
            {
                "role": "user",
                "content": f"{query}",
            }
        ],
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
        model=deployment
    )

    return response.choices[0].message.content
    


