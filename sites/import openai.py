import os
import openai
from PIL import Image
import requests

def generate_cat_image(prompt, size="256x256", n=1):
    # Set API key from environment variable
    openai.api_key = "sk-proj-s1No2TLxSsEe551UWafLT3BlbkFJnXcsmsvf1pGbUSC32U1k"

    # Create image generation request
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size=size
    )

    # Extract image URL from response
    image_url = response["data"][0]["url"]

    # Download image from URL
    response = requests.get(image_url)
    image_data = response.content

    # Save image to file
    with open("popeyes.png", "wb") as f:
        f.write(image_data)

    # Open image using PIL
    image = Image.open("popeyes.png")

    # Display image
    image.show()

# Example usage
generate_cat_image("page de couverture les miserables de victor hugo")
