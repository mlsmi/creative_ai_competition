# Creative AI Competition

This Python script uses OpenAI's gpt-4o model to generate creative responses to various prompts.

## Prerequisites

- Python 3.6 or higher
- OpenAI Python library

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/mlsmi/creative-ai-competition.git
    cd creative-ai-competition
    ```

2. Install the required Python library:
    ```
    pip install openai
    ```

3. Set up your OpenAI API key:
    - Open the `creative_ai_competition.py` file
    - Replace the empty string in `openai.api_key = ""` with your actual OpenAI API key

## Usage

1. Run the script:
    ```
    python creative_ai_competition.py
    ```

2. The script will generate responses for the predefined prompts and print them to the console.

3. To add or modify prompts, edit the `prompts` list in the `creative_ai_competition.py` file.

## Features

- Dynamic token limit calculation based on prompt specifications
- Automatic temperature adjustment for different types of prompts
- Creativity boosting for more imaginative responses
