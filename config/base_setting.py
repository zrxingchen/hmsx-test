# 设置服务器端口
SERVER_PORT = 8999
# 链接到数据库
SQLALCHEMY_DATABASE_URI ='mysql://root:2020312@127.0.0.1/hmsx_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# cookie
AUTH_COOKIE_NAME = '1903_hmsx' 

# 拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
] 
STATUS = {
    "1":"正常",
    "0":"已删除"
}
UPLOAD = {
    'ext' :['jpg','gif','bmp','jpeg','png'],
    'prefix_path':'\\web\\static\\upload',
    'prefix_url':'\\static\\upload\\'
}