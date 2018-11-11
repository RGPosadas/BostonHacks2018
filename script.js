
function loadGIF() {
    var val = document.getElementById("searchtext").value

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://api.giphy.com/v1/gifs/search?q=" + val.split(' ').join('+') + "&api_key=NhEPr6DtewNp95j4pv4TFaMbE3lHqqs9&limit=1", true);

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

            var myArr = JSON.parse(this.responseText);
            document.getElementById("inner").innerHTML = "<img src='" + myArr.data[0].images.original.url +"'>";
            // for (x in myArr.data) {
            //     document.getElementById("inner").innerHTML += "<img src='" + myArr.data[x].images.original.url +"'>";
            // }
        }
    };

    xhttp.send();
}               

function move(){
    var hide = document.getElementById("searchtext")
    

}