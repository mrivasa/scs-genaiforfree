* In your Codespace open the terminal panel (*Ctrl-`*)
* Go to the [Ollama](https://ollama.com) web site
* Click the **Download** button
* The site will prompt you to download an installer for the operating system you are you.  But your Codespace uses Linux so click on the Linux icon.
* Copy the installation command and run it in the terminal panel.  This will take a few seconds.
* In the meantime, click on the **Models** link in the upper left of the Ollama web site
* This is a catalog of all the models that can be served by Ollama.  Theoretically you can run most models from the Hugging Face catalog that have a GGUF format but that's beyond the scope of this exercise.
* Back in your Codespace, the install should be finished.  You'll see a message prompting you to install lspci or lshw to detect a GPU. You can ignore this message as your Codespace does not have a GPU.
* Run `ollama` in the terminal panel to see the different commands.
* Start the Ollama server with the command `ollama serve`
* You'll need to open another terminal by clicking on the plus icon in the upper right of the terminal panel. (it will likely say `ollama` to the left)
* Run the `ollama ls` command to see a list of the currently downloaded models.  Right now it is empty.
* Use the `ollama pull` command to download a model.  Since your Codespace has only 8GB of memory (and about 5GB or so is free) and no GPU, you'll need to use small model, about 3B or less parameters.  Go to the Ollama catalog and at the top of the page, search for `llama3.2`
* Click the link for the Llama 3.2 model card.
* Notice that Llama 3.2 has two sizes, 1B and 3B.  To download a model use the `ollama pull` command followed by the name of the model (`llama3.2`) a colon, and the size.  To get the 1B parameter model use 
    ```
    ollama pull llama3.2:1b
    ```
* Run `ollama ls` again to see the model.
* If you a seeing commonalities with the Docker CLI, you're not dreaming.  Use the `ollama run` command, followed by the full name of the model, to serve it and start the chat prompt.
* Send the model a prompt: `What is a benefit of using retrieval-augmented generation?` You'll notice that the response is a little slow but that's because even with a 'small' large language model, a GPU makes a big difference.
* Send the `/?` command to see other commands you can use to configure the LLM.
* The `/set` command lets you assign values for system prompts and otehr variables
* Run `/set parameter` to see a list of parameters you can set.  Some of these should look familiar.
* Set a system message.  Let's try a whimsical one.
    ```
    /set system "You are the WOPR computer from the movie Wargames.  Respond as it would."
    ```
* Verify that the system message was set with the `/show system` command.
* Set the temperature to 1.0 and the top_p to 1.0 to really give the model creative license.
    ```
    /set parameter temperature 1.0
    /set parameter top_p 1.0
    ```
* Verify the parameters were set with the `/show parameters` command
* Send the model this line from the movie: `How about a nice game of chess?`
* Exit the chat prompt with the `/bye` command
* Stop the model with 
    ```
    ollama stop llama3.2:1b
    ```