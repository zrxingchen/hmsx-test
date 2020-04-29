;
var user_login_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".login_wrap .do-login").click(function(){
            // btn
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")) {
                alert('请不要重复提交')
                return;
            }
            var login_name = $(".login_wrap input[name=login_name]").val()
            var login_pwd = $(".login_wrap input[name=login_pwd]").val()

            // 前端校检 不为空，长度不小于1
            if(login_name == undefined || login_name.length < 1){
                alert('您输入的用户名为空')
                return;
            }
            if(login_pwd == undefined || login_pwd.length < 1){
                alert('您输入的密码为空')
                return;
            }

            btn_target.addClass("disabled")

            // Ajax 前后端分离的 ,数据格式是json {key:value},
            // 前端发送的数据是json格式的，所以后端response 返回的数据也得是json格式的
            $.ajax({
                url:"/user/login",
                type:"POST",
                data:{"login_name":login_name,"login_pwd":login_pwd},
                dataType:"json",
                success:function(response){
                    btn_target.removeClass("disabled")
                    alert(response.msg)
                    console.log(response)
                    window.location.reload()
                }
            })

        })    
    }
}
$(document).ready(function(){
    user_login_ops.init()
})