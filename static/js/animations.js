/**
 * Cinematic Animations & Interactive UX for Personal Portfolio
 * - Page Load Entrance: Aperture zoom & focus
 * - Hero 3D Parallax & Viewfinder Mouse Tracking
 * - Specular 3D Card Tilt for Projects & Experience
 * - JavaScript-driven Animated Hamburger Navigation
 * - Academic Journey Milestone Animation for Education
 * - Dynamic Staggered Reveal for AJAX Cards
 * - Full prefers-reduced-motion Accessibility Support
 */

(function () {
    'use strict';

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ========================================================
    // 1. Page Load Entrance: Camera Lens Focus & Zoom
    // ========================================================
    function initPageEntrance() {
        if (prefersReducedMotion) {
            document.body.classList.add('page-loaded');
            return;
        }
        requestAnimationFrame(() => {
            document.body.classList.add('page-loaded');
        });
    }

    // ========================================================
    // 2. Hero Profile Interactive 3D Parallax & Viewfinder
    // ========================================================
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

    // ========================================================
    // 3. 3D Interactive Card Tilt (Projects & Experience)
    // ========================================================
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

                    const rotateX = ((y - centerY) / centerY) * -5;
                    const rotateY = ((x - centerX) / centerX) * 5;

                    card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-4px)`;
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

    // ========================================================
    // 4. JavaScript-driven Animated Hamburger Navigation
    // ========================================================
    function initMobileNav() {
        const toggleBtn = document.getElementById('nav-toggle');
        const siteNav = document.getElementById('site-nav');
        const header = document.querySelector('.site-header');

        if (!toggleBtn || !siteNav) return;

        function closeNav() {
            toggleBtn.classList.remove('is-active');
            toggleBtn.setAttribute('aria-expanded', 'false');
            toggleBtn.setAttribute('aria-label', 'Buka menu navigasi');
            siteNav.classList.remove('is-open');
            document.body.classList.remove('nav-open');
            if (header) header.classList.remove('nav-open');
        }

        function openNav() {
            toggleBtn.classList.add('is-active');
            toggleBtn.setAttribute('aria-expanded', 'true');
            toggleBtn.setAttribute('aria-label', 'Tutup menu navigasi');
            siteNav.classList.add('is-open');
            document.body.classList.add('nav-open');
            if (header) header.classList.add('nav-open');
        }

        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = toggleBtn.classList.contains('is-active');
            if (isOpen) {
                closeNav();
            } else {
                openNav();
            }
        });

        // Close on clicking nav links
        siteNav.addEventListener('click', (e) => {
            if (e.target.tagName === 'A') {
                closeNav();
            }
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (toggleBtn.classList.contains('is-active') && !header.contains(e.target)) {
                closeNav();
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && toggleBtn.classList.contains('is-active')) {
                closeNav();
                toggleBtn.focus();
            }
        });

        // Reset if window resizes to desktop width
        window.addEventListener('resize', () => {
            if (window.innerWidth > 768 && toggleBtn.classList.contains('is-active')) {
                closeNav();
            }
        });
    }

    // ========================================================
    // 5. Academic Journey Animation (Education Timeline)
    // ========================================================
    function initEducationJourney() {
        const timeline = document.getElementById('edu-timeline');
        if (!timeline) return;

        const frames = Array.from(timeline.querySelectorAll('.edu-frame'));
        if (frames.length === 0) return;

        if (prefersReducedMotion) {
            frames.forEach(frame => frame.classList.add('journey-active'));
            return;
        }

        // Staggered chronological unveiling
        frames.forEach((frame, index) => {
            frame.style.setProperty('--journey-index', index);

            // Mark current / latest university milestone at the top
            if (index === 0 && frame.classList.contains('is-current')) {
                frame.classList.add('milestone-top');
            }
        });

        // IntersectionObserver to sequentially activate journey milestones as user scrolls
        const journeyObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const idx = Number(target.style.getPropertyValue('--journey-index') || 0);

                    setTimeout(() => {
                        target.classList.add('journey-active');
                    }, idx * 140);

                    observer.unobserve(target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        });

        frames.forEach(frame => {
            if (!frame.classList.contains('journey-active')) {
                journeyObserver.observe(frame);
            }
        });

        // Interactive connector lighting when hovering past milestones
        frames.forEach(frame => {
            frame.addEventListener('mouseenter', () => {
                frame.classList.add('is-journey-focus');
                const connector = frame.querySelector('.edu-connector');
                if (connector) connector.classList.add('connector-glow');
            });
            frame.addEventListener('mouseleave', () => {
                frame.classList.remove('is-journey-focus');
                const connector = frame.querySelector('.edu-connector');
                if (connector) connector.classList.remove('connector-glow');
            });
        });
    }

    // ========================================================
    // 6. Staggered Scroll & AJAX Reveal
    // ========================================================
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

        // Watch dynamic AJAX containers
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

        // Watch education timeline mutations for dynamic AJAX reload
        const eduTimeline = document.getElementById('edu-timeline');
        if (eduTimeline) {
            const eduMutationObs = new MutationObserver(() => {
                initEducationJourney();
            });
            eduMutationObs.observe(eduTimeline, { childList: true });
        }
    }

    // ========================================================
    // Initialization Bootstrap
    // ========================================================
    function bootstrap() {
        initPageEntrance();
        initHeroParallax();
        initInteractiveTilt();
        initMobileNav();
        initEducationJourney();
        initScrollReveal();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bootstrap);
    } else {
        bootstrap();
    }

    // Listen to custom event when AJAX finishes loading education data
    document.addEventListener('educationLoaded', () => {
        initEducationJourney();
    });
})();
