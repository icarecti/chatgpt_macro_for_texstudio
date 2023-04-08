# ChatGPT for TeXstudio

Enhance your TeXstudio experience with the power of AI! This macro leverages OpenAI's technology to provide intelligent suggestions and improvements to your LaTeX documents. 
Watch this video to see it in action:

https://user-images.githubusercontent.com/79723245/230682343-96f56329-1ad7-4c60-bae3-f6a15741df59.mp4


# How does it work
___

The ChatGPT Macro for TeXstudio is a user-friendly integration that connects TeXstudio with OpenAI's API. 
The macro sends selected text from your document to a Python script, which communicates with the API and processes the response. 
The enhanced text is then written back to your editor.

# Getting Started
___

Follow these simple steps to set up the ChatGPT Macro for TeXstudio:

### Prerequisites

<details>
  <summary> <b>1. Install the latest version of TeXstudio</b> </summary>

Make sure you're using TeXstudio version `4.5.2rc1` or higher. To check your version, go to "Help" -> "About TeXstudio."

If you need to update, download the latest version from the [TeXstudio release page](https://github.com/texstudio-org/texstudio/releases)

For Linux users, download the AppImage, make it executable, and run it
</details>

<details>
  <summary> <b>2. Install Python and the OpenAI Python library</b> </summary>

Install Python from the [official website](https://realpython.com/installing-python/).

Install the `openai` library by running `pip install openai`.
</details>

<details>
  <summary> <b>3. Obtain an OpenAI API key</b> </summary>

Create an account at [openai.com](https://chat.openai.com/auth/login) and get your API key from the [OpenAI API Keys page](https://platform.openai.com/account/api-keys).
</details>


### Step 1: Set up the Python script
 
- Download the [openai_python_script](/openai_python_script).
  - by clicking on `raw` -> Save as... (Ctrl + S)
- Make it executable.
- Open the script and insert your OpenAI API key.
- Note the absolute filepath of the script.

### Step 2: Import the macro into TeXstudio
- Download the macro [ChatGPT.txsMacro](/ChatGPT.txsMacro).
  - by clicking on `raw` -> Save as... (Ctrl + S)
- Import it into TeXstudio.
- Edit the macro:
  - Update the filepath of the Python script with the one you noted in Step 1.
  - Verify that the Python path is correct (it should match the output of `which python3` in the terminal).

### Step 3: Enjoy the ChatGPT Macro

Now you're all set! Highlight any text in your document and run the macro using the shortcut Shift+F1 or by clicking on it. Watch as the power of AI enhances your LaTeX documents!

