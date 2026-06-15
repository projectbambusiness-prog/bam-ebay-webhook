from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "BAM Online"

@app.route("/ebay/account-deletion", methods=["GET", "POST"])
def account_deletion():

    challenge = request.args.get("challenge_code")

    if challenge:
        return jsonify({
            "challengeResponse": challenge
        })

    return jsonify({
        "status": "received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)