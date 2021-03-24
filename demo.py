import booste

api_key = "f1f22e45-8ae6-4658-911c-cb015014cc03"
model_key = "d9ded1e6-357d-4bf5-8958-02e5b5131f30"

model_parameters = {
    "string": "Top 10 reasons you should never live demo a product.\nErik Dunteman\nFeb 10, 2021\n10 minute read",
    "length": 100
}

out = booste.run(api_key, model_key, model_parameters)

print(out)