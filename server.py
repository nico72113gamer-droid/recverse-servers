from flask import Flask, jsonify, request
import sys

app = Flask(__name__)



@app.route('/api/config/v1/amplitude', methods=['GET', 'POST'])
@app.route('/api/config/v2/parameters', methods=['GET'])
def get_config():
    print("[SERVER] Client requested configuration setup.", file=sys.stderr)
    return jsonify({
        "RegistrationEnabled": True,
        "LoginEnabled": True,
        "MultiplayerEnabled": True,
        "PhotonEnabled": True,
        "VoiceEnabled": True
    })


@app.route('/api/v1/login/authenticate', methods=['POST'])
@app.route('/api/v2/accounts/login', methods=['POST'])
def player_login():
    print("[SERVER] Processing player login attempt...", file=sys.stderr)
    return jsonify({
        "success": True,
        "Token": "recroom_revival_secure_session_token",
        "PlayerId": 99999,
        "Username": "RevivalPlayer",
        "DisplayName": "Player 1",
        "IsDeveloper": True
    })

@app.route('/api/avatar/v2/saved', methods=['GET'])
def get_avatar():
    print("[SERVER] Sending default avatar configurations.", file=sys.stderr)
    return jsonify({
        "OutfitJson": "{}",  # Empty brackets default to standard tutorial clothing
        "SkinColor": 0,
        "FaceType": 0
    })


@app.errorhandler(404)
def not_found(e):
    print(f"[UNKNOWN API CALLED]: {request.method} {request.path}", file=sys.stderr)
    if request.data:
        print(f"Body: {request.data.decode('utf-8', errors='ignore')}", file=sys.stderr)
    return jsonify({"error": "Endpoint not implemented yet"}), 404

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("      REC ROOM PYTHON REVIVAL SERVER IS LIVE       ")
    print("      Listening on: http://127.0.0.1:8080         ")
    print("--------------------------------------------------")
    app.run(host='127.0.0.1', port=8080, debug=True)