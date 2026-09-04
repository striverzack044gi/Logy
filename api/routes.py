from flask import request, jsonify

from brain.brain import LogyBrain
from memory.memory import Memory


brain = LogyBrain()
memory = Memory()


def register_routes(app):

    @app.get("/")
    def home():

        return jsonify({
            "name": "Logy",
            "status": "online",
            "message": "Logy API is running."
        })

    @app.post("/chat")
    def chat():

        data = request.get_json(silent=True) or {}

        message = data.get("message", "").strip()

        if not message:

            return jsonify({
                "error": "Message is required."
            }), 400

        response = brain.think(message)

        # Local memory
        memory.add(
            message,
            response
        )

        return jsonify({
            "answer": response
        })

    @app.get("/memory")
    def get_memory():

        return jsonify({
            "memory": memory.get_recent()
        })

    @app.delete("/memory")
    def clear_memory():

        memory.clear()

        return jsonify({
            "message": "Memory cleared."
        })
