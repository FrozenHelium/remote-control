// volume
document.getElementById("vol-increase").onclick = function() { makeRequest("/volume/vol_increase"); };
document.getElementById("vol-decrease").onclick = function() { makeRequest("/volume/vol_decrease"); };


// keyboard
document.getElementById("left").onclick =   function() { makeRequest("/keyboard/tap_left_key");   };
document.getElementById("right").onclick =  function() { makeRequest("/keyboard/tap_right_key");  };
document.getElementById("up").onclick =     function() { makeRequest("/keyboard/tap_up_key");     };
document.getElementById("down").onclick =   function() { makeRequest("/keyboard/tap_down_key");   };
document.getElementById("space").onclick =  function() { makeRequest("/keyboard/tap_space_key");  };
document.getElementById("return").onclick = function() { makeRequest("/keyboard/tap_return_key");  };

document.getElementById("ctrl").onchange =  function() { if(this.checked){ makeRequest("/keyboard/press_ctrl_key");}  else{ makeRequest("/keyboard/release_ctrl_key");} };
document.getElementById("shift").onchange = function() { if(this.checked){ makeRequest("/keyboard/press_shift_key");} else{ makeRequest("/keyboard/release_shift_key");}};
document.getElementById("alt").onchange =   function() { if(this.checked){ makeRequest("/keyboard/press_alt_key");}   else{ makeRequest("/keyboard/release_alt_key");}  };
document.getElementById("win").onchange =   function() { if(this.checked){ makeRequest("/keyboard/press_win_key");}   else{ makeRequest("/keyboard/release_win_key");}  };

document.getElementById("vlc-play-pause").onclick = function() { makeRequest("/keyboard/tap_space_key"); };
document.getElementById("vlc-seek-backward-low").onclick = function() {
    makeRequest("/keyboard/press_shift_key");
    makeRequest("/keyboard/tap_left_key");
    makeRequest("/keyboard/release_shift_key");
};
document.getElementById("vlc-seek-forward-low").onclick = function() {
    makeRequest("/keyboard/press_shift_key");
    makeRequest("/keyboard/tap_right_key");
    makeRequest("/keyboard/release_shift_key");
};
document.getElementById("vlc-seek-backward-medium").onclick = function() {
    makeRequest("/keyboard/press_alt_key");
    makeRequest("/keyboard/tap_left_key");
    makeRequest("/keyboard/release_alt_key");
};
document.getElementById("vlc-seek-forward-medium").onclick = function() {
    makeRequest("/keyboard/press_alt_key");
    makeRequest("/keyboard/tap_right_key");
    makeRequest("/keyboard/release_alt_key");
};
document.getElementById("vlc-seek-backward-high").onclick = function() {
    makeRequest("/keyboard/press_ctrl_key");
    makeRequest("/keyboard/tap_left_key");
    makeRequest("/keyboard/release_ctrl_key");
};
document.getElementById("vlc-seek-forward-high").onclick = function() {
    makeRequest("/keyboard/press_ctrl_key");
    makeRequest("/keyboard/tap_right_key");
    makeRequest("/keyboard/release_ctrl_key");
};
document.getElementById("vlc-volume-inc").onclick = function() {
    makeRequest("/keyboard/press_ctrl_key");
    makeRequest("/keyboard/tap_up_key");
    makeRequest("/keyboard/release_ctrl_key");
};
document.getElementById("vlc-volume-dec").onclick = function() {
    makeRequest("/keyboard/press_ctrl_key");
    makeRequest("/keyboard/tap_down_key");
    makeRequest("/keyboard/release_ctrl_key");
};
document.getElementById("vlc-subtitles").onclick = function() {
    makeRequest("/keyboard/tap_character/v/");
};


function onCharacterInput(event) {
    if (event.which == 8) {   // backspace
        makeRequest("/keyboard/tap_backspace_key");
        return;
    }
    if (event.which == 10 || event.which == 13) {   // enter
        makeRequest("/keyboard/tap_return_key");
        return;
    }
    var el = document.getElementById("character");
    makeRequest("/keyboard/tap_character/" + el.value.substr(0,1) + "/");
    el.value = "";
};


//mouse
var pointer = document.getElementById("pointer");
var tracking = false;
var pointer_bounds = pointer.getBoundingClientRect();
var prev_cx = -1;
var prev_cy = -1;

function startTrack(){
    tracking = true;
}
function stopTrack(){
    tracking = false;
    prev_cx = -1;
    prev_cy = -1;
}
function traceMovement(cx, cy){
    var dx = 0;
    var dy = 0;

    if(prev_cx != -1 && prev_cy != -1){
        dx = (cx-prev_cx)*3;
        dy = (cy-prev_cy)*3;
    }

    prev_cx = cx;
    prev_cy = cy;

    makeRequest("/mouse/offset/"+dx+"/"+dy+"/");
}

// mouse input
// pointer.onmousedown = startTrack;
// pointer.onmouseup = stopTrack;
// pointer.onmousemove = function(e){
//     if(tracking){
//         e.preventDefault();
//         e.stopPropagation();
//         traceMovement(parseInt(e.clientX-pointer_bounds.left), parseInt(e.clientY-pointer_bounds.top));
//     }
// }

// touchinput
pointer.addEventListener("touchstart", startTrack, false);
pointer.addEventListener("touchend", stopTrack, false);
pointer.addEventListener("touchmove", function(e){
    if(tracking){
        e.preventDefault();
        e.stopPropagation();
        traceMovement(parseInt(e.touches[0].clientX), parseInt(e.touches[0].clientY));
    }
}, false);
pointer.onclick = function(){ makeRequest("/mouse/left_click"); }

document.getElementById("mouse-left-click").onclick = function() { makeRequest("/mouse/left_click"); };
document.getElementById("mouse-right-click").onclick = function() { makeRequest("/mouse/right_click"); };


// Make ajax request
function makeRequest(url) {
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
        alert('Failed to create an XMLHTTP instance');
        return false;
    }
    httpRequest.onreadystatechange = function(){
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                var response = JSON.parse(httpRequest.responseText);
                //document.getElementById("response").innerHTML = response.msg;
            } else {
                //document.getElementById("response").innerHTML = 'Oops! something went wrong.';
            }
        }
    };
    httpRequest.open('GET', url, false);
    httpRequest.send();
}
