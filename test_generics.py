import booste

string = 'What f.inc means to me.\nErik Dunteman.\nFebruary 2021.\n10 min read\n' # something like this; play around!
api_key = "f1f22e45-8ae6-4658-911c-cb015014cc03"
model_key = "d9ded1e6-357d-4bf5-8958-02e5b5131f30"

print("Prompt")
print(string)
print()

model_parameters = {
    "string": string,
    "length": 50
}

print("Generated")
print(booste.run(api_key, model_key, model_parameters))

