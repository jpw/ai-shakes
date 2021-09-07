from aitextgen import aitextgen

# If you want to download an alternative GPT-2 model from Hugging Face's repository of models, 
# pass that model name to model, eg
# ai = aitextgen(model="minimaxir/hacker-news")

# This can also be used to download the pretrained GPT Neo models from EleutherAI.
# ai = aitextgen(model="EleutherAI/gpt-neo-125M")

# Without any parameters, aitextgen() will download, cache, and load the 
# 124M GPT-2 "small" model via Huggingface
ai = aitextgen()

ai.generate()
ai.generate(n=3, max_length=100)
ai.generate(n=3, prompt="I believe in unicorns because", max_length=100)
ai.generate_to_file(n=10, prompt="I believe in unicorns because", max_length=100, temperature=1.2)
