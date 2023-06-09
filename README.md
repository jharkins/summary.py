# Summary CLI Tool

This command-line interface (CLI) tool uses the OpenAI GPT model to generate summaries of input files. Provide the path to the file you want to summarize, and the tool will return a concise summary of its content.

## Installation

1. Clone the repository
2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Install the package locally:

```
python setup.py develop
```

4. Set up an API key for the OpenAI API. The tool will prompt you to enter your API key the first time it runs. The key will be stored in a `config.ini` file located in the project directory for future use.

## Usage

To get started, simply provide a file path as an argument, like this:

```
summary example.txt
```

The tool will output the summary generated by the GPT model.

## Credits

- Developed by Joe Harkins
- Utilizes the OpenAI GPT model, powered by ChatGPT

## License

This project is licensed under the terms of the MIT License. Please refer to the [LICENSE](LICENSE) file for more information.
