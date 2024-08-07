# from openai import OpenAI

# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#     api_key="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",
# )

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alaxa and Google Cloude .",
#         },
#         {
#             "role": "user",
#             "content": "what is coding",
#         },
#     ],
# )

# print(completion.choices[0].message.content)
