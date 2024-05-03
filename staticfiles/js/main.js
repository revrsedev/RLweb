"use strict";

$(document).ready(function () {
  //preloader
  $(".preloader")
    .delay(300)
    .animate(
      {
        opacity: "0",
      },
      300,
      function () {
        $(".preloader").css("display", "none");
      }
    );

  // Initialize the last scroll position to 0
  var lastScrollTop = 0;

  // Attach a scroll event listener to the window object
  $(window).on("scroll", function () {
    // Get the current scroll position
    var st = $(this).scrollTop();

    // Get a reference to the navbar element
    var navBar = $(".main-navbar");

    // Determine the scroll direction and update the navbar classes accordingly
    if (st < lastScrollTop) {
      navBar.removeClass("navbar-active");
      navBar.addClass("navbar-scroll-bg");
    } else {
      navBar.addClass("navbar-active");
      navBar.removeClass("navbar-scroll-bg");
    }

    // Update the last scroll position
    lastScrollTop = st;

    // If the scroll position is less than 50 pixels, remove the background class
    if ($(this).scrollTop() < 50) {
      navBar.removeClass("navbar-scroll-bg");
    }

    if ($(this).scrollTop() > 250) {
      $(".scroll-top").addClass("scroll-top-active");
    } else {
      $(".scroll-top").removeClass("scroll-top-active");
    }
  });
});

$(".menu-item-has-children").append(
  '<button class="menu-item-button" type="button">+</button>'
);

$(".theme-change-button").on("click", function () {
  $(".theme-change").toggleClass("active");
});

$(".menu-item-button").on("click", function () {
  $(this).siblings(".sub-menu").slideToggle();

  console.log("ami achi");
});

var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

$(window).on("scroll", function () {
  if ($(this).scrollTop() > 200) {
    $(".back-to-top").fadeIn(200);
  } else {
    $(".back-to-top").fadeOut(200);
  }
});

$(".back-to-top").on("click", function (event) {
  event.preventDefault();
  $("html, body").animate({ scrollTop: 0 }, 300);
});

maudio({
  obj: "audio",
  fastStep: 10,
});

$(".bookmark-icon").on("click", function () {
  $(this).toggleClass("active");
});

new WOW().init();

// faq js
$(".faq-single-header").each(function () {
  $(this).on("click", function () {
    $(this).siblings(".faq-single-body").slideToggle();
    $(this).parent(".faq-single").toggleClass("active");
  });
});

// podcast-slider
$(".podcast-slider").slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1400,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// podcast-slider-two
$(".podcast-slider-two").slick({
  infinite: true,
  rows: 2,
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// rj-sldier
$(".rj-sldier").slick({
  infinite: true,
  rows: 2,
  slidesToShow: 4,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// sponsor-slider
$(".sponsor-slider").slick({
  infinite: true,
  slidesToShow: 6,
  slidesToScroll: 1,
  dots: false,
  arrows: false,
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 5,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 4,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
      },
    },
  ],
});

// testimonial-slider
$(".testimonial-slider").slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1400,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

$(".testimonial-slider-two").slick({
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
});

// testimonial-slider
$(".testimonial-slider-three").slick({
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// popular-show-slider
$(".popular-show-slider").slick({
  infinite: true,
  slidesToShow: 4,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow: $(".popular-show-prev"),
  nextArrow: $(".popular-show-next"),
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 576,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// popular-show-slider
$(".multi-radio-station-slider").slick({
  infinite: false,
  slidesToShow: 4,
  slidesToScroll: 1,
  rows: 2,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      },
    },
  ],
});

// previous-show-slider
$(".previous-show-slider").slick({
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  dots: false,
  arrows: true,
  prevArrow:
    '<button type="button" class="prev"><i class="fas fa-chevron-left"></i></button>',
  nextArrow:
    '<button type="button" class="next"><i class="fas fa-chevron-right"></i></button>',
  autoplay: false,
  cssEase: "cubic-bezier(0.645, 0.045, 0.355, 1.000)",
  speed: 1000,
  autoplaySpeed: 500,
  centerMode: true,
  centerPadding: "308px",
  responsive: [
    {
      breakpoint: 1700,
      settings: {
        centerPadding: "200px",
      },
    },
    {
      breakpoint: 1400,
      settings: {
        centerPadding: "100px",
      },
    },
    {
      breakpoint: 1200,
      settings: {
        centerPadding: "50px",
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        centerPadding: "50px",
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        centerPadding: "40px",
      },
    },
  ],
});
