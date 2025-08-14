from app import create_app

app = create_app("production")  # Choose the environment

if __name__ == "__main__":
    app.run()