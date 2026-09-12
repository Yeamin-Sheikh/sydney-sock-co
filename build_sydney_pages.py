import os

REPO = r"e:\Scripts\GitHub\sydney-sock-co"

SVG_SPRITE = """<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <symbol id="icon-sock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M7 3h7v8l4 4a4 4 0 0 1-5.66 5.66l-5.34-5.34V3z"></path>
    <path d="M7 8h7"></path>
  </symbol>
  <symbol id="icon-heart" viewBox="0 0 24 24" fill="currentColor" stroke="none">
    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
  </symbol>
  <symbol id="icon-kangaroo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M19 4c-.8 0-1.5.5-1.8 1.2L15 10l-4 1-2 5h-4l-2 3h8l2-4 3 2 4-5-2-4 2-2z"></path>
  </symbol>
  <symbol id="icon-leaf" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"></path>
    <path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path>
  </symbol>
  <symbol id="icon-truck" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect x="1" y="3" width="15" height="13"></rect>
    <polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon>
    <circle cx="5.5" cy="18.5" r="2.5"></circle>
    <circle cx="18.5" cy="18.5" r="2.5"></circle>
  </symbol>
  <symbol id="icon-gift" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="20 12 20 22 4 22 4 12"></polyline>
    <rect x="2" y="7" width="20" height="5"></rect>
    <line x1="12" y1="22" x2="12" y2="7"></line>
    <path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path>
    <path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>
  </symbol>
  <symbol id="icon-cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="9" cy="21" r="1"></circle>
    <circle cx="20" cy="21" r="1"></circle>
    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
  </symbol>
  <symbol id="icon-star" viewBox="0 0 24 24" fill="currentColor" stroke="none">
    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
  </symbol>
  <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="20 6 9 17 4 12"></polyline>
  </symbol>
  <symbol id="icon-shield-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
    <polyline points="9 12 11 14 15 10"></polyline>
  </symbol>
  <symbol id="icon-map-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
    <circle cx="12" cy="10" r="3"></circle>
  </symbol>
  <symbol id="icon-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
  </symbol>
  <symbol id="icon-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
    <polyline points="22,6 12,13 2,6"></polyline>
  </symbol>
  <symbol id="icon-refresh" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="23 4 23 10 17 10"></polyline>
    <polyline points="1 20 1 14 7 14"></polyline>
    <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
  </symbol>
  <symbol id="icon-feather" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path>
    <line x1="16" y1="8" x2="2" y2="22"></line>
    <line x1="17.5" y1="15" x2="9" y2="15"></line>
  </symbol>
</svg>"""

def get_header(active_tab="home"):
    return f"""  <!-- Impact Banner -->
  <div class="impact-ribbon">
    <div class="impact-stats">
      <span class="impact-badge">Our Sydney Impact</span>
      <span>184,200+ Pairs of Warm Socks & Meals Donated to Sydney Community Shelters</span>
      <span style="opacity: 0.8;">&bull; 1 Pair Bought = 1 Donated</span>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="container">
      <nav class="navbar">
        <a href="index.html" class="brand-logo">
          <img src="assets/svgs/logo.svg" alt="Sydney Sock Co" height="46">
        </a>
        <ul class="nav-links">
          <li><a href="index.html" class="nav-link {'active' if active_tab == 'home' else ''}">Home</a></li>
          <li><a href="shop.html" class="nav-link {'active' if active_tab == 'shop' else ''}">Shop Range</a></li>
          <li><a href="about.html" class="nav-link {'active' if active_tab == 'about' else ''}">Our Story</a></li>
          <li><a href="subscription.html" class="nav-link {'active' if active_tab == 'subscription' else ''}">Sock Club</a></li>
          <li><a href="care-guide.html" class="nav-link {'active' if active_tab == 'care' else ''}">Care Guide</a></li>
          <li><a href="contact.html" class="nav-link {'active' if active_tab == 'contact' else ''}">Contact & Studio</a></li>
        </ul>
        <div class="nav-actions">
          <select id="currency-select" class="currency-select" title="Change currency">
            <option value="AUD">AUD ($)</option>
            <option value="USD">USD ($)</option>
            <option value="EUR">EUR (&euro;)</option>
            <option value="GBP">GBP (&pound;)</option>
          </select>
          <button id="cart-trigger" class="cart-btn" title="View Cart">
            <svg class="icon" style="width:20px;height:20px;"><use href="#icon-cart"></use></svg>
            <span id="cart-badge" class="cart-badge">0</span>
          </button>
        </div>
      </nav>
    </div>
  </header>"""

