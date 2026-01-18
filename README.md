# 🤖 AI Image & Info Assistant

A dual-purpose AI assistant designed to generate high-quality images from text prompts and provide detailed information/answers to your questions.

## 🌟 Features

### 1. 🎨 AI Image Generation
* **Text-to-Image:** Converts your creative descriptions into visual art.
* **Auto-Save:** Automatically saves every generated image to a local `/images` folder so you never lose your creations.
* **Customizable:** Supports various styles (e.g., realistic, anime, cyberpunk) based on your prompt.

### 2. 🧠 Information Assistant
* **Knowledge Retrieval:** Ask questions on any topic and receive instant, accurate summaries or detailed explanations.
* **Context Aware:** Capable of understanding follow-up questions [Optional: remove if not true].

## 🛠️ Tech Stack

* **Programming Language:** [e.g., Python 3.10 / Node.js]
* **AI Models:**
    * *Images:* [e.g., OpenAI DALL-E 3 / Stable Diffusion / Midjourney]
    * *Text:* [e.g., OpenAI GPT-4 / Gemini / Llama 2]
* **Key Libraries:** [e.g., `openai`, `requests`, `pillow`, `dotenv`]

## 🚀 Getting Started

### Prerequisites
* [e.g., Python installed on your machine]
* An API Key from [e.g., OpenAI / Google / Hugging Face]

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    * Create a file named `.env` in the project folder.
    * Add your API key inside:
        ```
        API_KEY=your_secret_key_here
        ```

## 📖 How to Use

1.  **Run the Assistant:**
    ```bash
    python main.py
    ```

2.  **Choose Mode:**
    * Type `img` followed by your prompt to generate a picture.
        * *Example:* `img a futuristic city with flying cars`
    * Type `info` followed by your question to get answers.
        * *Example:* `info explain quantum computing in simple terms`

3.  **View Results:**
    * Text answers will appear in the console.
    * Images will appear in the `generated_images` folder.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the assistant.
