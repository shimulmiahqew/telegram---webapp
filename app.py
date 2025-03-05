from flask import Flask
app = Flask("free Airdrop")

@app.route('/')
def home():
    return "✅ Flask is working on Render!"

if __name__ == '__main__':
    app.run(debug=True)
