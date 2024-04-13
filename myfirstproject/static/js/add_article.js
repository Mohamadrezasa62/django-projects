function add_comment_article(){
    // console.log('success');

    const article_id = $('#article_id').val()
    const text = $('#text').val()
    const is_answer = $('#is_answer').val()
    const comment_id = $('#comment_id').val()
    // console.log('sssss')
    // the address or syntax of get is wrong because it doesnt work
    $.get('/article/add-article-comment', {
        text: text,
        article_id: article_id,
        is_answer: is_answer,
        comment_id: comment_id
    }).then(res => {
        console.log(res);
        $('.response-area').html(res);
    });
}

var scrolled = 0;
function add_comment_answer(CommentId){
    $('#is_answer').val("1");
    $('#comment_id').val(CommentId);
    scrolled = scrolled + 2500;
    $( "#header" ).animate({
    scrollTop :  scrolled
    });
    // alert( " Scrolled down " +scrolled+ " Px." );
}

