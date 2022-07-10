from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def init_checkerboard():
    return render_template("index.html", rows=8, cols=8, color_1="black", color_2="red")


@app.route('/<int:rows>/', methods=['GET'])
def change_rows(rows):
    return render_template("index.html", rows=rows, cols=8, color_1="black", color_2="red")


@app.route('/<int:rows>/<int:columns>/', methods=['GET'])
def change_rows_colums(rows, columns):
    return render_template("index.html", rows=rows, cols=columns, color_1="black", color_2="red")


@app.route('/<int:rows>/<int:columns>/<string:color_1>/', methods=['GET'])
def change_rows_colums_color(rows, columns, color_1):
    return render_template("index.html", rows=rows, cols=columns, color_1=color_1, color_2="red")


@app.route('/<int:rows>/<int:columns>/<string:color_1>/<string:color_2>/', methods=['GET'])
def change_rows_colums_colors(rows, columns, color_1, color_2):
    return render_template("index.html", rows=rows, cols=columns, color_1=color_1, color_2=color_2)


if __name__ == "__main__":
    app.run(debug=True)