def get_footer():
    return """  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <img src="assets/svgs/logo.svg" alt="Sydney Sock Co" height="42" style="margin-bottom: 1.25rem;">
          <p style="font-size: 0.9rem; line-height: 1.7; max-width: 320px;">
            Ethically knit socks crafted from fine Australian Merino wool and organic bamboo. Proudly rooted in Surry Hills, Sydney NSW.
          </p>
          <div style="margin-top: 1rem; display: flex; gap: 0.75rem;">
            <span style="font-size:0.8rem; background: #042F2E; color: #5EEAD4; padding: 4px 10px; border-radius: 4px; font-weight:700;">Surry Hills, NSW</span>
            <span style="font-size:0.8rem; background: #042F2E; color: #5EEAD4; padding: 4px 10px; border-radius: 4px; font-weight:700;">100% Carbon Neutral</span>
          </div>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <ul class="footer-links">
            <li><a href="shop.html">The Sydney Heritage Range</a></li>
            <li><a href="about.html">Our Ethical Wool Sourcing</a></li>
            <li><a href="subscription.html">Monthly Sock Subscription</a></li>
            <li><a href="care-guide.html">Merino Care & Wash Guide</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Giving Mission</h4>
          <ul class="footer-links">
            <li><a href="about.html#impact">Sydney Shelter Partnership</a></li>
            <li><a href="about.html#merino">Non-Mulesed Australian Merino</a></li>
            <li><a href="about.html#sustainability">Compostable Packaging</a></li>
            <li><a href="subscription.html">Monthly Impact Box Club</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Sydney Store & Studio</h4>
          <ul class="footer-links">
            <li><span style="font-size:0.85rem;">42 Crown St, Surry Hills NSW 2010</span></li>
            <li><span style="font-size:0.85rem;">Mon - Sat: 9:30 AM &ndash; 5:30 PM</span></li>
            <li><span style="font-size:0.85rem;">Email: hello@sydneysockco.com.au</span></li>
            <li><span style="font-size:0.85rem;">ABN: 48 620 914 832</span></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; 2026 Sydney Sock Co. All rights reserved. Made for Australian feet.</div>
        <div>Free express shipping across Australia on all orders over $60 AUD.</div>
      </div>
    </div>
  </footer>

  <!-- Slide-over Cart Drawer -->
  <div id="cart-overlay" class="cart-overlay"></div>
  <aside id="cart-drawer" class="cart-drawer">
    <div class="cart-shipping-bar">
      <div id="shipping-notice">Add <strong>$60.00 AUD</strong> more for Free Shipping!</div>
      <div class="progress-track">
        <div id="shipping-progress-bar" class="progress-fill" style="width: 0%;"></div>
      </div>
    </div>

    <div class="cart-header">
      <h3 style="font-size: 1.15rem; font-weight: 800;">Your Sock Drawer</h3>
      <button id="close-cart-btn" style="border:none; background:none; font-size:1.5rem; cursor:pointer;">&times;</button>
    </div>

    <div id="cart-items-list" class="cart-items"></div>

    <div class="cart-footer">
      <div style="background: #F0FDFA; border: 1px solid #99F6E4; border-radius: 8px; padding: 0.75rem; margin-bottom: 1rem; font-size: 0.85rem; color: #0F766E; display: flex; align-items: center; gap: 0.5rem;">
        <svg class="icon" style="color: #F43F5E; width:16px; height:16px;"><use href="#icon-heart"></use></svg>
        <span>This order donates <strong id="impact-count">0</strong> items to Sydney homeless missions!</span>
      </div>

      <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.9rem; color: var(--text-muted);">
        <span>Subtotal</span>
        <span id="cart-subtotal">$0.00 AUD</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 1.15rem; font-weight: 800; color: var(--text-main); margin-bottom: 1.25rem;">
        <span>Total</span>
        <span id="cart-total">$0.00 AUD</span>
      </div>
      <button id="checkout-btn" class="btn btn-teal" style="width: 100%;">
        Proceed to Checkout
      </button>
    </div>
  </aside>

  <!-- Modal Overlay -->
  <div id="modal-overlay" class="modal-overlay"></div>

  <!-- Size Guide Modal -->
  <div id="size-modal" class="modal-box">
    <button class="modal-close">&times;</button>
    <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem;">Sydney Sock Co Size Guide</h3>
    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">Find your perfect fit across Australian, US, UK, and European standards.</p>
    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;">
      <thead>
        <tr style="border-bottom: 2px solid var(--border-color); background: var(--bg-subtle);">
          <th style="padding: 0.75rem;">Size</th>
          <th style="padding: 0.75rem;">AU / UK</th>
          <th style="padding: 0.75rem;">US Men</th>
          <th style="padding: 0.75rem;">US Women</th>
          <th style="padding: 0.75rem;">EU</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.75rem; font-weight: 700;">S / M</td>
          <td style="padding: 0.75rem;">4 &ndash; 8</td>
          <td style="padding: 0.75rem;">5 &ndash; 8.5</td>
          <td style="padding: 0.75rem;">6 &ndash; 9.5</td>
          <td style="padding: 0.75rem;">36 &ndash; 41</td>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.75rem; font-weight: 700;">M / L</td>
          <td style="padding: 0.75rem;">8 &ndash; 11.5</td>
          <td style="padding: 0.75rem;">9 &ndash; 12.5</td>
          <td style="padding: 0.75rem;">10 &ndash; 13.5</td>
          <td style="padding: 0.75rem;">42 &ndash; 46</td>
        </tr>
        <tr>
          <td style="padding: 0.75rem; font-weight: 700;">XL</td>
          <td style="padding: 0.75rem;">12 &ndash; 15</td>
          <td style="padding: 0.75rem;">13 &ndash; 16</td>
          <td style="padding: 0.75rem;">14+</td>
          <td style="padding: 0.75rem;">47 &ndash; 50</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Checkout Modal -->
  <div id="checkout-modal" class="modal-box">
    <button class="modal-close">&times;</button>
    <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem;">Fast Aussie Checkout</h3>
    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.5rem;">Shipped in 100% home compostable mailers via Australia Post.</p>
    <form id="checkout-form">
      <div style="margin-bottom: 1rem;">
        <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Full Name</label>
        <input type="text" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:6px;" placeholder="Matilda Lawson" required>
      </div>
      <div style="margin-bottom: 1rem;">
        <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Email Address</label>
        <input type="email" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:6px;" placeholder="matilda@sydney.com.au" required>
      </div>
      <div style="margin-bottom: 1.5rem;">
        <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Postal Delivery Address</label>
        <input type="text" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:6px;" placeholder="42 Crown St, Surry Hills NSW 2010" required>
      </div>
      <button type="submit" class="btn btn-teal" style="width: 100%;">Place Order & Donate</button>
    </form>
  </div>

  <!-- Custom Right-Click Context Menu -->
  <div id="custom-context-menu" class="custom-context-menu">
    <div class="context-menu-item" data-action="copy"><span>Copy</span> <span style="opacity:0.5;font-size:0.75rem;">Ctrl+C</span></div>
    <div class="context-menu-item" data-action="cut"><span>Cut</span> <span style="opacity:0.5;font-size:0.75rem;">Ctrl+X</span></div>
    <div class="context-menu-item" data-action="paste"><span>Paste</span> <span style="opacity:0.5;font-size:0.75rem;">Ctrl+V</span></div>
    <div class="context-menu-divider"></div>
    <div class="context-menu-item" data-action="selectall"><span>Select All</span> <span style="opacity:0.5;font-size:0.75rem;">Ctrl+A</span></div>
  </div>

  <script type="module" src="js/app.js"></script>"""

