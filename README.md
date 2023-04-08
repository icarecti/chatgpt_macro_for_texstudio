# ChatGPT for TeXstudio

Enhance your TeXstudio experience with the power of AI! These macros leverage OpenAI's technology to provide intelligent suggestions and improvements to your LaTeX documents. 
Watch this video to see it in action:

https://user-images.githubusercontent.com/79723245/230682343-96f56329-1ad7-4c60-bae3-f6a15741df59.mp4


# How does it work

The ChatGPT Macro for TeXstudio is a user-friendly integration that connects TeXstudio with OpenAI's API.
The first macro  `ChatGPT` allows you to send selected text from your document to a Python script, which interacts with the API and processes the response. 
The response text is  inserted directly into your editor, creating an intuitive and interactive ChatGPT experience.
The secondary macro, `ChatGPT-PromptLibrary`, offers a collection of predefined prompts accessible through a dropdown menu, allowing you to easily apply them to any selected text.

# Getting Started

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
- Download both macros [ChatGPT.txsMacro](/ChatGPT.txsMacro) and [ChatGPT-PromptLibrary.txsMacro](/ChatGPT-PromptLibrary.txsMacro).
  - by clicking on `raw` -> Save as... (Ctrl + S)
- Import it into TeXstudio.
  -  Macros -> Edit Macros... -> Import
- Edit the macro:
  - Macros -> Edit Macros... 
  - Update the filepath of the Python script with the one you noted in Step 1.
  - Verify that the Python path is correct (it should match the output of `which python3` in the terminal).

### Step 3: Enjoy the ChatGPT Macro

Now you're all set! Highlight any text in your document and run the macros using the shortcuts Shift+F1 and Shift+F2 or by clicking on it. Watch as the power of AI enhances your LaTeX documents!

# Advanced

## Add your own prompt to the prompt library
Adding your own prompt is as easy as just adding one line to the macro script:

`{ promptOption: "text that will be displayed in the dropdown", basePrompt: "command that will be sent to ChatGPT" }`
  
## Change the parameters in the python script

Within the Python script, you have the ability to modify various parameters to fine-tune the generated response:

- **system message**: The system message determines the behavior of the assistant. By default, ChatGPT uses *"You are a helpful assistant."* for this macro, it has been modified to *"You are a helpful assistant and an expert LaTeX editor. You only return valid LaTeX. Everything you return is directly inserted into a LaTeX document and interpreted as LaTeX code."*
- **model**: The model is set to `gpt-3.5-turbo`. If you have access to GPT4 you can switch it to `gpt-4`.
- **max_tokens**: This parameter sets the maximum length of the response. The total token limit for a single request with `gpt-3.5-turbo` is 4000 (approximately 6 pages of text), including the input. If your input consists of 3000 tokens, the response can only be 1000 tokens long. By default, this is set to 3000, meaning your maximum input can be 1000 tokens (roughly 1.5 pages of text).
- **temperature**: [see official documentation](https://platform.openai.com/docs/api-reference/chat/create#chat/create-temperature)