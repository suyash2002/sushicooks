const menuOpen = document.querySelector('.menu-open');
const menuClose = document.querySelector('.menu-close');
const nav = document.querySelector('nav');
const links = document.querySelectorAll('.nav-item');

menuOpen.addEventListener('click', () => {
    nav.classList.add('openNav');
    menuOpen.classList.add('menuRotate');
    menuClose.classList.remove('menuRotate');
    links.forEach(link => {
        link.classList.add('links-animation');
    });
})

menuClose.addEventListener('click', () => {
    nav.classList.remove('openNav');
    menuOpen.classList.remove('menuRotate');
    menuClose.classList.add('menuRotate');
    links.forEach(link => {
        link.classList.remove('links-animation');
    });
});