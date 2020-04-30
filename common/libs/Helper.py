from flask import render_template,g
import datetime
# 自定义渲染方法
def ops_render(template,context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template,**context)

# 获取当前时间，并格式化
def getCurrentDate():
    return datetime.datetime.now()