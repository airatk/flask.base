from app import app as application


if __name__ == "__main__":
    application.run(host="0.0.0.0", port="3000", debug=True)
