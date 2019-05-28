from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    poem = {
        'title':'Tĩnh Dạ Tử',
        'body': 'Nội dung bài thơ',
        'author' : 'Lý Bạch',
        'gender' : 0
    }

    poems = []
    poems.append(poem)
    poems.append({
        'title':'Thúy Kiều',
        'body': 'Nội dung bài thơ',
        'author' : 'Nguyễn Du',
        'gender' : 1
    })

    poems.append({
    'title':'Con Rơi',
    'body': 'Nội dung bài thơ',
    'author' : 'Bá Hòa',
    'gender' : 1
})

    return render_template('index.html', data = poems)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
