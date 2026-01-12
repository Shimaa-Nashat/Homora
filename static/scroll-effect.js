const hidden = document.querySelectorAll('.hidden');

window.addEventListener('scroll', () => {
    const trigger = window.innerHeight * 0.8;
    hidden.forEach(el => {
        const elTop = el.getBoundingClientRect().top;
        if (elTop < trigger) {
            el.classList.add('show');
        }
    });
});
