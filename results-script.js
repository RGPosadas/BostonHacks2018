$( document ).ready(function() {
    console.log( "ready!" );
});

var val = window.location.search;

var xhttp = new XMLHttpRequest();
xhttp.open("GET", "http://api.giphy.com/v1/gifs/search?q=" + val.split(' ').join('+') + "&api_key=NhEPr6DtewNp95j4pv4TFaMbE3lHqqs9&limit=1", true);

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        document.getElementById("first").innerHTML = "<img src='" + myArr.data[0].images.original.url +"'>";
        // We need an if else function here to show if we approve or not
        document.getElementById("second").innerHTML = "<img src='No-Nos-300x300.png'>";
        //IF the mask is over the GIF, let the user decide if they want to close the mask by clicking on it
        document.getElementById("second").onclick = function() {
            // if (document.getElementById("second").innerHTML == "<img src='No-Nos-300x300.png'>") {
                document.getElementById("second").innerHTML = "<img src='" + myArr.data[0].images.original.url +"'>";
            // }
            // else {
                // document.getElementById("second").innerHTML = "<img src='No-Nos-300x300.png'>";
            // }
        }
    }
};

xhttp.send();