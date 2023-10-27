from flask import Flask, request, render_template

app = Flask(__name__)

# Load the whitelist from a file
with open('whitelist.txt') as f:
    whitelist = [line.strip() for line in f]

@app.route('/', methods=['GET', 'POST'])
def wallet_checker():
    if request.method == 'POST':
        user_wallet = request.form['wallet']
        if user_wallet in whitelist:
            result = "You are whitelisted."
        else:
            result = "You are not whitelisted."
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()