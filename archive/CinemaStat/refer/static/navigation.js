$(document).ready(function(){
  $(".info-button").click(function(){
    $(".body-pane").toggleClass("open");
    $(".dots-nav-container").toggleClass("open");
    $(".info-pane").toggleClass("open");
    $(".nav").toggleClass("not-fixed");
    $(".page-fade").fadeToggle("300");
  });
});

$(document).ready(function(){
  $(".page-fade").click(function(){
    $(".body-pane").toggleClass("open");
    $(".dots-nav-container").toggleClass("open");
    $(".info-pane").toggleClass("open");
    $(".page-fade").fadeToggle("300");
    $(".nav").toggleClass("not-fixed");
  });
});

$(document).ready(function(){
  $(".info-pane-close").click(function(){
    $(".body-pane").toggleClass("open");
    $(".dots-nav-container").toggleClass("open");
    $(".info-pane").toggleClass("open");
    $(".page-fade").fadeToggle("300");
    $(".nav").toggleClass("not-fixed");
  });
});



$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    var wh = $(window).height()/2;
    if (scroll >= wh) {
        $(".nav").addClass("darken");
        $(".dots-nav-container").addClass("dark-dots");
    } else {
        $(".nav").removeClass("darken");
        $(".dots-nav-container").removeClass("dark-dots");
    }
});


$(document).ready(function(){
    $("a[href='#top']").click(function() {
         $("html, body").animate({ scrollTop: 0 }, "slow");
         return false;
    });
});
