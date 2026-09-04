from api.api import create_app
from config.config import HOST, PORT, DEBUG


app = create_app()


if __name__ == "__main__":

    print("================================")
    print("          LOGY AI")
    print("================================")
    print(f"Server: http://{HOST}:{PORT}")
    print("Status: Online")
    print("================================")

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )
