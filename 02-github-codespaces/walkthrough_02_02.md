* Open the terminal panel (*Ctrl-`*)
* Install the `ipykernel` package
    ```bash
    pip install ipykernel
    ```
* Open the Command Pallette (*Ctrl/Cmd-Shift-P*)
* Search for `jupyter`
* Click on **Create: New Jupyter Notebook**
* Press *Ctrl/Cmd-S* to save the notebook in the `02-github-codespaces` folder as `tokens.ipynb`
* Click the **Select Kernel** button in the upper right corner of the notebook.
* Select **Python Environments**
* Select the Python environment labeled with `Global Env` or `Recommended` on the right.
* In the cell, import the `tiktoken` module.
    ```python
    import tiktoken
    ```
* Press *Shift-Enter* to execute the cell and move to the next cell.  Since there is no next cell, a new one will be created.
* In the new cell, create the `text` variable like in the previous exercise using the contents of `02-github-codespaces/about_gen_ai.txt`.  Execute the cell with *Shift-Enter*.
    ```python
    text = """
    [contents here]
    """
    ```
* In the next cell, create the encoding, convert the `text` to `tokens` and `print` the `tokens`.  Execute the cell.
    ```python
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    print(tokens)
    ```
* In the next cell, compute the ratio of words in the `text` to `tokens` and execute the cell.
    ```python
    no_words = len(text.split(" "))
    print(f"The text has {no_words} words")
    print(f"This was converted into {len(tokens)} tokens")
    print(f"Ratio of words to tokens: {no_words / len(tokens)}")
    ```
* Go back to the cell where you created the encoding and change the encoding to `p50k_base`.  Execute that cell again.
* And execute the cell computing the ratio again.