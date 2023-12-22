# ChatGPT Integration with External Plugins

This Python script integrates the OpenAI GPT-4 model with external plugins for various tasks. It allows natural language interaction with GPT-4 and execution of specific actions based on responses.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/Saturn91/GPT-Assistant.git
cd GPT-Assistan
```

2. Install required libraries:

```bash
pip install requests
```
3. Set up your OpenAI API Key in API_KEY.json as shown in the template file

4. Run the script:
```bash
python start.py
```

5. Interact via natural language input.

# External Plugins

1. sendEmail: Sends emails based on input.
2. doCommit: Commits changes to a Git repository.
3. ... (the other two are not implemented)

Add more plugins by creating Python files and updating the pluginDict.

License
```
This project is licensed under the MIT License. See LICENSE for details.
```
