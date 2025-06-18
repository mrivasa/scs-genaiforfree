* Go to [GitHub](https://github.com)
* In the upper right, click on your profile picture
* Click **Settings**
* Scroll down until you see **Developer settings** on the left side. Click it.
* Expand **Personal access tokens on the left side**
* Click **Tokens (classic)**
* Click **Generate new token** and **Generate new token (classic)**
    * You may be asked to reauthenticate
* Add a **Note** to the token (i.e. SCS AI Demo).
* Leave the rest of the settings as is and click **Generate token** at the bottom of the screen.
* The generated token is shown. *Don't close this page yet!* You won't be able to see it again.
* In a new tab, go to github.com again.
* Click on your profile picture and **Settings**
* On the left, click **Codespaces**
* Under **Secrets**, click the **New secret** button
* Give the secret a **Name** (i.e. `GH_MODELS_TOKEN`)
* Paste the token into the **Value** textbox
* Under **Repository access**, select the name of the repository from which you created the Codespace.
* Click the **Add secret** button
* In your Codespace, a popup in the lower right will notify you that the secrets have changed and prompt you restart the Codespace.
* Open the Command Pallette (*Ctrl/Cmd-Shift-P*)
* Search for `jupyter` and select **Create: New Jupyter Notebook**
* Save the notebook in `03-github-models` as `secrets.ipynb`
* In the first cell import the `os` module, and execute the cell.
    ```python
    import os
    ```
* In the next cell, call the `getenv` function and pass it the name of the secret (i.e. `GH_MODELS_TOKEN`) you added to the repository.
    ```python
    token = os.getenv("GH_MODELS_TOKEN", "")
    ```
* Print out the last four character of the `token`
    ```python
    print(token[-4:])
    ```
* Go to [Exercise 03-03](https://github.com)