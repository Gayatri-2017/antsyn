from flask import Flask, render_template, request, flash
# import area
import Synonyms
import Antonyms

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)
    
app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=["GET","POST"])
def login_page():
    # flash("Hi")
    error = ''
    try:
        if request.method == "POST":
            inp = request.form['textbox']
            # flash(inp)
            if inp != "" :
                # apa = Synonyms.helloworld()
                # print(apa)
                # flash("Hi")
                out = list(Synonyms.synonyms(inp))
                print(out[0])
                flash("Replacing with Synonyms")
                flash(out[0])
                out = " ".join(Antonyms.replace_negations(inp.split()))
                flash("Replacing 'not + word' with antonyms")
                flash(out)
                # out = area.area(inp)
            else:
                error = "Enter Text."
        return render_template("tryTextBoxFancy.html", error = error)
    except Exception as e:
        flash(e)
        return render_template("tryTextBoxFancy.html", error = error)