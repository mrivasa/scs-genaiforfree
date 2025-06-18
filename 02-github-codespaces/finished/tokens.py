import tiktoken

text = """
Generative AI is rapidly changing how we approach work, creativity, and problem-solving across industries. By enabling machines to produce human-like text, images, and code, it reduces the time required for content creation and streamlines complex tasks. From personalized tutoring in education to accelerated software development, its applications are expanding daily. However, this power also brings challenges, including ethical concerns, misinformation risks, and job displacement, requiring thoughtful adoption and responsible integration into real-world workflows and decision-making.
"""

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode(text)
print(tokens)

decoded_text = enc.decode(tokens)
print(decoded_text)

if decoded_text == text:
    print("Decoded text is the same as the original text")
else:
    print("Something went wrong")

no_words = len(text.split(" "))
print(f"The text has {no_words} words")
print(f"This was converted into {len(tokens)} tokens")
print(f"Ratio of words to tokens: {no_words / len(tokens)}")
