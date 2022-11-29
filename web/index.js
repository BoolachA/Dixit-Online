eel.expose(showScreen);
function showScreen(screenName){
    document.body.childNodes.forEach(child => {
        try {
            if (child.id == screenName) {
                child.classList.remove("hidden")
            } else {
                child.classList.add("hidden")
            }
        } catch (e) {}
    });
    if(screenName=="MenuB"){
        eel.configHost("shutdown")
        getHostIp()
    }
}

function connect(){
    ip = document.getElementById('submitForm').value
    eel.startClient(ip)
}

async function getHostIp(){
    let ip = await eel.getHostIp()();
    document.getElementById("ipAnnouce").innerHTML = "IP de la sala: " + ip
}

function destoyBtn(){
    document.getElementById("aviso").remove()
}

function toggleFullScreen() {
    var doc = window.document;
    var docEl = doc.documentElement;
 
    var requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
    var cancelFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;
 
    if(!doc.fullscreenElement && !doc.mozFullScreenElement && !doc.webkitFullscreenElement && !doc.msFullscreenElement) {
        requestFullScreen.call(docEl);
    }
    else {
        cancelFullScreen.call(doc);
    }
 }
 


setTimeout(destoyBtn, 10000)