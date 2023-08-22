from flask import Flask, render_template, request, redirect, url_for
from main import generateQR_Code

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    qr_code_result = None
    if request.method == 'POST':
        url = str(request.form['url'])
        qr_code_result = generateQR_Code(url)
    
    return render_template('index.html',
                           page_title = 'QR Code Generator',
                            qr_code_result = qr_code_result)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0" , port=8000)


