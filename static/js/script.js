'use strict'

const navBar = document.querySelector('.navbar'),
    buttonToTop = document.getElementById('scroll-up')

window.addEventListener('scroll', () => {
    if (pageYOffset < 200) {
        navBar.classList.remove('navbar-alt')

        buttonToTop.hidden = true
        buttonToTop.style.opacity = '0'
    } else {
        navBar.classList.add('navbar-alt')

        buttonToTop.hidden = false
        buttonToTop.style.opacity = '.6'
    }
})