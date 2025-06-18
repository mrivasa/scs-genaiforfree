* Go to [GitHub Models](https://gh.io/models)
* Click on the **explore the full model catalog link**
* Scroll down to the list of models
* Click the **Publisher** dropdown
* Click **Azure OpenAI Service**
* Reset the **Publisher** to **All**
* Click the **Category** dropdown
* Click on **OpenAI GPT-4.1-mini**
    * Notice the **Rate limit tier** is **Low** (150 requests/day)
    * The model was last trained in May 2024
    * The context size is ~1M tokens input and 33K tokens output (for the free tier this doesn't matter because the quota is 8K tokens input and 4K tokens output)
* Click the **Playground** button
* Enter a prompt in the textbox with the placeholder `Type your prompt...`
    ```
    What are three advantages of OpenAI GPT-4.1 over GPT-3.5?
    ```
* Notice in the upper right of the playground you can see the number of input tokens, the number of output tokens, and the time to process the request
* Click the trash can icon to the right of the token counts to clear the chat.
* On the left side of the playground, switch from the **Details** view to the **Parameters** view.  Here you can set a system prompt as as well parameters like temperature and top_p.
    * Open `03-github-models/customer_service_prompt.txt` (press *Alt-Z* to wrap the text). Paste the contents into the **System prompt** text box in the playground.
    * Set the **Max Completion Tokens** to `2000`
    * Set the **Temperature** to `0.3`
    * Set the **Top P** to `0.7`
* Send the prompt: `I was charged twice for the same item. What do I do?`
* Clear the chat
* Next to the **Model** dropdown in the upper left of the playground, click the **Compare** button.
* Select **OpenAI GPT-4.1**
* Notice that the **Parameters** for both models are the same.
* Paste the prompt: `I was charged twice for the same item. What do I do?` into one model and the other will be populated.
* Send the prompt.
    * Notice that the response for GPT-4.1 is a little longer and also uses formatting.
* Try another prompt: `I bought the wrong item. How can I return it?`
    * Again, GPT-4.1 is slightly more detailed and formatted more.
