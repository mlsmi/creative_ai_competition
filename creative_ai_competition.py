import openai
import random
import re

# Enter your OpenAI API key here
openai.api_key = ""

# Prompts. Enter more, if needed
prompts = [
    "Write a motivational speech delivered by a sunflower to other plants in a garden. The speech should be no more than 60 words.",
    "Describe a surreal dessert that changes its flavor based on the eater's mood. Keep the description under 40 words.",
    "Invent a new sport that can only be played in zero gravity. Explain the rules and objective in 80 words.",
    "Imagine a conversation between a cloud and a mountain about the passage of time. The dialogue should be no more than 50 words.",
    "Suggest a creative way to use sound to paint a picture on a canvas without using any traditional painting tools. Explain in 70 words.",
    "Come up with a name and slogan for a fictional company that sells bottled lightning. Keep it within 25 words.",
]

def creativity_boost(prompt):
    """Add creativity-boosting elements to the prompt."""
    boosters = [
        "Think outside the box. Be wildly creative and unique.",
        "Imagine you're the most innovative thinker in the universe.",
        "Channel the spirit of Salvador Dali and Leonardo da Vinci combined.",
        "Pretend you're explaining this to a child who loves fantastical ideas.",
    ]
    return f"{prompt}\n\nCreativity Boost: {random.choice(boosters)}"

def extract_max_tokens(prompt):
    """Extract the maximum number of tokens based on various length specifications."""
    words_match = re.search(r'(\d+)\s*(?:words?|w)\s*(?:max|maximum|limit)', prompt, re.IGNORECASE)
    if words_match:
        return int(int(words_match.group(1)) * 1.8)  # Assuming 1.8 tokens per word on average

    lines_match = re.search(r'(\d+)\s*(?:lines?|l)\s*(?:max|maximum|limit)', prompt, re.IGNORECASE)
    if lines_match:
        return int(int(lines_match.group(1)) * 18)  # Assuming 18 tokens per line on average

    paragraph_match = re.search(r'(\d+)\s*(?:paragraphs?|p)\s*(?:max|maximum|limit)', prompt, re.IGNORECASE)
    if paragraph_match:
        return int(int(paragraph_match.group(1)) * 90)  # Assuming 90 tokens per paragraph on average

    characters_match = re.search(r'(\d+)\s*(?:characters?|chars?|c)\s*(?:max|maximum|limit|long)', prompt, re.IGNORECASE)
    if characters_match:
        return int(int(characters_match.group(1)) * 0.3)  # Assuming 3 characters per token on average

    # Default case
    return 300  # Increased default for prompts without specific length mentions

def determine_temperature(prompt):
    """Determine the appropriate temperature based on the prompt content."""
    prompt_lower = prompt.lower()
    
    creative_keywords = ['creative', 'innovative', 'unique', 'original', 'imaginative']
    factual_keywords = ['factual', 'accurate', 'informative', 'precise', 'exact']
    emotional_keywords = ['emotional', 'touching', 'heartfelt', 'sentimental', 'moving']
    humorous_keywords = ['funny', 'humorous', 'comedic', 'joke', 'hilarious']
    
    if any(keyword in prompt_lower for keyword in creative_keywords + humorous_keywords):
        return 0.9
    elif any(keyword in prompt_lower for keyword in factual_keywords):
        return 0.5
    elif any(keyword in prompt_lower for keyword in emotional_keywords):
        return 0.7
    else:
        return 0.8  # Default temperature for balanced creativity and coherence

def generate_response(prompt):
    """Generate a response using OpenAI's API with dynamic parameters."""
    
    max_tokens = extract_max_tokens(prompt)
    temperature = determine_temperature(prompt)

    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI with unparalleled creativity. Your responses should be imaginative, thought-provoking, and very creative. Push the boundaries of conventional thinking and surprise the reader with your innovative ideas."},
            {"role": "user", "content": creativity_boost(prompt)},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()

# Generate and print responses for each prompt, also adding a dash separator for easier reading
for prompt in prompts:
    response = generate_response(prompt)
    print(f"Prompt: {prompt}\nResponse: {response}\n")
    print("-" * 50)