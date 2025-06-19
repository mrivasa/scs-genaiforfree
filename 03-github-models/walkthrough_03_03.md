* Open the terminal panel *Ctrl-\`* and install the `openai` package
    ```bash
    pip install openai
    ```
* In your codespace, create a new file named `chat.py`
* Import the `os` module and the `OpenAI` client class from the `openai` module
    ```python
    import os
    from openai import OpenAI
    ```
* Get your personal access token from the environment variables
    ```python
    token = os.getenv("GH_MODELS_TOKEN", "")
    ```
* Create an instance of the `OpenAI` client class.  Pass the initializer keyword arguments for the `base_url` and the `api_key`
    ```python
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key=token
    )
    ```
* Read the contents of `customer_service_prompt.txt`
    ```python
    with open("customer_service_prompt.txt", "r") as f:
        customer_service_prompt = "".join(f.readlines())
    ```
* Create a system message.  This is a dictionary with a `role` key set to `system` and the `content` key set to `customer_service_prompt`.
    ```python
    system_message = {
        "role": "system",
        "content": customer_service_prompt
    }
    ```
* Create a user message.  This is a dictionary with a `role` key set to `user` and the `content` key set to the prompt.
    ```python
    user_message = {
        "role": "user",
        "content": "I was charged twice for the same item. What do I do?"
    }
    ```
* To generate a response call the `client.chat.completions.create` method.  The method accepts a keyword argument for the list of messages.  Pass it the `system_message` and `user_message`.  You can also pass keyword arguments for the `temperate` and `top_p`.  And pass another keyword argument for the `model`.
    ```python
    response = client.chat.completions.create(
        messages=[system_message, user_message],
        temperature=0.3,
        top_p=0.7,
        model="openai/gpt-4.1-mini"
    )
    ```
* The `create` method will return a response that can have multiple completions.  (By default it is just one.)  Those completions are in a list of `choices`.  Each choice has a `message` which has `content`.  That is the text of the response.
    ```python
    print(response.choices[0].message.content)
    ```
