from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Shop Acc Roblox</h1>
    <p>Website đang hoạt động</p>
    <a href='/login'>Đăng nhập</a>
    """

@app.route("/login")
def login():
    return """
    <h2>Đăng nhập</h2>
    <input placeholder='Tên tài khoản'>
    <br><br>
    <input type='password' placeholder='Mật khẩu'>
    <br><br>
    <button>Đăng nhập</button>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
