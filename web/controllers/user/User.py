from flask import Blueprint,render_template
from flask import Blueprint,render_template,request,jsonify
from common.models.User import User
from common.libs.user.UserService import UserService


router_user = Blueprint('user_page',__name__)

@router_user.route("/login")
@router_user.route("/login",methods=["GET","POST"])
def login():
    
    if request.method == "GET":
        return render_template('user/login.html')

    resp = {
        'code':200,
        'msg':'登录成功',
        'data':{}
    }
    req = request.values
    login_name = req['login_name']
    login_pwd = req['login_pwd']
    # 后端校检 不为空  长度不小于1
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的用户名~~~"
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码~~~"
        return jsonify(resp)


    
    # 数据库比对
    user_info = User.query.filter_by(login_name=login_name).first()

    if not user_info:
        resp['code'] = -1
        resp['msg'] = "用户不存在"
        return jsonify(resp)
    
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = "账号已经被禁用，请联系管理员处理"
        return jsonify(resp)
    
    if user_info.login_pwd !=  UserService.generatePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "密码错误"
        return jsonify(resp)

    return jsonify(resp)
