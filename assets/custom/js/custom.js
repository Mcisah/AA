/**
 * Created by michael on 3/2/17.
 */

function hilda(){
    document.getElementById('co').innerHTML = "****";
}

function p_p(){
    if (screen.width >= 779)
        if (document.getElementById('p_p_image').style.height == "50px" && document.getElementById('p_p_image').style.width == "50px") {
            document.getElementById('p_p_image').style.height = "30px";
            document.getElementById('p_p_image').style.width = "30px";
        }else{
            document.getElementById('p_p_image').style.height = "50px";
            document.getElementById('p_p_image').style.width = "50px";
        }else{
        // do nothing
    }
}


function riri() {
    location.reload();
}