from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Директория для хранения данных пользователей
DATA_DIR = "data"

# Проверяем существование директории, если нет - создаем
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Главная страница сайта
@app.route("/")
def home():
    return render_template("index.html")

# Страница регистрации
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]  # Получаем введенный пароль

        # Записываем данные в текстовый файл
        with open(os.path.join(DATA_DIR, f"{username}.txt"), "w") as f:
            f.write(f"Username: {username}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Password: {password}\n")  # Сохраняем пароль

        # После успешной регистрации перенаправляем пользователя на другой сайт
        return redirect("https://www.onlinegdb.com/")  # Замените URL на нужный

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True, port=8084)  # Указываем порт 8084
