import booste

prompts = ["A hotdog", "A basketball"] # list of prompts, as strings
images = [
     "https://upload.wikimedia.org/wikipedia/commons/f/fb/Hotdog_-_Evan_Swigart.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball.png"
     ] # list of images, as URLs, as strings

api_key = "f1f22e45-8ae6-4658-911c-cb015014cc03"

out = booste.clip(api_key, prompts, images) # nested json blob of similarities

# Parse each similarity and pretty print
print("\n\n\n")
for prompt in prompts:
     for image in images:
          print("\n\t\tPrompt:\t\t", prompt, "\n\t\tImage URL:\t", image, "\n\t\tSimilarity:\t", out[prompt][image]["similarity"], "")
print("\n\n\n")