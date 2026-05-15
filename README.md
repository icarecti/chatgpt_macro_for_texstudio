# 🤖 ChatGPT for TeXstudio

Enhance your TeXstudio experience with the power of AI! These macros leverage OpenAI's technology to provide intelligent suggestions and improvements to your LaTeX documents. 
Watch this video to see it in action:

https://user-images.githubusercontent.com/79723245/230745138-730ee0de-c1d1-4b48-8b08-7d099e9dd52f.mp4

# 🧠 How does it work


The ChatGPT Macro for TeXstudio is a user-friendly integration that connects TeXstudio with OpenAI's API.
The first macro  `ChatGPT` allows you to send selected text from your document to a Python script, which interacts with the API and processes the response. 
The response text is  inserted directly into your editor, creating an intuitive and interactive ChatGPT experience.
The secondary macro, `ChatGPT-PromptLibrary`, offers a collection of predefined prompts accessible through a dropdown menu, allowing you to easily apply them to any selected text.

# 🛠️ May 2026: Modern AI Options

This macro was developed in 2023 and is still working, but more AI solutions are now available for LaTeX and TeXstudio workflows.
For built-in TeXstudio support, see the official [AI Chat Assistant documentation](https://texstudio-org.github.io/advanced.html#ai-chat-assistant).
For a more agentic workflow, consider tools such as Claude Code or Codex CLI: AI agents that can be customized with plugins, skills, MCP servers, hooks, and similar extensions.
For an AI-first LaTeX editor and scientific workspace, [OpenAI Prism](https://openai.com/prism/) is another alternative.

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

- **developer message**: The developer message determines the behavior of the assistant. The script uses OpenAI's Responses API, where these instructions are sent with the `developer` role. Older Chat Completions examples often used the `system` role; for current OpenAI Responses code, keep `developer`.
- **model**: The model is set to `gpt-5.4-mini`.
- **reasoning**: The reasoning effort is set to `medium`.
- **max_output_tokens**: This parameter sets the maximum number of tokens generated for the response, including visible output and reasoning tokens. By default, this is set to 3000.

### Use a different AI provider

Some providers offer an OpenAI-compatible Python client setup, but their endpoint, role names, model names, and streaming format can differ. To adapt `openai_python_script.py`, change the client credentials and `base_url`, update the `model`, and use the provider's supported instruction role. For example, Chat Completions-style providers such as DeepSeek use `system`, `user`, `assistant`, and `tool` roles rather than OpenAI's `developer` role.

If the provider does not support OpenAI's Responses API, replace `client.responses.create(...)` with `client.chat.completions.create(...)`, pass `messages=message_log` instead of `input=message_log`, and use provider-supported parameters such as `max_tokens` instead of `max_output_tokens`.

Minimal Chat Completions-style shape:

```python
client = OpenAI(
    api_key="... your provider api key ...",
    base_url="https://provider.example/v1",
)

message_log = [
    {"role": "system", "content": "You are an expert LaTeX editor. Only return valid LaTeX."}
]
message_log.append({"role": "user", "content": prompt})

response = client.chat.completions.create(
    model="provider-model-name",
    messages=message_log,
    max_tokens=3000,
    stream=True,
)

for chunk in response:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```


# 📍 Roadmap

- [x] add a prompt library
- [x] add the functionality to abort a running call
- [x] use any selected text as input (even special characters)
- [ ] make `max_completion_tokens` dynamic, depending on the length of the input
- [ ] include feedback about used token / used money
- [ ] parse errors and finish reason

# 💪 Contribute
You have some ideas on how to improve the macros or tips on how to make them run on different systems? Don't hesitate
- create an [issue](https://github.com/icarecti/chatgpt_macro_for_texstudio/issues) 
- open a pull request


# 📚 FAQ

### ❓ The response of ChatGPT has no empty spaces. Why is that?

**A:** If your TeXstudio version is older than `4.5.2rc1`, then empty spaces are removed by TeXstudio while reading the response. This issue was resolved with version `4.5.2rc1`.


### ❓ How can I add my own prompt to the prompt-library?

**A:** Adding your own prompt is a breeze! Just follow these simple steps:

1. Navigate to `Macros > Edit Macros...`
2. Click on `ChatGPT-PromptLibrary.`
3. Add a line in the following format:

``` { promptOption: "text that will be displayed in the dropdown", basePrompt: "command that will be sent to ChatGPT" } ```

### ❓ How expensive is it to use this macro?

**A:** The macro itself is completely free! However, OpenAI does charge a small fee for each request made to their API. The costs are quite minimal, so you can easily generate a large amount of content without breaking the bank.

As of May 15, 2026, the configured `gpt-5.4-mini` model costs $0.75 per 1M input tokens and $4.50 per 1M output tokens with standard API pricing. Assuming one page of text is about 700 tokens:

- Rewrite 1 page and receive about 1 page back: about $0.0037.
- Rewrite 10 pages and receive about 10 pages back: about $0.037.
- Generate 100 pages of output: about $0.315, plus the cost of your input and any reasoning tokens.

These are rough reference values. Pricing changes over time, so check the official [OpenAI Pricing page](https://openai.com/pricing) for current pricing.
