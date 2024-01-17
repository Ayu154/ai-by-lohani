from flask import Flask, render_template, request

app = Flask(__name__)

def chat_bot(user_input):
    if user_input.lower() == "hi":
        return "Hello"
    elif user_input.lower() == "who r u":
        return "I'm AI by Lohani Ayush"
    elif user_input.lower() == "who is your best friend":
        return "Kehnsika"
    elif user_input.lower() == "what is your name":
        return "haggu"
    elif user_input.lower() == "what year is today":
        return "In A.D its 2024, in B.S its 2080"
    elif user_input.lower() == "who is your father":
        return "Bhuwan Lohani"
    elif user_input.lower() == "who is your mother":
        return "Poonam Lohani"
    elif user_input.lower() == "exit":
        return "Goodbye!"
    else:
        return "I don't understand that question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chat_bot(user_input)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
