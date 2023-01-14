/*****************************************
Agenda List/Grid View & Day/Night Toggle
******************************************/
var checkbox = document.getElementById("ChangeMode");
 
if (sessionStorage.getItem("mode") == "dark") {
  darkmode();
} else {
  lightmode();
}

checkbox.addEventListener("change", function() {
  if (checkbox.checked) {
    darkmode();
  } else {
    lightmode();
  }
});

function darkmode() {
  document.body.classList.add("dark");
  checkbox.checked = true;
  sessionStorage.setItem("mode", "dark");
  document.cookie = "mode=dark; expires=Thu, 18 Dec 2023 12:00:00 UTC";
}

function lightmode() {
  document.body.classList.remove("dark");
  checkbox.checked = false;
  sessionStorage.setItem("mode", "light");
  document.cookie = "mode=light; expires=Thu, 18 Dec 2023 12:00:00 UTC";
}

/***********************
Scroll-To-Top Function
************************/
//Get the button:
mybutton = document.getElementById("toTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
    mybutton.style.transition = "all .5s ease-in-out";
  } else {
    mybutton.style.display = "none";
  }
}

$("#toTop").click(function() {
  $("html, body").animate({ scrollTop: 0 }, "slow");
  return false;
});

/*************************
Avatar Upload Image Field
*************************/
$(document).ready(function() {

    var readURL = function(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#profile-upload').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#id_image").on('change', function(){
        readURL(this);
    });

    $(".upload-button").on('click', function() {
       $("#id_image").click();
    });
});

/*********************
Input Label Transform
**********************/
$('.form').find('input, textarea').on('keyup blur focus input', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('act highlight');
        } else {
          label.addClass('act highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('act highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }
    else if (e.type === 'input') {
      if ( $this.val() === '' ) {
        label.removeClass('act highlight');
      }else if ( $this.val() !== '' ) {
        label.addClass('act highlight');
      }
    }

});

/**********************
Alert Messages Timeout
***********************/

window.setTimeout(function() {
  $(".alert").slideUp(500, function() {
    $(this).remove();
  });
}, 3000);

/**********
Copyright
**********/
function updateCopyright() {
  var d = new Date();
  document.getElementById('copyrightYear').innerHTML = d.getFullYear();
}
