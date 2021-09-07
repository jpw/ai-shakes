from aitextgen import aitextgen

ai = aitextgen(model_folder="models/shakes_model",
                tokenizer_file="models/shakes.tokenizer.json")

ai.generate(n=1, max_length=200, temperature=1.7)
ai.generate_to_file(n=10, max_length=200, temperature=1.7)