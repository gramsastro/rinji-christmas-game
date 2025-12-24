from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from engine import ChristmasTreeGame

# Initialize Flask app and game
app = Flask(__name__)
game = ChristmasTreeGame()

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    # Get incoming message and sender ID
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "").split(":")[-1]

    # Create Twilio response
    resp = MessagingResponse()
    msg = resp.message()

    # Welcome message
    if incoming_msg.lower() in ["hi", "hello", "start"]:
        msg.body("🎅 Welcome to Rinji’s Christmas Tree Game!\nPick a number between 1 and 25.")
    
    # If user sends a number
    elif incoming_msg.isdigit():
        number = int(incoming_msg)
        result = game.pick_number(sender, number)
        msg.body(result)
    
    # Invalid input
    else:
        msg.body("Please send a number between 1 and 25.")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
