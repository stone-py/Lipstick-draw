
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

app.config['SECRET_KEY'] = '00000'



@app.route('/')
def test():
    return render_template("/kouhong.html")


@app.route('/kouhong_json')
def kouhong_json():
    
    data = {
        "kouhonglist": ['阿玛尼415', '阿玛尼206', '阿玛尼400金管',
                        '植村秀AMRD174','植村秀AMRD364',
                        'CHANEL 106','CHANEL 98','CHANEL 92',
                        '纪梵希 N333','纪梵希 306',
                        'Bobbibrown 4 Ruby','Bobbibrown 6 cranberry']
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
