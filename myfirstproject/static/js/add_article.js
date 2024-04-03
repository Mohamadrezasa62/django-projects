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