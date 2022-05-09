import requests


response = requests.get(
    "https://lh3.googleusercontent.com/XkPlKyP6bwIABj8KswI8Jm8bItj_L_dDa0ZThxiQ4HyBFgiOzWdxVi_PZKu4dl3HdcNg9hVFmO22iyDKSDjlKrDuag-2DyJlaDJ5Kw=w600"
)


file = open("sample_image.jpg", "wb")

file.write(response.content)

file.close()
