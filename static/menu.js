document.addEventListener('DOMContentLoaded', () => {

    const mobile = () => {
  
      const hamburgerOpen = document.querySelector('.header__hamburger_open')
      const hamburgerClose = document.querySelector('.mobile__hamburger_close')
      const mobile = document.querySelector('.mobile')
      const overlay = document.querySelector('.overlay')
  
      const openMobile = () => { // объявим функцию открытия мобильной навигации
        mobile.classList.add('mobile_active')
        overlay.classList.add('overlay_active')
      }
  
      const closeMobile = () => { // объявим функцию закрытия мобильной навигации
        mobile.classList.remove('mobile_active')
        overlay.classList.remove('overlay_active')
      }
  
      hamburgerOpen.addEventListener('click', () => {
        openMobile() // вызываем функцию открытия мобильной навигации
      })
  
      hamburgerClose.addEventListener('click', () => {
        closeMobile() // вызываем функцию закрытия мобильной навигации
      })
  
      window.addEventListener('resize', () => {
        if (window.innerWidth >= 768 ) {
          closeMobile() // вызываем функцию закрытия мобильной навигации
        }
      })
  
      overlay.addEventListener('click', () => {
        closeMobile() // вызываем функцию закрытия мобильной навигации
      })
  
    }
  
    mobile()
  
  })