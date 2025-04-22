import pybullet as p
import pybullet_data
import time
from openai import OpenAI
import pyttsx3

# Initialize OpenAI client
client = OpenAI(api_key="your-openai-api-key")  # Replace with your actual API key

# Initialize text-to-speech
engine = pyttsx3.init()

# Astronomy context
ASTRONOMY_CONTEXT = """
You are a helpful educational robot teaching basic astronomy.
Explain concepts simply and adapt based on feedback.
"""

# Get response from OpenAI
def get_response(prompt, context=ASTRONOMY_CONTEXT):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Start PyBullet simulation
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
robot_id = p.loadURDF("r2d2.urdf", [0, 0, 0.1])
p.setGravity(0, 0, -9.8)

font_id = None

while True:
    question = input("\nAsk the robot a question (or type 'exit'): ")
    if question.lower() in ['exit', 'quit']:
        break

    response = get_response(question)
    print("Robot says:", response)
    engine.say(response)
    engine.runAndWait()

    if font_id:
        p.removeUserDebugItem(font_id)
    font_id = p.addUserDebugText(response[:90], [0.5, 0, 1.2], textColorRGB=[0.2, 1, 0.5], textSize=1.2)

    for _ in range(120):
        p.stepSimulation()
        time.sleep(1. / 240.)

    feedback = input("Was that clear? (leave empty to skip, or add feedback): ")
    if feedback.strip():
        improved = get_response(
            f"Original question: {question}\nPrevious answer: {response}\nFeedback: {feedback}"
        )
        print("Robot (revised):", improved)
        engine.say(improved)
        engine.runAndWait()

        p.removeUserDebugItem(font_id)
        font_id = p.addUserDebugText(improved[:90], [0.5, 0, 1.2], textColorRGB=[1, 0.7, 0.1], textSize=1.2)

        for _ in range(120):
            p.stepSimulation()
            time.sleep(1. / 240.)

p.disconnect()
