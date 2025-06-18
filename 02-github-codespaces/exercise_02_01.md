* Press *Ctrl-`* to open the terminal panel.
* Install the `tiktoken` package
    ```bash
    pip install tiktoken
    ```
* Open the file `02-github-codespaces/tokens.py`
* Import the `tiktoken` module
    ```python
    import tiktoken
    ```
*  You'll need some text to convert to tokens.  Create a variable named `text`
    ```python
    text = """
    
    """
    ```
* Open the file `02-github-codespaces/about_gen_ai.txt`.  Copy the contents and paste it between the pair of triple quotes.
* An encoding will determine how to convert the text to tokens. The `tiktoken` package implements several encoding algorithms including  `cl100k_base` which is used by many of the modern OpenAI models such as GPT-4.
    ```python
    enc = tiktoken.get_encoding("cl100k_base")
    ```
* Use the encoding to encode the text and return a list of tokens.
    ```python
    tokens = enc.encode(text)
    ```
* Print the tokens
    ```python
    print(tokens)
    ```
*  Click the *Run* button in the upper right corner of the editor.
*  Notice that the tokens are a list of numbers.
*  You can also convert the tokens back into words.
    ```python
    decoded_text = enc.decode(tokens)
    print(decoded_text)
    ```
*  Compare the `decoded_text` to the original `text`.
    ```python
    if decoded_text == text:
        print("Decoded text is the same as the original text")
    else:
        print("Something went wrong")
    ```
* Run the file again.
* Compute the ratio of words to tokens
    ```python
    no_words = len(text.split(" "))
    print(f"The text has {no_words} words")
    print(f"This was converted into {len(tokens)} tokens")
    print(f"Ratio of words to tokens: {no_words / len(tokens)}")
    ```
* Run the file again.
* Go to [Exercise 02-02](https://github.com)