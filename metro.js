document.documentElement.classList.remove('preload');
document.body.classList.remove('preload');
document.body.classList.add('loaded');
const menuToggle = document.getElementById('menu-toggle');
const dropdownMenu = document.getElementById('dropdown-menu');
const backdrop = document.querySelector('.backdrop');
if (menuToggle && dropdownMenu && backdrop) {
    function closeMenu() {
        dropdownMenu.classList.remove('active');
        backdrop.classList.remove('active');
    }
    menuToggle.addEventListener('click', function() {
        dropdownMenu.classList.toggle('active');
        backdrop.classList.toggle('active');
    });
    backdrop.addEventListener('click', closeMenu);
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeMenu();
    });
}
document.addEventListener('click', function(e) {
    const link = e.target.closest('a');
    if (!link) return;
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || link.target === '_blank' || href.startsWith('javascript:')) return;
    if (href === window.location.pathname || href === window.location.href) return;
    e.preventDefault();
    document.getElementById('page-blink').style.opacity = '1';
    setTimeout(function() { window.location = href; }, 260);
});
