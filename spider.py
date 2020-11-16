import requests

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
def get_bd_msg(keyword):

    header={
        'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    result=requests.get('https://www.baidu.com/s?wd={}'.format(keyword),headers=header).text
    result=result.replace("//www.baidu.com/img/flexible/logo/pc/result.png",'static/images/停车场.JPG')
    return result

get_bd_msg('学校')