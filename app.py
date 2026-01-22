from flask import Flask, render_template, request
from services.text_service import extract_text_from_pdf
from services.question_service import generate_questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text", "")
        file = request.files.get("file")

        if file and file.filename:
            text = extract_text_from_pdf(file)

        questions = generate_questions(
            text=text,
            num=int(request.form["num"]),
            qtype=request.form["type"],
            difficulty=request.form["difficulty"]
        )

        return render_template("result.html", questions=questions)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
