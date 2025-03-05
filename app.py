from flask import Flask
app = Flask(main.py)

@app.route('/')
def home():
    return "✅ Flask is working on Render!"

if __name__ == '__main__':
    app.run(debug=True)
