# 🤖 LLM-Powered Teaching Robot (PyBullet + GPT)

This prototype simulates a robot that teaches astronomy using a language model (GPT-3.5), built with PyBullet and Python.

## Features
- Real-time Q&A input
- Adaptive explanations using GPT
- Feedback-based learning
- Text-to-speech responses
- Lightweight and demo-ready

## Setup
1. Clone the repo or unzip this folder.
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Replace `"your-openai-api-key"` with your OpenAI key in `llm_teacher_pybullet.py`.
5. Run the robot:
   ```
   python llm_teacher_pybullet.py
   ```

## Demo
- Ask questions like "What is a black hole?"
- Give feedback like "That was too complex"
- Hear the robot speak the revised answer

## License
MIT License
