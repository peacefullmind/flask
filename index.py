from flask import Flask
from flask import render_template
from  flask import request
from spider import get_bd_msg

app=Flask(__name__)

#装饰器
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return 'demo yemian'

@app.route('/s')
def search():
    keyword=request.args.get('wd')
    html=get_bd_msg(keyword)
    return html

if __name__=='__main__':
    app.run(debug=True)