# Lipstick-draw
女朋友想要一个口红的抽奖,就先做了一个demo


## 环境
+ python3.7
  
## 依赖
+ pip install flask
  
## 使用
[flask1.py](https://github.com/stone0011/Lipstick-draw/blob/master/flask1.py)中
```python
def kouhong_json():
    
    data = {
        "kouhonglist": ['阿玛尼415', '阿玛尼206', '阿玛尼400金管',
                        '植村秀AMRD174','植村秀AMRD364',
                        'CHANEL 106','CHANEL 98','CHANEL 92',
                        '纪梵希 N333','纪梵希 306',
                        'Bobbibrown 4 Ruby','Bobbibrown 6 cranberry']
    }
    return jsonify(data)
```
更改data中的数组即可（口红对应颜色未找到，现有颜色为常见口红色随机）
