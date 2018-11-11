
function UserAction() {
    const Http = new XMLHttpRequest();

    const url='api.giphy.com/v1/gifs/search';

    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange=(e)=>{
        console.log(Http.responseText)
    }
}