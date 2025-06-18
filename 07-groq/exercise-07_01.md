* Go to [groq.com](https://groq.com)
* Click the **DEV CONSOLE** buttcon
* Click the **Login with GitHub** button
* Follow the onboarding steps to create your account
* In the Dev Console click the **Playground** link at the upper right.
* This is similar to the playground in GitHub Models
* Click on the **Dashboard** link at the upper right
* Click on the **API Keys** link at the upper right
* Click the **Create API Key** button
  * Enter a name to the API key
  * Click the **Submit** button
  * Copy the API key **before** closing the dialog.  You won't be able to retrieve it later.
  * Store the API key as a secret for your fork of the workshop repository on GitHub (see [Exercise 03-02](https://github.com) for details)
* In your Codepsace, open the terminal panel (*Ctrl-\`*) and install the `groq` Python package.
  ```bash
  pip install groq
  ```
* In `07-groq` create a new file named `chat.py`.
* Copy and paste the contents of `03-github-models/chat.py`
* Replace the line
  ```python
  from openai import OpenAI
  ```
  with
  ```python
  from groq import Groq
  ```
* Replace the line creating the `OpenAI` client with
  ```python
  client = Groq(api_key=os.getenv("GROQ_API_KEY")) # replace GROQ_API_KEY with the name of your secret
  ```
* In the line that calls the `create` method, set the `model` keyword argument to `llama-3.3-70b-versatile`
