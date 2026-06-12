from flask import Flask, request, redirect, session, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = "shopacc_secret_key"

# Tạo database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        balance INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    username = session.get("username")

    if username:
        return f"""
        <h1>Shop Acc Roblox</h1>
        <p>Xin chào {username}</p>
        <a href='/logout'>Đăng xuất</a>
        """
    
    return """
    <h1>Shop Acc Roblox</h1>
    <a href='/login'>Đăng nhập</a><br><br>
    <a href='/register'>Đăng ký</a>
    """

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()

            c.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )

            conn.commit()
            conn.close()

            return redirect("/login")

        except:
            return "Tên tài khoản đã tồn tại"

    return """
    <h2>Đăng ký</h2>

    <form method="POST">
        <input name="username" placeholder="Tên tài khoản">
        <br><br>

        <input type="password" name="password" placeholder="Mật khẩu">
        <br><br>

        <button type="submit">Đăng ký</button>
    </form>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = c.fetchone()
        conn.close()

        if user:
            session["username"] = username
            return redirect("/")

        return "Sai tài khoản hoặc mật khẩu"

    return """
    <h2>Đăng nhập</h2>

    <form method="POST">
        <input name="username" placeholder="Tên tài khoản">
        <br><br>

        <input type="password" name="password" placeholder="Mật khẩu">
        <br><br>

        <button type="submit">Đăng nhập</button>
    </form>
    """

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
