from aitextgen import aitextgen

ai = aitextgen(model_folder="models/shakes_model",
                tokenizer_file="models/shakes.tokenizer.json")

ai.generate(n=3, max_length=200)
