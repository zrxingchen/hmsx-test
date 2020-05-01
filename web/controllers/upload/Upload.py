from flask import Blueprint,request
from application import app,db
import os,datetime

router_upload = Blueprint('upload_page',__name__)


@router_upload.route('/ueditor',methods=['POST,GET'])
def ueditor():
    return 



@router_upload.route('/pic',methods=['GET,POST'])
def pic():
    file_target = request.files
    print(file_target['pic'].filename)
    # 将图片保存到 static/upload/pic.jpg
    root_path = app.root_path+ app.config['UPLOAD']['prefix_path']
    file_dir = datetime.datetime.now().strftime("%Y%m%d")
    save_dir = root_path + "\\" + file_dir
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        
    
    #+'\\'+filename
    

    return 'pic'
    

