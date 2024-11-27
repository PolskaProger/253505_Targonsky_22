class Slider {
    constructor({ container, auto = true, delay = 2, loop = true, navs = true, pags = true, stopMouseHover = true }) {
        this.container = document.querySelector(container);
        this.slides = this.container.querySelectorAll('.slide');
        this.currentSlide = 0;
        this.auto = auto;
        this.delay = delay * 1000;
        this.loop = loop;
        this.stopMouseHover = stopMouseHover;
        this.interval = null;

        this.init();
        if (navs) this.addNavigation();
        if (pags) this.addPagination();
        if (this.auto) this.startAutoRotate();
    }

    init() {
        this.showSlide(this.currentSlide);
        if (this.stopMouseHover) {
            this.container.addEventListener('mouseover', () => clearInterval(this.interval));
            this.container.addEventListener('mouseout', () => this.startAutoRotate());
        }
    }

    showSlide(index) {
        this.slides.forEach(slide => slide.style.display = 'none');
        this.slides[index].style.display = 'block';
        this.updatePagination();
    }

    nextSlide() {
        this.currentSlide = (this.currentSlide + 1) % this.slides.length;
        this.showSlide(this.currentSlide);
    }

    prevSlide() {
        this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
        this.showSlide(this.currentSlide);
    }

    startAutoRotate() {
        this.interval = setInterval(() => this.nextSlide(), this.delay);
    }

    addNavigation() {
        this.container.querySelector('.next').addEventListener('click', () => this.nextSlide());
        this.container.querySelector('.prev').addEventListener('click', () => this.prevSlide());
    }

    addPagination() {
        const pagination = this.container.querySelector('.pagination');
        pagination.innerHTML = '';
        this.slides.forEach((_, i) => {
            const span = document.createElement('span');
            span.textContent = i + 1;
            span.addEventListener('click', () => {
                this.currentSlide = i;
                this.showSlide(i);
            });
            pagination.appendChild(span);
        });
        this.updatePagination();
    }

    updatePagination() {
        const pagination = this.container.querySelectorAll('.pagination span');
        pagination.forEach((span, i) => {
            span.classList.toggle('active', i === this.currentSlide);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Slider({
        container: '.slider-container',
        auto: true,
        delay: 2,
        loop: true,
        navs: true,
        pags: true,
        stopMouseHover: true
    });
});
