# Zinix – Rule-Based AI Chatbot 🤖

Zinix is a simple rule-based AI chatbot developed using Python as part of **Artificial Intelligence Project 1 – Industrial Training at DecodeLabs**.

The chatbot simulates basic human interaction through predefined responses, dictionary-based knowledge mapping, and rule-based decision-making logic.

## 📌 Project Overview

Zinix is designed to demonstrate the fundamental concepts of rule-based artificial intelligence, including input sanitization, control flow, decision-making, and continuous user interaction.

Unlike machine learning-based chatbots, Zinix uses predefined rules and exact input matching to generate responses.

## ✨ Features

- **Rule-Based Responses:** Responds to predefined user inputs.
- **Input Sanitization:** Handles uppercase letters, punctuation, and extra whitespace.
- **Continuous Conversation:** Maintains interaction through a `while` loop.
- **Dictionary-Based Knowledge Base:** Stores predefined intents and responses.
- **Fallback Mechanism:** Provides a default response for unknown inputs.
- **Exit Commands:** Supports `bye`, `exit`, and `quit`.
- **Error Handling:** Handles keyboard interruption and end-of-input gracefully.

## 🛠️ Technologies Used

- Python 3
- Standard Python Libraries
  - `string`

## 📂 Project Structure

```text
Project 01/
│
├── ai_chatbot.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning the repository)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/DecodeLabs-Internship.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Project 01
   ```

3. Run the chatbot:

   ```bash
   python ai_chatbot.py
   ```

## 💬 Example Interaction

```text
Hi There, Welcome to Zinix!

You: hello
Zinix: Hello! How can I help you today?

You: what is your name
Zinix: I'm Zinix, a rule-based AI chatbot.

You: who created you
Zinix: I'm Zinix, a rule-based AI chatbot created by Nazibur Rahman.

You: I love you
Zinix: I appreciate your sentiment, but I'm just a chatbot.

You: bye
Zinix: Goodbye! Have a great day!
```

## 🧠 Concepts Demonstrated

- Rule-Based Artificial Intelligence
- Input Sanitization and Normalization
- Dictionary-Based Mapping
- Conditional Logic
- Continuous Loops
- Exception Handling
- Basic Human-Computer Interaction

## 🎯 Project Objective

The objective of this project is to understand how intelligent interfaces can be constructed using explicit programming rules and deterministic decision-making logic.

## 👨‍💻 Author

**Nazibur Rahman**

Artificial Intelligence Project 1
Industrial Training – DecodeLabs

---

⭐ If you find this project interesting, feel free to explore the code and experiment with additional chatbot responses.