# ----------------- 1. index.html (Home) - 9 pictures -----------------
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sydney Sock Co | Ethical Australian Merino & Bamboo Socks</title>
  <meta name="description" content="Sustainably crafted Australian Merino wool and organic bamboo socks. Every pair bought donates a pair of warm socks or a hot meal to Sydney shelters. Surry Hills, Sydney NSW.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('home')}

  <!-- Hero Section -->
  <section id="hero" class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="hero-tag">
          <svg class="icon" style="width:16px; height:16px; color:#0284C7;"><use href="#icon-leaf"></use></svg>
          100% Ethical Australian Materials
        </div>
        <h1 class="hero-title">Step Into Unrivalled Comfort. <span class="teal-text">Give Back to Sydney.</span></h1>
        <p class="hero-desc">
          Crafted from ultra-fine 19.5-micron Australian Merino wool and organic bamboo. Breathable, blister-free, and guaranteed to spark joy on morning walks along Bondi or daily commutes.
        </p>
        <div class="hero-badges">
          <div class="hero-badge-pill">
            <svg class="icon" style="color: #0D9488; width:18px; height:18px;"><use href="#icon-kangaroo"></use></svg>
            Designed in Sydney, NSW
          </div>
          <div class="hero-badge-pill">
            <svg class="icon" style="color: #F43F5E; width:18px; height:18px;"><use href="#icon-heart"></use></svg>
            1 Pair Bought = 1 Donated
          </div>
          <div class="hero-badge-pill">
            <svg class="icon" style="color: #0284C7; width:18px; height:18px;"><use href="#icon-truck"></use></svg>
            Free Express Post Over $60 AUD
          </div>
        </div>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="shop.html" class="btn btn-teal">Shop The Range</a>
          <a href="subscription.html" class="btn btn-outline">Build Sock Box</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Ethical Origins & Pastoral Heritage Section (2 pictures) -->
  <section class="section" style="background: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; align-items: center;">
        <div>
          <span class="section-tag">Ethical Provenance</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">From Sunlit NSW Pastures to Precision Circular Knitting</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            We trace every spool of yarn directly to certified non-mulesed Merino sheep farms across regional New South Wales. The raw wool is scoured in closed-loop systems, spun to fine 19.5-micron threads, and knit on 200-needle Italian machinery for an imperceptible toe seam.
          </p>
          <div style="display: flex; gap: 1.5rem;">
            <div style="flex: 1; border-left: 3px solid var(--primary); padding-left: 1rem;">
              <h4 style="font-size: 1.1rem; color: var(--text-main);">Zero Mulesing Wool</h4>
              <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 4px;">Audited welfare standards across ethical Australian grazing properties.</p>
            </div>
            <div style="flex: 1; border-left: 3px solid var(--accent); padding-left: 1rem;">
              <h4 style="font-size: 1.1rem; color: var(--text-main);">200-Needle Density</h4>
              <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 4px;">Dense, cushioned knit with hand-linked seamless toes.</p>
            </div>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem;">
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/merino-farm.jpg" alt="Australian Merino pasture farm in NSW" style="width: 100%; height: 260px; object-fit: cover; display: block;">
            <div style="padding: 0.75rem; background: var(--bg-card); font-size: 0.85rem; font-weight: 700; color: var(--text-main);">
              Ethical Merino Sheep Pasture
            </div>
          </div>
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/knitting-mill.jpg" alt="Sydney circular sock knitting machinery" style="width: 100%; height: 260px; object-fit: cover; display: block;">
            <div style="padding: 0.75rem; background: var(--bg-card); font-size: 0.85rem; font-weight: 700; color: var(--text-main);">
              Precision 200-Needle Mill
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Featured Bestsellers Showcase (4 pictures) -->
  <section id="bestsellers" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Sydney Favorites</span>
        <h2 class="section-title">Iconic Aussie Pairs Ready for Any Terrain</h2>
        <p class="section-subtitle">
          Designed in Surry Hills and tested on the coastal cliffs of Bondi, mountain trails of the Blue Mountains, and boardroom floors of Martin Place.
        </p>
      </div>

      <div class="products-grid">
        <div class="sock-card">
          <div class="sock-img-box">
            <span class="sock-material-badge">Organic Bamboo</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Meal Donated
            </span>
            <img src="assets/images/koala-crew.jpg" alt="The Koala Canopy Crew" class="sock-card-img">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Botanical & Wildlife</span>
            <h3 class="sock-title">The Koala Canopy Crew</h3>
            <p class="sock-desc">Ultra-soft antibacterial combed bamboo featuring sleeping sleepy koalas amongst native gum leaves.</p>
            <div class="sock-card-footer">
              <span class="sock-price">$18.00 AUD</span>
              <a href="shop.html" class="btn btn-teal">View Details</a>
            </div>
          </div>
        </div>

        <div class="sock-card">
          <div class="sock-img-box">
            <span class="sock-material-badge">100% Merino Wool</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Pair Donated
            </span>
            <img src="assets/images/sunset-merino.jpg" alt="Sydney Harbour Sunset Gradient" class="sock-card-img">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Fine Merino Wool</span>
            <h3 class="sock-title">Sydney Harbour Sunset Gradient</h3>
            <p class="sock-desc">Fine 19.5-micron non-mulesed Australian Merino wool reflecting golden hour reflections across the harbour.</p>
            <div class="sock-card-footer">
              <span class="sock-price">$22.50 AUD</span>
              <a href="shop.html" class="btn btn-teal">View Details</a>
            </div>
          </div>
        </div>

        <div class="sock-card">
          <div class="sock-img-box">
            <span class="sock-material-badge">Merino Cushion</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Pair Donated
            </span>
            <img src="assets/images/bondi-cushion.jpg" alt="Bondi Coastal Trail Cushion" class="sock-card-img">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Athletic & Trail</span>
            <h3 class="sock-title">Bondi Coastal Trail Cushion</h3>
            <p class="sock-desc">Reinforced heel and toe padding with dynamic arch support for the scenic Bondi to Coogee walk.</p>
            <div class="sock-card-footer">
              <span class="sock-price">$24.00 AUD</span>
              <a href="shop.html" class="btn btn-teal">View Details</a>
            </div>
          </div>
        </div>

        <div class="sock-card">
          <div class="sock-img-box">
            <span class="sock-material-badge">Heavy Merino Loop</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Meal Donated
            </span>
            <img src="assets/images/roo-boot.jpg" alt="Red Earth Kangaroo Boot Sock" class="sock-card-img">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Heavy Boot & Work</span>
            <h3 class="sock-title">Red Earth Kangaroo Boot Sock</h3>
            <p class="sock-desc">Thermal insulating loop-knit Merino sock designed for Blundstones, Redbacks, and rugged Australian conditions.</p>
            <div class="sock-card-footer">
              <span class="sock-price">$26.00 AUD</span>
              <a href="shop.html" class="btn btn-teal">View Details</a>
            </div>
          </div>
        </div>
      </div>
      <div style="text-align: center; margin-top: 2.5rem;">
        <a href="shop.html" class="btn btn-teal" style="padding: 0.9rem 2.5rem; font-size: 1.05rem;">Explore All 6 Heritage Styles &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Subscription Box Showcase (1 picture) -->
  <section class="section section-warm">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/subscription-box.jpg" alt="Monthly Sydney Sock Club unboxing box" style="width: 100%; height: 380px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Never Run Out of Fresh Socks</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">The Sydney Sock Club Subscription</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            Receive curated boxes delivered to your doorstep every month, packaged in 100% home-compostable zero-plastic kraft mailers. Every shipment donates warm socks and fresh meals directly to Sydney homeless shelters.
          </p>
          <ul style="list-style: none; margin-bottom: 2rem; display: flex; flex-direction: column; gap: 0.75rem;">
            <li style="display: flex; align-items: center; gap: 0.75rem; font-weight: 600;">
              <svg class="icon" style="color: var(--primary); width:18px; height:18px;"><use href="#icon-check"></use></svg>
              Save up to 20% compared to individual retail pairs
            </li>
            <li style="display: flex; align-items: center; gap: 0.75rem; font-weight: 600;">
              <svg class="icon" style="color: var(--primary); width:18px; height:18px;"><use href="#icon-check"></use></svg>
              Free priority dispatch across Sydney and Australia
            </li>
            <li style="display: flex; align-items: center; gap: 0.75rem; font-weight: 600;">
              <svg class="icon" style="color: var(--primary); width:18px; height:18px;"><use href="#icon-check"></use></svg>
              Pause, swap styles, or cancel anytime with one click
            </li>
          </ul>
          <a href="subscription.html" class="btn btn-teal">Build Your Custom Box &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Ethical Mission & Giving Back (2 pictures) -->
  <section id="impact" class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Community Purpose</span>
          <h2 class="section-title" style="text-align: left;">Socks Are The Most Requested Item in Sydney Homeless Shelters</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; margin-bottom: 1.5rem; line-height: 1.7;">
            When we launched Sydney Sock Co in Surry Hills, we discovered that fresh, clean socks and warm meals are rarely donated to community missions. We partnered directly with local Sydney outreach hubs to establish a strict 1-for-1 giveback promise.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem;">
            <div style="background: var(--bg-subtle); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-color);">
              <h3 style="font-size: 2rem; color: var(--primary); font-weight: 900;">184,200+</h3>
              <p style="font-size: 0.85rem; color: var(--text-muted);">Pairs donated across Sydney</p>
            </div>
            <div style="background: var(--bg-subtle); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-color);">
              <h3 style="font-size: 2rem; color: var(--ocean); font-weight: 900;">100%</h3>
              <p style="font-size: 0.85rem; color: var(--text-muted);">Plastic-free compostable mailers</p>
            </div>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem;">
          <div style="border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-lg);">
            <img src="assets/images/hero.jpg" alt="Sydney Sock Co Australian Merino Wool" style="width: 100%; height: 260px; object-fit: cover; display: block;">
          </div>
          <div style="border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-lg);">
            <img src="assets/images/lifestyle-socks.jpg" alt="Sydney Sock Co lifestyle socks worn on city pavement" style="width: 100%; height: 240px; object-fit: cover; display: block;">
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

