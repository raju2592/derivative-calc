$ = window.$;
MathJax = window.MathJax;

function handleInput(inputFunction) {
    $('#function').attr('disabled', 'disabled');
    $('#derivativeOutput').empty()
    $.ajax({
        url: '/getDerivative',
        type: 'GET',
        data: {function: inputFunction},
        success: function(response) {
            if(response.success) {
                var html = '';
                html += 'I claim that, ' + response.answer;
                html += '<br>';
                for(var i = 0; i < response.story.length; i++) {
                    html += response.story[i] + '<br>';
                }
                $('#derivativeOutput').append(html);
                $("#derivativeOutput").css("font-size","95%");
                $("#derivativeOutput").css("color","black");
                MathJax.Hub.Typeset();
            } else {
                $('#derivativeOutput').append('Can\'t understand, sorry :( :(');
                $("#derivativeOutput").css("font-size","100%");
                $("#derivativeOutput").css("color","red");
            }
            $('#function').removeAttr('disabled');
        },
        error: function(){
            alert('Something Went Wrong!');
            $('#function').removeAttr('disabled');
        },
    });
}

$(document).ready(function() {
    $('#inputForm').submit(function(e) {
        e.preventDefault();
        var inputFunction = $('#function').val();
        handleInput(inputFunction);
    });
    $('#inputForm').submit();
});
