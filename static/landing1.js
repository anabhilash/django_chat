/**
 * Created by ABHILASH on 02-08-2016.
 */

    var login=document.getElementById("login")
    var register=document.getElementById("signup")
    var login_form=document.getElementById("login-form")
    var register_form=document.getElementById("register-form")
    var _close0=document.getElementsByClassName('close')[0]
    var _close1=document.getElementsByClassName('close')[1]
    var login_button=document.getElementById("login-button")
    _close0.onclick = function() {
        login_form.style.display = "none";
    }
    _close1.onclick = function() {
        register_form.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == login_form)
        {
            login_form.style.display = "none";
        }
        else
            if(event.target==register_form)
            {
                register_form.style.display = "none";
            }
    }

    login.onclick = function() {
        login_form.style.display = "block";
    }

    register.onclick = function() {
        register_form.style.display = "block";
    }


    function submitLogin() {
        $.ajax({
            type: 'post',
            url: window.location.host + '/login',
            data: {
                username: $('#login-username').val(),
                password: $("#login-password").val(),
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[1].value
            },
            success: function (response) {
                if (response == 'invalid') {
                    $('#_username').text('invalid credentials')
                } else {
                    window.location.href = '/'
                }
            }
        })
    }
    function submitRegister()
    {
        if($('#register-password').val()==$('#register-re-password').val())
        {
            $.ajax({
            type:'post',
            url: window.location.host + '/register1',
            data:{
                username:$('#register-username').val(),
                password:$('#register-password').val(),
                email:$('#register-email').val(),
                csrfmiddlewaretoken:document.getElementsByName('csrfmiddlewaretoken')[0].value
            }
        })
        }
        else {
            
        }
    }