# ----------------- 2. shop.html (Shop All) - 8 pictures -----------------
shop_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shop The Range | Sydney Sock Co</title>
  <meta name="description" content="Explore our full collection of Australian Merino wool and organic bamboo socks. Every pair bought donates a pair to Sydney homeless shelters.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('shop')}

  <!-- Shop Hero Banner with content picture (1 picture) -->
  <section style="background: linear-gradient(rgba(4,47,46,0.85), rgba(4,47,46,0.85)); padding: 4rem 0; color: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 2.5rem; align-items: center;">
        <div>
          <span class="impact-badge" style="margin-bottom: 1rem; display: inline-block;">Complete Australian Range</span>
          <h1 style="font-size: 2.8rem; font-weight: 900; margin-bottom: 0.75rem;">Engineered for Australian Feet</h1>
          <p style="font-size: 1.15rem; color: #CCFBF1; margin-bottom: 1.5rem; line-height: 1.7;">
            Every design combines ultra-fine 19.5-micron non-mulesed Merino wool or breathable bamboo with hand-linked seamless toes and reinforced heel cups.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.9rem; font-weight: 600;">
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ 1 Pair Bought = 1 Donated</span>
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ Free Express Post Over $60 AUD</span>
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ 100-Day Blister-Free Guarantee</span>
          </div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.15);">
          <img src="assets/images/lifestyle-socks.jpg" alt="Sydney lifestyle socks collection in action" style="width: 100%; height: 260px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Products Catalog (6 pictures) -->
  <section id="catalog" class="section">
    <div class="container">
      <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
        <div>
          <span class="section-tag">All 6 Signature Styles</span>
          <h2 class="section-title" style="text-align: left;">The Sydney Sock Collection</h2>
        </div>
        <button id="open-size-guide-btn" class="btn btn-outline" style="font-size: 0.85rem; padding: 0.5rem 1rem;">
          View Shoe Size Guide
        </button>
      </div>

      <div id="products-grid" class="products-grid">
        <div class="sock-card" data-id="syd-koala-crew">
          <div class="sock-img-box">
            <span class="sock-material-badge">Organic Bamboo</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Hot Meal
            </span>
            <img src="assets/images/koala-crew.jpg" alt="The Koala Canopy Crew" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Botanical & Wildlife</span>
            <h3 class="sock-title">The Koala Canopy Crew</h3>
            <p class="sock-desc">Ultra-soft antibacterial combed bamboo featuring sleeping sleepy koalas amongst native gum leaves.</p>
            <div class="size-selector" data-sock-id="syd-koala-crew">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$18.00 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-koala-crew">Add to Cart</button>
            </div>
          </div>
        </div>

        <div class="sock-card" data-id="syd-sunset-merino">
          <div class="sock-img-box">
            <span class="sock-material-badge">100% Merino</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Pair Donated
            </span>
            <img src="assets/images/sunset-merino.jpg" alt="Sydney Harbour Sunset Gradient" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Fine Merino Wool</span>
            <h3 class="sock-title">Sydney Harbour Sunset Gradient</h3>
            <p class="sock-desc">Fine 19.5-micron non-mulesed Australian Merino wool reflecting golden hour reflections across the harbour.</p>
            <div class="size-selector" data-sock-id="syd-sunset-merino">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$22.50 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-sunset-merino">Add to Cart</button>
            </div>
          </div>
        </div>

        <div class="sock-card" data-id="syd-bondi-cushion">
          <div class="sock-img-box">
            <span class="sock-material-badge">Merino Blend</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Pair Donated
            </span>
            <img src="assets/images/bondi-cushion.jpg" alt="Bondi Coastal Trail Cushion" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Athletic & Trail</span>
            <h3 class="sock-title">Bondi Coastal Trail Cushion</h3>
            <p class="sock-desc">Reinforced heel and toe padding with dynamic arch support for the scenic coastal walk.</p>
            <div class="size-selector" data-sock-id="syd-bondi-cushion">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$24.00 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-bondi-cushion">Add to Cart</button>
            </div>
          </div>
        </div>

        <div class="sock-card" data-id="syd-roo-boot">
          <div class="sock-img-box">
            <span class="sock-material-badge">Heavy Merino</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Hot Meal
            </span>
            <img src="assets/images/roo-boot.jpg" alt="Red Earth Kangaroo Boot Sock" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Heavy Boot & Work</span>
            <h3 class="sock-title">Red Earth Kangaroo Boot Sock</h3>
            <p class="sock-desc">Thermal insulating loop-knit Merino sock designed for Blundstones and rugged Aussie conditions.</p>
            <div class="size-selector" data-sock-id="syd-roo-boot">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$26.00 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-roo-boot">Add to Cart</button>
            </div>
          </div>
        </div>

        <div class="sock-card" data-id="syd-surry-hills">
          <div class="sock-img-box">
            <span class="sock-material-badge">Mercerised Cotton</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Pair Donated
            </span>
            <img src="assets/images/surry-hills.jpg" alt="Surry Hills Heritage Houndstooth" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Executive Dress</span>
            <h3 class="sock-title">Surry Hills Heritage Houndstooth</h3>
            <p class="sock-desc">Classic bespoke houndstooth knit with hand-linked seamless toes for zero friction in dress shoes.</p>
            <div class="size-selector" data-sock-id="syd-surry-hills">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$19.50 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-surry-hills">Add to Cart</button>
            </div>
          </div>
        </div>

        <div class="sock-card" data-id="syd-cockatoo-ankle">
          <div class="sock-img-box">
            <span class="sock-material-badge">Organic Bamboo</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="#icon-heart"></use></svg>
              1 Hot Meal
            </span>
            <img src="assets/images/cockatoo-ankle.jpg" alt="Sulphur-Crested Cockatoo Ankle" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">Low-Cut Athletic</span>
            <h3 class="sock-title">Sulphur-Crested Cockatoo Ankle</h3>
            <p class="sock-desc">Breathable no-slip silicone heel grip with playful yellow cockatoo crest embroidery on the tab.</p>
            <div class="size-selector" data-sock-id="syd-cockatoo-ankle">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>
            <div class="sock-card-footer">
              <span class="sock-price">$16.50 AUD</span>
              <button class="btn btn-teal add-sock-btn" data-id="syd-cockatoo-ankle">Add to Cart</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Ethical Wool Guarantee Card (1 picture) -->
  <section class="section section-warm" style="border-top: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 3rem; align-items: center;">
        <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
          <img src="assets/images/merino-farm.jpg" alt="Ethical Merino pasture in Australia" style="width: 100%; height: 320px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Pure Australian Wool</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Why 19.5-Micron Merino Outperforms Synthetic Blends</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            Unlike petroleum-based polyesters or cheap synthetics, natural Merino fibers regulate body temperature dynamically: cooling your feet in humid Sydney summers and holding heat during chilly Southern Highlands mornings. Natural lanolin naturally repels odor-causing bacteria so your socks stay fresh after 14 hours of continuous wear.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <span class="hero-badge-pill"><svg class="icon" style="color: var(--primary); width:16px; height:16px;"><use href="#icon-feather"></use></svg> Non-itchy superfine micron</span>
            <span class="hero-badge-pill"><svg class="icon" style="color: var(--ocean); width:16px; height:16px;"><use href="#icon-refresh"></use></svg> Dynamic temperature regulation</span>
            <span class="hero-badge-pill"><svg class="icon" style="color: #F59E0B; width:16px; height:16px;"><use href="#icon-shield-check"></use></svg> Blister-free seamless toes</span>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

