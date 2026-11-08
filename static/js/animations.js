/**
 * Cinematic Animations for Personal Portfolio
 * - Page Entrance: Aperture focus & subtle zoom-in
 * - Hero Photo: Interactive 3D Viewfinder mouse tracking & parallax
 * - 3D Interactive Card Tilt with specular light (Projects & Experience)
 * - Dynamic Staggered Reveal for AJAX cards
 * - Respects prefers-reduced-motion for accessibility
 */

(function () {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // 1. Page Load Entrance (Cinematic Focus & Zoom)
    function initPageEntrance() {
        if (prefersReducedMotion) {
            document.body.classList.add('page-loaded');
            return;
        }
        requestAnimationFrame(() => {
            document.body.classList.add('page-loaded');
        });
    }

    // 2. Hero Profile Interactive 3D Parallax & Viewfinder Tracking
    function initHeroParallax() {
        if (prefersReducedMotion || window.innerWidth < 768) return;

        const heroPhoto = document.querySelector('.hero-photo');
        const heroSection = document.querySelector('.hero');
        if (!heroPhoto || !heroSection) return;

        let ticking = false;

        heroSection.addEventListener('mousemove', (e) => {
            if (ticking) return;
            ticking = true;

            requestAnimationFrame(() => {
                const rect = heroPhoto.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                const deltaX = (e.clientX - centerX) / (window.innerWidth / 2);
                const deltaY = (e.clientY - centerY) / (window.innerHeight / 2);

                const rotateX = -deltaY * 12;
                const rotateY = deltaX * 12;
                const transX = deltaX * 8;
                const transY = deltaY * 8;

                heroPhoto.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translate3d(${transX.toFixed(1)}px, ${transY.toFixed(1)}px, 0)`;
                ticking = false;
            });
        });

        heroSection.addEventListener('mouseleave', () => {
            heroPhoto.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translate3d(0, 0, 0)';
            heroPhoto.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        });

        heroSection.addEventListener('mouseenter', () => {
            heroPhoto.style.transition = 'transform 0.1s ease-out';
        });
    }

    // 3. Interactive 3D Polaroid Tilt (Khusus Project & Experience Card)
    function initInteractiveTilt() {
        if (prefersReducedMotion || window.innerWidth < 768) return;

        let ticking = false;

        document.addEventListener('mousemove', (e) => {
            if (ticking) return;
            ticking = true;

            requestAnimationFrame(() => {
                const card = e.target.closest('.project-card, .experience-card');
                if (card) {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;

                    const rotateX = ((y - centerY) / centerY) * -6;
                    const rotateY = ((x - centerX) / centerX) * 6;

                    card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-5px)`;
                    card.style.setProperty('--mouse-x', `${(x / rect.width) * 100}%`);
                    card.style.setProperty('--mouse-y', `${(y / rect.height) * 100}%`);
                    card.classList.add('is-tilting');
                }
                ticking = false;
            });
        });

        document.addEventListener('mouseout', (e) => {
            const card = e.target.closest('.project-card, .experience-card');
            if (card && (!e.relatedTarget || !card.contains(e.relatedTarget))) {
                card.style.transform = '';
                card.classList.remove('is-tilting');
            }
        });
    }

    // 4. Staggered Scroll & AJAX Reveal
    function initScrollReveal() {
        if (prefersReducedMotion) return;

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach((entry, idx) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('revealed');
                    }, idx * 60);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.08 });

        function observeCards(container) {
            if (!container) return;
            const items = container.querySelectorAll('.project-card, .experience-card');
            items.forEach((item, index) => {
                if (!item.classList.contains('revealed')) {
                    item.classList.add('reveal-item');
                    item.style.setProperty('--stagger-delay', `${index * 50}ms`);
                    observer.observe(item);
                }
            });
        }

        observeCards(document.body);

        const targetContainers = ['grid', 'exp-grid'];
        targetContainers.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                const mutationObs = new MutationObserver(() => {
                    observeCards(el);
                });
                mutationObs.observe(el, { childList: true });
            }
        });
    }

    // Initialize all enhancements on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initPageEntrance();
            initHeroParallax();
            initInteractiveTilt();
            initScrollReveal();
        });
    } else {
        initPageEntrance();
        initHeroParallax();
        initInteractiveTilt();
        initScrollReveal();
    }
})();