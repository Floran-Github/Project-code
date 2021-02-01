function tooglemenu(){
    var menu = document.querySelector('.menutoggle');
    var nav = document.querySelector('.navigation');
    var start = document.querySelector('.main');
    menu.classList.toggle('active');
    nav.classList.toggle('active');
    if(start.classList.contains('active')){
        start.classList.toggle('overlap');
    }
}

function startfun(){
    document.getElementById('about-me').scrollIntoView();
}

function navigation(){
    var menu = document.querySelector('.menutoggle');
    var nav = document.querySelector('.navigation');
    setTimeout(() =>{
    if(menu.classList.contains('active')){
        nav.classList.remove('active');
        menu.classList.remove('active');    
    }
    }, 100);
}
function homefun(){
    navigation();
    document.getElementById('home').scrollIntoView();
}
function aboutme(){
    navigation();
    document.getElementById('about-me').scrollIntoView();
}

function team(){
    navigation();
    document.getElementById('team').scrollIntoView();
}

function contact(){
    navigation();
    document.getElementById('contact').scrollIntoView();
}