# ----------------- 3. about.html (Our Story) - 7 pictures -----------------
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Our Story & Ethical Mission | Sydney Sock Co</title>
  <meta name="description" content="Discover the origins of Sydney Sock Co, our 1-for-1 giveback promise to homeless shelters across Sydney, and ethical Australian Merino wool sourcing.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('about')}

  <!-- About Hero Banner with Studio Image (1 picture) -->
  <section style="background: linear-gradient(rgba(13,148,136,0.92), rgba(4,47,46,0.92)); padding: 4rem 0; color: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: center;">
        <div>
          <span class="impact-badge" style="margin-bottom: 1rem; display: inline-block;">Surry Hills, Sydney NSW</span>
          <h1 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem;">Knitting a Fairer Future for Sydney</h1>
          <p style="font-size: 1.15rem; color: #CCFBF1; line-height: 1.7;">
            We started Sydney Sock Co with a single machine and a radical pledge: every single pair you buy provides a warm pair of socks or a hot nutritious meal to someone sleeping rough in our hometown.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.2);">
          <img src="assets/images/surry-hills.jpg" alt="Sydney Sock Co flagship studio in Surry Hills" style="width: 100%; height: 260px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Story Chapter 1: The Merino Pasture (1 picture) -->
  <section id="merino" class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/merino-farm.jpg" alt="Australian Merino pasture farm in regional NSW" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Chapter One</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Sourcing Only Non-Mulesed Australian Merino</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Australia grows the world's most luxurious wool, yet mass-market apparel often cuts corners with mulesed stock and harsh chemical baths. We partner directly with generational sheep stations across regional New South Wales who practice regenerative grazing and humane animal husbandry.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            Our Merino fleece measures an ultra-fine 19.5 microns, giving it cloud-soft comfort that never pricks or scratches sensitive skin. It breathes naturally, absorbs moisture vapor before it turns to liquid sweat, and insulates in both wet and dry conditions.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Story Chapter 2: The Knitting Mill (1 picture) -->
  <section class="section section-warm">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Chapter Two</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">200-Needle Circular Precision Knitting</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Standard mass-produced socks use 96 to 144 needles, resulting in loose weaves that stretch out after three washes. Our Sydney production utilizes 200-needle high-density circular knitting machines.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            This creates an ultra-tight, durable matrix that resists heel and toe blowout. Each toe is hand-linked with zero bulky raised seams, eliminating hot spots and blisters during long Sydney walking commutes or coastal treks.
          </p>
          <div style="display: flex; gap: 1rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); flex: 1;">
              <strong style="color: var(--primary); font-size: 1.25rem;">200 Needle</strong>
              <div style="font-size: 0.85rem; color: var(--text-muted);">High-density anti-sag weave</div>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); flex: 1;">
              <strong style="color: var(--primary); font-size: 1.25rem;">Hand-Linked</strong>
              <div style="font-size: 0.85rem; color: var(--text-muted);">Zero-friction seamless toes</div>
            </div>
          </div>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/knitting-mill.jpg" alt="Circular knitting machinery in Sydney mill" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Story Chapter 3: Shelter Giving (1 picture) -->
  <section id="impact" class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/hero.jpg" alt="Australian Merino wool and community shelter donation" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Chapter Three</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">The 1-for-1 Sydney Shelter Giving Program</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Socks are the most urgently requested clothing item at emergency shelters, but they are the least frequently donated. When you buy a pair of Sydney Sock Co socks, our donation partners (including the Wayside Chapel and Matthew Talbot Hostel) receive custom-manufactured antimicrobial shelter socks or hot meals.
          </p>
          <div style="background: #F0FDFA; border: 1px solid #99F6E4; border-radius: 12px; padding: 1.5rem; margin-top: 1.5rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
              <svg class="icon" style="color: #F43F5E; width:22px; height:22px;"><use href="#icon-heart"></use></svg>
              <h4 style="font-size: 1.1rem; color: #0F766E;">184,200+ Donations Delivered</h4>
            </div>
            <p style="font-size: 0.95rem; color: #115E59; line-height: 1.6;">
              Every quarter, our volunteer team loads delivery vans at our Surry Hills studio and distributes fresh thermal socks directly to shelters across the Sydney CBD, Darlinghurst, Parramatta, and Woolloomooloo.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Story Chapter 4: Durability & Craft (1 picture) -->
  <section class="section section-warm">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Chapter Four</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Built for Boots, Trails & Daily Wear</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Australian footwear demands durability. Whether paired with elastic-sided leather boots on rugged terrain or sneakers for the city commute, our reinforced heel and toe cups withstand tens of thousands of abrasion cycles before showing wear.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            We back every pair with our 100-Day No-Hole Guarantee: if your socks develop a hole within 100 days of purchase, return them for a replacement pair on the house.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/roo-boot.jpg" alt="Heavy duty Merino work boot socks" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Story Chapter 5: Surry Hills Roots & Sydney Pavement (2 pictures) -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/lifestyle-socks.jpg" alt="Sydney lifestyle socks worn on city pavement" style="width: 100%; height: 260px; object-fit: cover; display: block;">
          </div>
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/sunset-merino.jpg" alt="Sydney Harbour sunset gradient Merino wool" style="width: 100%; height: 260px; object-fit: cover; display: block;">
          </div>
        </div>
        <div>
          <span class="section-tag">Chapter Five</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Rooted in Surry Hills, Sydney NSW</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Surry Hills was historically the textile and garment manufacturing beating heart of Sydney. From our studio at 42 Crown Street, we maintain that legacy by designing modern, vibrant patterns celebrating Australian native flora, fauna, and coastal colours.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 2rem;">
            Drop by our studio to feel yarn samples, pick up local click-and-collect orders, or learn more about our ongoing homeless shelter volunteer drives.
          </p>
          <a href="contact.html" class="btn btn-teal">Visit Our Studio & Showroom &rarr;</a>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

