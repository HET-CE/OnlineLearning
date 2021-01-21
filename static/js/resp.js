burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
navList = document.querySelector('.navlist')
rightnav = document.querySelector('.rightnav')



burger.addEventListener('click',()=>{
    rightnav.classList.toggle('visible-resp');
    navList.classList.toggle('visible-resp');
    navbar.classList.toggle('navh-resp');
})




