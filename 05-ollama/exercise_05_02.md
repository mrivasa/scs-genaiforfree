* In your Codespace open the Extensions panel (*Ctrl/Cmd-Shift-X*)
* Search for `rest client`
* Install the extension by *Huachao Mao*
* Create a new file in `05-ollama` called `api.http`
* Run the Llama 3.2 model if it was stopped
    ```bash
    ollama run llama3.2:1b
    ```
* Ollama also starts a REST server on port 11434.  You can access it using the **REST Client** extension.
* Open the `api.http` file.  All HTTP requests are separated with three hashtags.
    ```
    ###
    ```
* The Ollama endpoint to list downloaded models is `/api/tags`.  Below the three hashtags in `api.http` issue a `GET` request to get the models.
    ```
    GET http://localhost:11434/api/tags
    ```
* Above the endpoint you'll see a **Send Request** link.  Click it to send the request to the API.
* You'll see a JSON response that lists the Llama 3.2 1B model you downloaded.
* To chat with Ollama via the REST API you'll need make a POST request to the `/api/chat` endpoint.  The body of the request will be a JSON object.  The only required key in the JSON object is `model` which is the name of the model to use, `llama3.2:1b` in this case.  And it's useful to provide an array of `messages` as well.  Similar to the GitHub Models demos, each message is a JSON object with a `role` and `content` key.  Here is the request to be added to `api.http`.
    ```
    POST http://localhost:11434/api/chat
    Content-Type: application/json

    {
        "model": "llama3.2:1b",
        "meesages": [
            {
                "role": "user",
                "content": "What benefits does retrieval augmented generated offer AI apps?"
            }
        ]
    }
    ```
* When you click **Send Request** it might seem like nothing happened.  But after several seconds, you'll get an HTTP response with a lot of JSON objects in the body.  Look closely at them.  Each one has a `message` key with an object that has a `content` key.  And the value of `content` is a token.  Also, the JSON objects all have a `done` key with a value of `false`.  Except for the last one.  Scroll down and notice the last JSON object has a `done` key with a value of `true`.  It also has the number of tokens in the prompt and request.
* The reason for the messy response is because the response is being streamed one token at a time.  You'll notice when you use ChatGPT that you don't have to wait for the response to complete before you can see it.  You see the response as it is being generated.  That's what is happening here.  But since the **REST Client** extension doesn't support streaming, you have to wait for the entire response to be generated before you can see it.  That's why it seemed like nothing happened when you sent the request.  The **REST Client** extension was actually waiting for the response to finish.
* There is no workaround for waiting for the response to finish.  However, you can add a `stream` key to the request body and set it to `false`.  You'll stil have to wait on the response but at least it won't be split into tokens and you'll be able to read it.
* Run the `/bye` command to exit the chat prompt.
