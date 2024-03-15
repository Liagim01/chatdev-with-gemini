# from openai import OpenAI

# client = OpenAI(
#     api_key='sk-9VNaFiikGgrOSA3i879a8b1b48534785AdEf6a5776EcE9D4',
#     base_url="https://sailaoda.cn/v1",
#     # base_url="https://sailaoda.cn/v1/",
# )

# response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "hello"}]
# )

# print(response.choices[0].message.content)

import vertexai
from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)

vertexai.init()
model = GenerativeModel(model_name='gemini-1.0-pro')
response =model.generate_content(contents='Hi')
print(response.candidates)