# ----------------- 4. subscription.html (Sock Club) - 7 pictures -----------------
subscription_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Sydney Sock Club | Monthly Sock Subscription Box</title>
  <meta name="description" content="Join the Sydney Sock Club. Get fresh Australian Merino and organic bamboo socks delivered monthly. Save 15-20% plus 1 pair donated to Sydney shelters with every box.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('subscription')}

  <!-- Subscription Hero Banner with Content Picture (1 picture) -->
  <section style="background: linear-gradient(rgba(4,47,46,0.9), rgba(4,47,46,0.9)); padding: 4rem 0; color: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: center;">
        <div>
          <span class="impact-badge" style="margin-bottom: 1rem; display: inline-block;">Monthly Sock Box Club</span>
          <h1 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem;">Fresh Socks. Maximum Comfort. Guaranteed Impact.</h1>
          <p style="font-size: 1.15rem; color: #CCFBF1; margin-bottom: 1.5rem; line-height: 1.7;">
            Delivered directly to your door in 100% home compostable kraft mailers. Every monthly box donates equal pairs or hot meals to Sydney shelters.
          </p>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap; font-size: 0.95rem; font-weight: 700;">
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ Save Up to 20%</span>
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ Free Express Shipping</span>
            <span class="hero-badge-pill" style="color: var(--text-main);">✓ Pause or Cancel Anytime</span>
          </div>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.2);">
          <img src="assets/images/subscription-box.jpg" alt="Monthly Sydney Sock Club kraft gift unboxing box" style="width: 100%; height: 280px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Subscription Interactive Builder -->
  <section id="subscription" class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Configure Your Box</span>
        <h2 class="section-title">Build Your Sydney Sock Subscription</h2>
        <p class="section-subtitle">
          Select your desired pair count and aesthetic theme. You can swap styles or adjust frequency anytime from your account.
        </p>
      </div>

      <div class="sub-builder-card">
        <div>
          <div class="sub-step">
            <h4>Step 1: Choose Monthly Pair Count</h4>
            <div class="tier-options">
              <div class="tier-card" data-pairs="2">
                <strong>2 Pairs</strong>
                <span>Save 10% &bull; $32 AUD</span>
              </div>
              <div class="tier-card active" data-pairs="3">
                <strong>3 Pairs</strong>
                <span>Most Popular &bull; Save 15%</span>
              </div>
              <div class="tier-card" data-pairs="4">
                <strong>4 Pairs</strong>
                <span>Best Value &bull; Save 20%</span>
              </div>
            </div>
          </div>

          <div class="sub-step">
            <h4>Step 2: Choose Style Aesthetic</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
              <div style="padding: 1.25rem; border: 2px solid var(--primary); border-radius: 8px; text-align: center; background: white; cursor: pointer;">
                <strong>Aussie Flora & Fauna</strong>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Koalas, Kangaroos, Cockatoos</p>
              </div>
              <div style="padding: 1.25rem; border: 1px solid var(--border-color); border-radius: 8px; text-align: center; background: white; cursor: pointer;">
                <strong>Executive Classic</strong>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Houndstooth, Ribbed & Solids</p>
              </div>
              <div style="padding: 1.25rem; border: 1px solid var(--border-color); border-radius: 8px; text-align: center; background: white; cursor: pointer;">
                <strong>Curated Mix</strong>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">Seasonal Surprises & Wool Blends</p>
              </div>
            </div>
          </div>
        </div>

        <div class="sub-summary-box">
          <span style="font-weight: 700; color: var(--primary); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">Subscription Rate</span>
          <div class="sub-price-tag" id="sub-price-display">$45.00 AUD</div>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem; line-height: 1.6;">
            Includes 3 pairs of premium socks + 3 hot meals donated to Sydney homeless missions each month. Free Australian priority delivery included.
          </p>
          <button class="btn btn-teal" style="width: 100%;" onclick="document.getElementById('checkout-modal').classList.add('open'); document.getElementById('modal-overlay').classList.add('open');">
            Subscribe Now & Save 15%
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Recent Monthly Box Rotations (3 pictures) -->
  <section class="section section-warm">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Previous Editions</span>
        <h2 class="section-title">What Club Members Received in Recent Boxes</h2>
        <p class="section-subtitle">
          Every month features a fresh mix of non-mulesed Merino wool and organic bamboo socks crafted for the current Sydney season.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        <div style="background: white; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
          <img src="assets/images/koala-crew.jpg" alt="Month 1 Koala Canopy Crew" style="width: 100%; height: 240px; object-fit: cover; display: block;">
          <div style="padding: 1.25rem;">
            <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Box Month 1</span>
            <h4 style="font-size: 1.15rem; margin-top: 4px;">The Koala Canopy Crew</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 6px;">Combed organic bamboo with native wattle blooms and gentle ribbing.</p>
          </div>
        </div>

        <div style="background: white; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
          <img src="assets/images/sunset-merino.jpg" alt="Month 2 Sydney Harbour Sunset Gradient" style="width: 100%; height: 240px; object-fit: cover; display: block;">
          <div style="padding: 1.25rem;">
            <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Box Month 2</span>
            <h4 style="font-size: 1.15rem; margin-top: 4px;">Sydney Harbour Sunset Gradient</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 6px;">19.5-micron fine Australian Merino wool inspired by sunset over Port Jackson.</p>
          </div>
        </div>

        <div style="background: white; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
          <img src="assets/images/cockatoo-ankle.jpg" alt="Month 3 Sulphur-Crested Cockatoo Ankle" style="width: 100%; height: 240px; object-fit: cover; display: block;">
          <div style="padding: 1.25rem;">
            <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); text-transform: uppercase;">Box Month 3</span>
            <h4 style="font-size: 1.15rem; margin-top: 4px;">Sulphur-Crested Cockatoo Ankle</h4>
            <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 6px;">Summer athletic cut with silicone anti-slip heel grip and iconic yellow crest.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Packaging, Craft & Lifestyle Details (3 pictures) -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/knitting-mill.jpg" alt="Precision circular mill production" style="width: 100%; height: 360px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Eco-Conscious Packaging</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Zero Plastic. 100% Home Compostable Mailers.</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            Every Sydney Sock Club subscription box is packed by hand in our Surry Hills studio using FSC-certified unbleached kraft cardboard and sealed inside cassava-starch compostable mailers. Worm farms and backyard compost bins break them down entirely in 90 days.
          </p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
              <img src="assets/images/lifestyle-socks.jpg" alt="Everyday lifestyle comfort in Sydney" style="width: 100%; height: 160px; object-fit: cover; display: block;">
            </div>
            <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
              <img src="assets/images/merino-farm.jpg" alt="Ethical farm provenance" style="width: 100%; height: 160px; object-fit: cover; display: block;">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

