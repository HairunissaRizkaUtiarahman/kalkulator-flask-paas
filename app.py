from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operator = request.form.get("operator")

            if operator == "add":
                result = num1 + num2
            elif operator == "subtract":
                result = num1 - num2
            elif operator == "multiply":
                result = num1 * num2
            elif operator == "divide":
                if num2 == 0:
                    result = "Error: tidak bisa bagi 0"
                else:
                    result = num1 / num2
        except:
            result = "Input tidak valid"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
