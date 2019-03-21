$(()=>{
    listenInput()
    console.log(window.location)
    // $('#entranceVideo').hide()
})
function listenInput(){
    $("#riddle").keyup(function(){
        const input = $(this).val()
        setTimeout(function () {
            if(input.toLowerCase()=='mellon'){
                console.log("YESS")
                $(".gateOfMoriaImg").hide()
                $(".myCustomText").hide()
                var vid = document.getElementById("entranceVideo");
                $('#entranceVideo').show()
                verifyFriend()
                vid.play()
                vid.addEventListener('ended',function(){
                    console.log("ended")
                    window.location.href = 'welcome'
                },false)
            }
        }, 700);
    })
}

function verifyFriend(){
    let csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: 'verifyFriend',
        data: {
            csrfmiddlewaretoken: csrftoken 
        },
        success:function(data){

        }
    })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}