# ----------------- 5. care-guide.html (Care Guide) - 7 pictures -----------------
care_guide_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sock Care & Longevity Guide | Sydney Sock Co</title>
  <meta name="description" content="Learn how to care for your Australian Merino wool and organic bamboo socks. Washing temperatures, eucalyptus detergent tips, and air drying for maximum lifespan.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('care')}

  <!-- Care Guide Hero with Content Image (1 picture) -->
  <section style="background: linear-gradient(rgba(13,148,136,0.92), rgba(4,47,46,0.92)); padding: 4rem 0; color: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: center;">
        <div>
          <span class="impact-badge" style="margin-bottom: 1rem; display: inline-block;">Fabric Longevity</span>
          <h1 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem;">How to Care for Natural Australian Fibers</h1>
          <p style="font-size: 1.15rem; color: #CCFBF1; line-height: 1.7;">
            Natural Merino wool and bamboo are self-regulating, odor-resistant fibers. With simple, mindful washing habits, your Sydney Sock Co pairs will remain plush, vibrant, and blister-free for years.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.2);">
          <img src="assets/images/sock-care.jpg" alt="Gentle hand washing of Merino socks with eucalyptus wash" style="width: 100%; height: 260px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Step 1: Wool Care Fundamentals (1 picture) -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Guideline 01</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Wash in Cold Water with Eucalyptus Detergent</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Hot water strips the natural protective lanolin oils from pure Australian Merino wool fibers, making them brittle and prone to shrinkage. Always set your washing machine to a gentle cold cycle (30°C or below) or hand-wash in a basin.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            We recommend pH-neutral wool wash containing natural Australian eucalyptus oil. Eucalyptus naturally disinfects without harsh bleach or enzymes that degrade protein fibers.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/merino-farm.jpg" alt="Natural Australian wool sourcing" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Step 2: Protecting Cushion Soles (1 picture) -->
  <section class="section section-warm">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/bondi-cushion.jpg" alt="Bondi Coastal Trail cushioned athletic sock" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Guideline 02</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Turn Inside Out Before Washing</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Turning your socks inside out protects the exterior patterns, fine gauge yarns, and jacquard artwork from machine friction and pilling against rough fabrics like denim.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            It also exposes the interior terry-loop cushioning directly to water and detergent, thoroughly rinsing away sweat salts and skin particulates that collect in the footbed during trail running or long shifts.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Step 3: Heavy Duty Boot Sock Care (1 picture) -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Guideline 03</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Air Dry in the Shade (Never Tumble Dry)</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            High heat from electric clothes dryers is the number one destroyer of socks: it degrades the elastane arch bands and shrinks wool fibers.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            Hang your socks on a drying rack or clothesline in a shaded, well-ventilated spot. The fresh Sydney sea breeze dries Merino quickly without the fiber fatigue caused by direct midday sunlight.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/roo-boot.jpg" alt="Heavy duty Merino work boot sock durability" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Step 4: Storage & Daily Longevity (1 picture) -->
  <section class="section section-warm">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 1px solid var(--border-color);">
          <img src="assets/images/lifestyle-socks.jpg" alt="Socks worn on city street" style="width: 100%; height: 340px; object-fit: cover; display: block;">
        </div>
        <div>
          <span class="section-tag">Guideline 04</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Fold Flat, Never Roll Into Tight Balls</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Rolling socks into tight inverted potato balls overstretches the ribbed cuff elastic over time, causing socks to slump down your calf during the day.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7;">
            Store your socks flat or fold them in half gently. The double-welted cuffs will maintain their snug grip around your ankles for hundreds of wear cycles.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Step 5: Dress Sock Maintenance & Packaging Storage (2 pictures) -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3.5rem; align-items: center;">
        <div>
          <span class="section-tag">Guideline 05</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">Keep Toenails Trimmed & Store in Breathable Kraft Boxes</h2>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1rem;">
            Sharp, unfiled toenails exert immense localized pressure against the front toe pocket with every step inside dress shoes or leather boots. Regularly filing your nails preserves our hand-linked seamless toe closures indefinitely.
          </p>
          <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 1.5rem;">
            Keep spare pairs neatly organised inside breathable cardboard drawer organizers or our signature gift boxes away from direct dampness.
          </p>
          <a href="shop.html" class="btn btn-teal">Explore The Heritage Range &rarr;</a>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/surry-hills.jpg" alt="Surry Hills Heritage Houndstooth executive dress sock" style="width: 100%; height: 260px; object-fit: cover; display: block;">
          </div>
          <div style="border-radius: var(--radius-md); overflow: hidden; box-shadow: var(--shadow-md); border: 1px solid var(--border-color);">
            <img src="assets/images/subscription-box.jpg" alt="Sydney Sock Co subscription storage box" style="width: 100%; height: 260px; object-fit: cover; display: block;">
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

