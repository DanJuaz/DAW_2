
// Menu activate/desactivate
const mobileButton = document.getElementById('mobile');
//Fixed nav mobile
  window.addEventListener("scroll", function() {
    mobileButton.classList.toggle("active", window.scrollY > 0);
  });
  const mobileMenu = document.getElementById('mobile-menu');
  
  window.addEventListener('resize', updateMobileMenuDisplay);
  function updateMobileMenuDisplay() {
    if (window.innerWidth >= 600) {
        mobileMenu.style.display = "flex";
    } else {
        mobileMenu.style.display = "none";
    }
}
function mobile_menu() {
  const mobileMenu = document.getElementById('mobile-menu');
  
  if (mobileMenu.style.display === "flex") {
      mobileMenu.style.display = "none";
  } else {
      mobileMenu.style.display = "flex";
  }
}
// Fixed nav
const nav = document.querySelector(".header-nav");
  window.addEventListener("scroll", function() {
    nav.classList.toggle("active", window.scrollY > 0);
  });
