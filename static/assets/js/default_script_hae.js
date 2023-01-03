toggleNav = (navVisible) => {
    nav = document.querySelector("#nav");
    if(!navVisible) {
        defaultStyle = nav.getAttribute("style");
        nav.style.transform = `translate(200px)`;
    }else {
        defaultStyle = nav.getAttribute("style");
        nav.style.transform = `translate(-200px)`;
    }
}