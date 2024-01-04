# 🤖 ChatGPT for TeXstudio

Enhance your TeXstudio experience with the power of AI! These macros leverage OpenAI's technology to provide intelligent suggestions and improvements to your LaTeX documents. 
Watch this video to see it in action:

https://user-images.githubusercontent.com/79723245/230745138-730ee0de-c1d1-4b48-8b08-7d099e9dd52f.mp4

# 🧠 How does it work


The ChatGPT Macro for TeXstudio is a user-friendly integration that connects TeXstudio with OpenAI's API.
The first macro  `ChatGPT` allows you to send selected text from your document to a Python script, which interacts with the API and processes the response. 
The response text is  inserted directly into your editor, creating an intuitive and interactive ChatGPT experience.
The secondary macro, `ChatGPT-PromptLibrary`, offers a collection of predefined prompts accessible through a dropdown menu, allowing you to easily apply them to any selected text.

# 🚀 Getting Started

*Note: this macro was developed and tested on Ubuntu 22.04 but should also run on Windows and Mac.*

Follow these simple steps to set up the ChatGPT Macro for TeXstudio:

### Prerequisites

<details>
  <summary> <b>1. Install the latest version of TeXstudio</b> </summary>

Make sure you're using TeXstudio version `4.5.2rc1` or higher. To check your version, go to "Help" -> "About TeXstudio."

If you need to update, download the latest version from the [TeXstudio release page](https://github.com/texstudio-org/texstudio/releases).

For Linux users, download the `*AppImage`, make it executable (`chmod +x filename`), and run it.
</details>

<details>
  <summary> <b>2. Install Python and the OpenAI Python library</b> </summary>

Install Python from the [official website](https://realpython.com/installing-python/).

Install the `openai` Python library. Open a terminal and run `pip install openai`.
</details>

<details>
  <summary> <b>3. Obtain an OpenAI API key</b> </summary>

Create an account at [openai.com](https://chat.openai.com/auth/login) and get your API key from the [OpenAI API Keys page](https://platform.openai.com/account/api-keys). It will be only shown once, so save it somewhere for the next step.
</details>


### Step 1: Set up the Python script
 
- Download the [openai_python_script](/openai_python_script.py).
  - by clicking on `raw` -> Save as... (Ctrl + S)
- Make it executable.
- Open the script and insert your OpenAI API key.
- Note the absolute filepath of the script.

### Step 2: Import the macro into TeXstudio
- Download both macros [ChatGPT.txsMacro](/ChatGPT.txsMacro) and [ChatGPT-PromptLibrary.txsMacro](/ChatGPT-PromptLibrary.txsMacro).
  - by clicking on `raw` -> Save as... (Ctrl + S)
  - save both files as `ChatGPT.txsMacro` and `ChatGPT-PromptLibrary.txsMacro` (don't add a file ending like .txt)
- Import it into TeXstudio.
  -  Macros -> Edit Macros... -> Import
- Edit both macro:
  - Macros -> Edit Macros... 
  - Update the `script_path` variable with the absolute filepath of the Python script you noted in Step 1.
  - Verify that the Python path is correct (type `which python3` in the terminal and paste the result into the macro).

### Step 3: Enjoy the ChatGPT Macro

Now you're all set! Highlight any text in your document and run the macros using the shortcuts Shift+F1 and Shift+F2 or by clicking on it. The first time you execute the macros they ask you `Do you trust this script?` if you click `Yes, allow all calls it will ever make` this message will not be shown to you again.

# ⚙️ Advanced

### Stop a Running Script
If you have executed the macro and you want to stop it (because the response is to long or not what you expected) then just click on `Macro` -> `Stop ChatGPT` or `Stop ChatGPT PromptLib`. These two menu options are dynamically generated when the Macros are executed and not visible if the Macros where never executed.

Screenshot of the menu:

<img src="https://user-images.githubusercontent.com/79723245/235262063-53c46478-6d01-4c7b-b885-0df57307ac8d.png" width="300"/>


### Change the parameters in the python script

Within the Python script, you have the ability to modify various parameters to fine-tune the generated response:

- **system message**: The system message determines the behavior of the assistant. By default, ChatGPT uses *"You are a helpful assistant."* for this macro, it has been modified to *"You are a helpful assistant and an expert LaTeX editor. You only return valid LaTeX. Everything you return is directly inserted into a LaTeX document and interpreted as LaTeX code."*
- **model**: The model is set to `gpt-3.5-turbo`. If you have access to GPT4 you can switch it to `gpt-4`.
- **max_tokens**: This parameter sets the maximum length of the response. The total token limit for a single request with `gpt-3.5-turbo` is 4000 (approximately 6 pages of text), including the input. If your input consists of 3000 tokens, the response can only be 1000 tokens long. By default, this is set to 3000, meaning your maximum input can be 1000 tokens (roughly 1.5 pages of text). If you use `gpt-4`then I recommend `max_tokens=5000`.
- **temperature**: [see official documentation](https://platform.openai.com/docs/api-reference/chat/create#chat/create-temperature)


# 📍 Roadmap

- [x] add a prompt library
- [x] add the functionality to abort a running call
- [ ] make the max_tokens dynamically, depending on the length of the input
- [ ] improve prompts in the prompt library
- [ ] use any selected text as input (even special characters)
- [ ] include feedback about used token / used money
- [ ] parse errors and finish reason

# 💪 Contribute
You have some ideas on how to improve the macros or tips on how to make them run on different systems? Don't hesitate
- create an [issue](https://github.com/icarecti/chatgpt_macro_for_texstudio/issues) 
- open a pull request


# 📚 FAQ

### ❓ The response of ChatGPT has no empty spaces. Why is that?

**A:** If your TeXstudio version is older than `4.5.2rc1`, then empty spaces are removed by TeXstudio while reading the response. This issue was resolved with version `4.5.2rc1`.

### ❓ Why is it so slow in generating text?

**A:** When you create an account at OpenAI, you receive a free credit that expires after a few months. Using only this free credit results in slower response times. Adding a payment option to your OpenAI account significantly improves the response time, as demonstrated in the introduction video above.

### ❓ How can I add my own prompt to the prompt-library?

**A:** Adding your own prompt is a breeze! Just follow these simple steps:

1. Navigate to `Macros > Edit Macros...`
2. Click on `ChatGPT-PromptLibrary.`
3. Add a line in the following format:

``` { promptOption: "text that will be displayed in the dropdown", basePrompt: "command that will be sent to ChatGPT" } ```

### ❓ How expensive is it to use this macro?

**A:** The macro itself is completely free! However, OpenAI does charge a small fee for each request made to their API. The costs are quite minimal, so you can easily generate a large amount of content without breaking the bank.

To give you an idea, the current pricing for the `gpt-3.5-turbo` model is $0.002 per 1,000 tokens. You can check the most up-to-date pricing information on the [OpenAI Pricing page](https://openai.com/pricing).

**💡 Examples of Costs**
- Generate the entire Harry Potter book series (7 books, 2,200 pages) for just $3.
- Create 100 pages of text (including input) for a mere 10 cents.
