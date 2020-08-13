var apiUrl = "http://localhost:5000/api/chat";

        $(document).ready(function(){
            $("#send").click(function(){
                console.log('SENDING MESSAGE');
                var chat = $('#message').val();
                message = {message : chat}
                console.log(message)
                $.post(apiUrl,message, 
                    function(data, status, jqXHR) {
                        $('#history').append('YOU : ' + chat + '<br>');
                        $('#history').append('VOCOBOT : ' + data + '<br>');
                    })

                $('#message').val('');
            });
            $('#message').keypress(function (e) {
                var key = e.which;
                if(key == 13)  // the enter key code
                {
                    $('#send').click();
                    return false;  
                }
                });  


               
        });