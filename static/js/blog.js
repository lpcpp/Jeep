jQuery(document).ready(function($) {
    $("#btn_submit").click(function(){
        title = $('#title').val();
        content = $('#content').val();
        var _xsrf = getCookie('_xsrf');
        $.ajax({  
            type:'post',
            url:'/blog/add/',
            data:{'title': title, 'content': content, '_xsrf': _xsrf},
            dataType:'json',
            success:function(data){
                if(data.status == 'success'){
                    window.location.href='/blog/list/';
                }else{
                    alert(data);
                }
            }
        });
    });
})
