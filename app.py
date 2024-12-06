from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('trangchu.html')

@app.route('/dangkynhanvien')
def dangkynhanvien():
    return render_template('dangkynhanvien.html')

if __name__ == '__main__':
    app.run(debug=True)
