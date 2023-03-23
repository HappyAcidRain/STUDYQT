import openai

openai.api_key = "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"

models = openai.Model.list()

# print the first model's id
print(models)
