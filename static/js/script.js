'use strict'

// BackToTop button

const navBar = document.querySelector('.navbar'),
    buttonToTop = document.getElementById('scroll-up'),
    yPoint = 200

window.addEventListener('scroll', () => {
    if (pageYOffset < yPoint) {
        navBar.classList.remove('navbar-alt')

        buttonToTop.hidden = true
        buttonToTop.style.opacity = '0'
    } else {
        navBar.classList.add('navbar-alt')

        buttonToTop.hidden = false
        buttonToTop.style.opacity = '.6'
    }
})

buttonToTop.addEventListener('mouseover', () => {
    if (pageYOffset >= yPoint) {
        buttonToTop.style.cursor = 'pointer'
        buttonToTop.style.opacity = '1'
    }
})
buttonToTop.addEventListener('mouseout', () => {
    buttonToTop.style.cursor = ''
    if (pageYOffset >= yPoint) { buttonToTop.style.opacity = '.6' }
})

buttonToTop.addEventListener('click', () => {
    window.scrollTo({ pageXOffset, top: 0, behavior: 'smooth' })
})

// End BackToTop button

// BurgerMenu

const menuWrapper = document.querySelector('.nav-on-header'),
    menu = document.querySelector('.ti-menu')

menu.addEventListener('click', (event) => {
    event.preventDefault()

    if (menu.classList.contains('ti-menu')) {
        menu.classList.remove('ti-menu')
        menu.classList.add('ti-close')
        menuWrapper.classList.add('offcanvas-show')
    } else {
        menuWrapper.classList.remove('offcanvas-show')
        menu.classList.remove('ti-close')
        menu.classList.add('ti-menu')
    }
})

// End BurgerMenu
