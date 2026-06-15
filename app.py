from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "BAM_DELETE_VERIFY_2026_JACK_HUFF_784913"

ENDPOINT_URL = "https://bam-ebay-webhook.onrender.com/ebay/account-deletion"


@app.route("/")
def home():
    return "BAM Online"


@app.route("/ebay/account-deletion", methods=["GET", "POST"])
def account_deletion():

    challenge_code = request.args.get("challenge_code")

    if challenge_code:

        data = (
            challenge_code
            + VERIFICATION_TOKEN
            + ENDPOINT_URL
        )

        challenge_response = hashlib.sha256(
            data.encode("utf-8")
        ).hexdigest()

        return jsonify({
            "challengeResponse": challenge_response
        })

    return jsonify({
        "status": "received"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)