import booste, time

prompts = ["A hotdog", "Not a hotdog"] # list of prompts, as strings
images = [
     "https://upload.wikimedia.org/wikipedia/commons/f/fb/Hotdog_-_Evan_Swigart.jpg",
     "https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball.png"
     ] # list of images, as URLs, as strings

api_key = "f1f22e45-8ae6-4658-911c-cb015014cc03"

while True:
     print("looping", time.time())
     out_dict = booste.clip(api_key, prompts, images, pretty_print=True) # nested json blob of similarities
     # Parse each similarity and pretty print
     # print("\n\n\n")
     # for prompt in prompts:
     #      for image in images:
     #           print("\n\t\tPrompt:\t\t", prompt, "\n\t\tImage URL:\t", image, "\n\t\tSimilarity:\t", out_dict[prompt][image]["similarity"], "")
     # print("\n\n\n")

     time.sleep(60)