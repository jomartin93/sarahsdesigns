---
layout: default
title: Home
---
<script>
  document.addEventListener('input', e => {
    if (e.target.tagName.toLowerCase() !== 'textarea') return;
    const el = e.target;
    const scrollY = window.scrollY; // remember scroll position
    el.style.height = 'auto';
    el.style.height = el.scrollHeight + 'px';
    window.scrollTo(window.scrollX, scrollY); // restore scroll position
  });
</script>
<div class="card">
  <h1>Welcome to Sarah's Designs</h1>
  <p>We're a St. Louis based floral studio specializing in custom arrangements and event florals. Whether you're looking to brighten your property or create a memorable event, we're here to help bring your vision to life (see our past successes in our <a href="/gallery/">gallery</a>). If you're wanting a consultation, use our services, or just have questions, take a few seconds to fill out our contact form below, we'll be in touch shortly!</p>
</div>
<div class="card">
  <h1>Contact Us</h1>
  <form method="POST" action="https://formspree.io/f/xdkpbwlz">
    <label for="name">Name</label><br>
    <input id="name" name="name" required style="width:100%;padding:.6rem;margin:.3rem 0 1rem;"><br>
    <label for="email">Email</label><br>
    <input id="email" type="email" name="email" required style="width:100%;padding:.6rem;margin:.3rem 0 1rem;"><br>
    <label for="message">Message</label><br>
    <textarea id="message" name="message" rows="6" required style="width:100%;padding:.6rem;margin:.3rem 0 1rem;"></textarea><br>
    <button type="submit" style="padding:.6rem 1rem;border:0;margin:.3rem 0.1rem;">Send</button>
  </form>
</div>