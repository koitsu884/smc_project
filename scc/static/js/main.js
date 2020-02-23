const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


$(document).ready(function () {
  setTimeout(function () {
    $('#message').fadeOut('slow');
  }, 6000);

  $('#lang img').click(function (e) {
    let parent = $(this).parent();
    // console.log($(this).attr('data-lang'));
    // console.log(parent.attr('data-url'));
    // console.log($("[name='csrfmiddlewaretoken']"));
    // console.log(e);
    $.post(parent.attr('data-url'), {
      'language': $(this).attr('data-lang'),
      'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']")[0].value
    }, function () {
      location.reload(true)
    })
    //  alert($(this).find("span.t").text());
  });

  $('#BackTop').click(function () {
    $('html,body').animate({scrollTop: 0}, 500);
  });
  $(window).scroll(function () {
      if ($(this).scrollTop() > 300) {
          $('#BackTop').fadeIn(300);
      } else {
          $('#BackTop').stop().fadeOut(300);
      }
  }).scroll();
});