# ----------------- 6. contact.html (Contact & Studio) - 7 pictures -----------------
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact & Surry Hills Studio | Sydney Sock Co</title>
  <meta name="description" content="Get in touch with Sydney Sock Co. Visit our flagship studio at 42 Crown St, Surry Hills NSW. Customer support, shelter donation inquiries, and custom corporate gifting.">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
{SVG_SPRITE}
{get_header('contact')}

  <!-- Contact Hero with Content Image (1 picture) -->
  <section style="background: linear-gradient(rgba(4,47,46,0.9), rgba(4,47,46,0.9)); padding: 4rem 0; color: white; border-bottom: 1px solid var(--border-color);">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 3rem; align-items: center;">
        <div>
          <span class="impact-badge" style="margin-bottom: 1rem; display: inline-block;">We'd Love to Chat</span>
          <h1 style="font-size: 3rem; font-weight: 900; margin-bottom: 1rem;">Visit Our Surry Hills Studio & Workshop</h1>
          <p style="font-size: 1.15rem; color: #CCFBF1; line-height: 1.7;">
            Located in the historic fashion district of Surry Hills. Drop by to feel fabric swatches, collect online orders, or partner with us for charity giving drives.
          </p>
        </div>
        <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); border: 2px solid rgba(255,255,255,0.2);">
          <img src="assets/images/surry-hills.jpg" alt="Surry Hills Sydney Studio storefront" style="width: 100%; height: 260px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Form & Studio Details -->
  <section class="section">
    <div class="container">
      <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 3.5rem;">
        <div>
          <span class="section-tag">Send Us A Note</span>
          <h2 class="section-title" style="text-align: left; margin-top: 0.5rem;">How Can We Help You Today?</h2>
          <form id="contact-form" style="display: flex; flex-direction: column; gap: 1.25rem; margin-top: 1.5rem;" onsubmit="event.preventDefault(); alert('Thank you for contacting Sydney Sock Co! Our Surry Hills team will reply within 24 hours.'); this.reset();">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Your Name</label>
                <input type="text" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:8px;" placeholder="Liam Anderson" required>
              </div>
              <div>
                <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Email Address</label>
                <input type="email" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:8px;" placeholder="liam@sydney.com.au" required>
              </div>
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Subject</label>
              <select style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:8px; background:white;">
                <option>Customer Order & Shipping Inquiry</option>
                <option>Shelter Donation & Charity Partnership</option>
                <option>Corporate Gifting & Custom Knitting</option>
                <option>Wholesale & Retail Stockist Request</option>
                <option>Press & Media</option>
              </select>
            </div>
            <div>
              <label style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:0.35rem;">Your Message</label>
              <textarea rows="5" style="width:100%; padding:0.75rem; border:1px solid var(--border-color); border-radius:8px; font-family:inherit;" placeholder="Tell us how we can assist..." required></textarea>
            </div>
            <button type="submit" class="btn btn-teal" style="align-self: flex-start; padding: 0.85rem 2.25rem;">
              Send Message
            </button>
          </form>
        </div>

        <div>
          <div style="background: white; border-radius: var(--radius-lg); border: 1px solid var(--border-color); padding: 2rem; box-shadow: var(--shadow-sm);">
            <h3 style="font-size: 1.3rem; font-weight: 800; margin-bottom: 1.25rem;">Studio Details</h3>
            <div style="display: flex; flex-direction: column; gap: 1.25rem;">
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <svg class="icon" style="color: var(--primary); width:22px; height:22px; flex-shrink:0; margin-top:2px;"><use href="#icon-map-pin"></use></svg>
                <div>
                  <strong>Address</strong>
                  <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 2px;">42 Crown Street, Surry Hills NSW 2010, Australia</p>
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <svg class="icon" style="color: var(--primary); width:22px; height:22px; flex-shrink:0; margin-top:2px;"><use href="#icon-phone"></use></svg>
                <div>
                  <strong>Phone</strong>
                  <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 2px;">(02) 9358 1290 (Mon &ndash; Fri, 9am &ndash; 5pm AEST)</p>
                </div>
              </div>
              <div style="display: flex; gap: 1rem; align-items: flex-start;">
                <svg class="icon" style="color: var(--primary); width:22px; height:22px; flex-shrink:0; margin-top:2px;"><use href="#icon-mail"></use></svg>
                <div>
                  <strong>Direct Email</strong>
                  <p style="font-size: 0.9rem; color: var(--text-muted); margin-top: 2px;">hello@sydneysockco.com.au</p>
                </div>
              </div>
            </div>

            <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
              <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem;">Showroom Visiting Hours</h4>
              <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6;">
                Monday &ndash; Friday: 9:30 AM &ndash; 5:30 PM<br>
                Saturday: 10:00 AM &ndash; 4:00 PM<br>
                Sunday: Closed (Distribution to Sydney Shelters)
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Photo Gallery Showcase Across Operations (6 pictures) -->
  <section class="section section-warm">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Behind the Scenes</span>
        <h2 class="section-title">Our Studio, Shelters & Australian Operations</h2>
        <p class="section-subtitle">
          See the full circle of Sydney Sock Co: from parcel dispatch in Surry Hills to our community shelter distributions.
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/hero.jpg" alt="Shelter donation distribution" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">Shelter Hub</div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/subscription-box.jpg" alt="Sustainable packaging assembly" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">Zero-Waste Packaging</div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/knitting-mill.jpg" alt="Custom corporate knitting" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">Mill Machinery</div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/lifestyle-socks.jpg" alt="Surry Hills street lifestyle" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">Sydney Street Test</div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/sunset-merino.jpg" alt="Merino sample swatches" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">Merino Swatches</div>
        </div>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); background: white;">
          <img src="assets/images/merino-farm.jpg" alt="Merino pasture station" style="width: 100%; height: 180px; object-fit: cover; display: block;">
          <div style="padding: 0.75rem; font-size: 0.85rem; font-weight: 700;">NSW Pasture Station</div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
</body>
</html>
"""

pages = {
    "index.html": index_html,
    "shop.html": shop_html,
    "about.html": about_html,
    "subscription.html": subscription_html,
    "care-guide.html": care_guide_html,
    "contact.html": contact_html,
}

for filename, content in pages.items():
    file_path = os.path.join(REPO, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename} successfully ({len(content)} bytes).")

print("All 6 Sydney Sock Co pages updated successfully!")
