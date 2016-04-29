jQuery(document).ready(function($) {
    $("#btn_submit").click(function(){
        username = $('#username').val();
        password = $('#password').val();
        var _xsrf = getCookie('_xsrf');
        $.ajax({  
            type:'post',
            url:'/login/',
            data:{'username': username, 'password': password, '_xsrf': _xsrf},
            dataType:'json',
            success:function(data){
                alert(data);
            }
        });
    });
})
