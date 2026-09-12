import { socksData, sizeGuideData } from './products.js';
import { CurrencyManager } from './currency.js';
import { SockCartManager } from './cart.js';
import { calculateSubscriptionPlan } from './subscription.js';

document.addEventListener('DOMContentLoaded', () => {
  const currency = new CurrencyManager();
  const cart = new SockCartManager();

  const productsContainer = document.getElementById('products-grid');
  const currencySelect = document.getElementById('currency-select');
  const cartDrawer = document.getElementById('cart-drawer');
  const cartOverlay = document.getElementById('cart-overlay');
  const cartTrigger = document.getElementById('cart-trigger');
  const closeCartBtn = document.getElementById('close-cart-btn');
  const cartItemsList = document.getElementById('cart-items-list');
  const cartBadge = document.getElementById('cart-badge');
  const cartSubtotalEl = document.getElementById('cart-subtotal');
  const cartTotalEl = document.getElementById('cart-total');
  const shippingProgressBar = document.getElementById('shipping-progress-bar');
  const shippingNotice = document.getElementById('shipping-notice');
  const impactCountEl = document.getElementById('impact-count');
  const sizeModal = document.getElementById('size-modal');
  const checkoutModal = document.getElementById('checkout-modal');
  const modalOverlay = document.getElementById('modal-overlay');

  // Render Product Catalog
  function renderProducts() {
    if (!productsContainer) return;
    productsContainer.innerHTML = socksData.map(sock => {
      const priceObj = currency.convert(sock.basePriceAUD);
      return `
        <div class="sock-card" data-id="${sock.id}">
          <div class="sock-img-box">
            <span class="sock-material-badge">${sock.material}</span>
            <span class="sock-impact-pill">
              <svg class="icon" style="color:#F43F5E; width:14px; height:14px;"><use href="assets/svgs/icons.svg#icon-heart"></use></svg>
              ${sock.impact}
            </span>
            <img src="assets/images/${sock.image}" alt="${sock.title}" class="sock-card-img" loading="lazy">
          </div>
          <div class="sock-card-body">
            <span class="sock-category">${sock.category}</span>
            <h3 class="sock-title">${sock.title}</h3>
            <p class="sock-desc">${sock.description}</p>
            
            <div class="size-selector" data-sock-id="${sock.id}">
              <button class="size-btn active" data-size="S / M">S / M</button>
              <button class="size-btn" data-size="M / L">M / L</button>
              <button class="size-btn" data-size="XL">XL</button>
            </div>

            <div class="sock-card-footer">
              <span class="sock-price">${priceObj.formatted}</span>
              <button class="btn btn-teal add-sock-btn" data-id="${sock.id}">
                Add to Cart
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }
  renderProducts();

  // Currency Switcher
  currencySelect?.addEventListener('change', (e) => {
    currency.setCurrency(e.target.value);
    renderProducts();
    updateCartUI();
  });

  // Size Button Selection
  document.addEventListener('click', (e) => {
    const sizeBtn = e.target.closest('.size-btn');
    if (sizeBtn) {
      const parent = sizeBtn.closest('.size-selector');
      parent.querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
      sizeBtn.classList.add('active');
    }
  });

  // Update Cart Drawer UI
  function updateCartUI() {
    const totals = cart.getTotals();
    if (cartBadge) cartBadge.textContent = totals.itemCount;

    const subtotalConverted = currency.convert(totals.finalSubtotalAUD);
    if (cartSubtotalEl) cartSubtotalEl.textContent = subtotalConverted.formatted;
    if (cartTotalEl) cartTotalEl.textContent = subtotalConverted.formatted;

    if (shippingProgressBar && shippingNotice) {
      shippingProgressBar.style.width = `${totals.shippingProgressPercent}%`;
      if (totals.isFreeShipping) {
        shippingNotice.innerHTML = `<strong>Free Express Shipping Unlocked!</strong> (Australia & Worldwide)`;
      } else {
        const remainingConverted = currency.convert(totals.amountForFreeShippingAUD);
        shippingNotice.innerHTML = `Add <strong>${remainingConverted.formatted}</strong> more for Free Shipping!`;
      }
    }

    if (impactCountEl) {
      impactCountEl.textContent = totals.totalDonations;
    }

    if (cartItemsList) {
      if (cart.items.length === 0) {
        cartItemsList.innerHTML = `<div style="text-align:center;color:#78716C;padding:2rem;">Your sock drawer is empty.</div>`;
      } else {
        cartItemsList.innerHTML = cart.items.map(item => {
          const itemPrice = currency.convert(item.basePriceAUD);
          return `
            <div class="cart-item-row" data-key="${item.itemKey}">
              <img src="assets/images/${item.image || 'koala-crew.jpg'}" alt="${item.title}" style="width:48px; height:48px; object-fit:cover; border-radius:8px; border:1px solid #E7E5E4;">
              <div style="flex-grow:1;">
                <div style="font-size:0.9rem; font-weight:700;">${item.title}</div>
                <div style="font-size:0.8rem; color:#78716C;">Size: ${item.size} &bull; ${item.material}</div>
                <div style="font-size:0.85rem; font-weight:700; color:#0D9488; margin-top:2px;">${itemPrice.formatted}</div>
                <div style="display:flex; align-items:center; gap:0.5rem; margin-top:4px;">
                  <button class="qty-btn" data-action="dec" data-key="${item.itemKey}" style="width:22px;height:22px;border:1px solid #E7E5E4;border-radius:4px;cursor:pointer;">-</button>
                  <span style="font-size:0.85rem; font-weight:600;">${item.quantity}</span>
                  <button class="qty-btn" data-action="inc" data-key="${item.itemKey}" style="width:22px;height:22px;border:1px solid #E7E5E4;border-radius:4px;cursor:pointer;">+</button>
                </div>
              </div>
              <button class="qty-btn" data-action="del" data-key="${item.itemKey}" style="border:none;background:none;color:#EF4444;cursor:pointer;font-size:1.1rem;">&times;</button>
            </div>
          `;
        }).join('');
      }
    }
  }
  updateCartUI();

  // Drawer Controls
  function openCart() {
    cartDrawer?.classList.add('open');
    cartOverlay?.classList.add('open');
  }
  function closeCart() {
    cartDrawer?.classList.remove('open');
    cartOverlay?.classList.remove('open');
  }
  cartTrigger?.addEventListener('click', openCart);
  closeCartBtn?.addEventListener('click', closeCart);
  cartOverlay?.addEventListener('click', closeCart);

  // Add To Cart Event
  document.addEventListener('click', (e) => {
    const addBtn = e.target.closest('.add-sock-btn');
    if (addBtn) {
      const sockId = addBtn.getAttribute('data-id');
      const sock = socksData.find(s => s.id === sockId);
      const card = addBtn.closest('.sock-card');
      const activeSize = card?.querySelector('.size-btn.active')?.getAttribute('data-size') || 'M / L';

      if (sock) {
        cart.addItem(sock, activeSize, 1);
        updateCartUI();
        showToast(`Added ${sock.title} (${activeSize}) to cart!`);
        openCart();
      }
    }
  });

  // Cart Items Controls
  cartItemsList?.addEventListener('click', (e) => {
    const btn = e.target.closest('.qty-btn');
    if (!btn) return;
    const key = btn.getAttribute('data-key');
    const action = btn.getAttribute('data-action');
    if (action === 'inc') cart.updateQuantity(key, 1);
    if (action === 'dec') cart.updateQuantity(key, -1);
    if (action === 'del') cart.removeItem(key);
    updateCartUI();
  });

  // Toast Function
  function showToast(msg) {
    const toast = document.createElement('div');
    toast.style.cssText = `
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #042F2E;
      color: #CCFBF1;
      border: 1px solid #0D9488;
      border-radius: 8px;
      padding: 12px 20px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.15);
      z-index: 9999;
      font-weight: 600;
      font-size: 0.9rem;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3200);
  }

  // Subscription Builder Interactivity
  let currentPairTier = 3;
  let currentTheme = 'mixed';
  let currentFreq = 'monthly';

  document.querySelectorAll('.tier-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.tier-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      currentPairTier = Number(card.getAttribute('data-pairs'));
      updateSubscriptionDisplay();
    });
  });

  function updateSubscriptionDisplay() {
    const plan = calculateSubscriptionPlan({
      pairCount: currentPairTier,
      theme: currentTheme,
      frequency: currentFreq
    });
    const converted = currency.convert(plan.priceAUD);
    const subPriceEl = document.getElementById('sub-price-display');
    if (subPriceEl) subPriceEl.textContent = converted.formatted;
  }

  // Size Guide Modal
  document.getElementById('open-size-guide-btn')?.addEventListener('click', () => {
    modalOverlay?.classList.add('open');
    sizeModal?.classList.add('open');
  });

  // Modal closers
  document.querySelectorAll('.modal-close, #modal-overlay').forEach(el => {
    el.addEventListener('click', () => {
      modalOverlay?.classList.remove('open');
      sizeModal?.classList.remove('open');
      checkoutModal?.classList.remove('open');
    });
  });

  // Checkout Modal Trigger
  document.getElementById('checkout-btn')?.addEventListener('click', () => {
    if (cart.items.length === 0) {
      showToast('Please add pairs to your cart first.');
      return;
    }
    closeCart();
    modalOverlay?.classList.add('open');
    checkoutModal?.classList.add('open');
  });

  // Checkout Form Submission
  document.getElementById('checkout-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const orderId = 'SYD-AU-' + Math.floor(10000 + Math.random() * 90000);
    cart.clearCart();
    updateCartUI();
    modalOverlay?.classList.remove('open');
    checkoutModal?.classList.remove('open');
    showToast(`Order Confirmed! Reference #${orderId}. Thank you for your ethical donation!`);
  });

  // Right-Click Context Menu Implementation (User Rule Compliance)
  const contextMenu = document.getElementById('custom-context-menu');
  window.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    if (!contextMenu) return;
    contextMenu.style.left = `${Math.min(e.clientX, window.innerWidth - 180)}px`;
    contextMenu.style.top = `${Math.min(e.clientY, window.innerHeight - 180)}px`;
    contextMenu.classList.add('open');
  });

  window.addEventListener('click', () => {
    contextMenu?.classList.remove('open');
  });

  contextMenu?.addEventListener('click', async (e) => {
    const item = e.target.closest('.context-menu-item');
    if (!item) return;
    const action = item.getAttribute('data-action');
    try {
      if (action === 'copy') {
        const sel = window.getSelection()?.toString();
        if (sel) await navigator.clipboard.writeText(sel);
      } else if (action === 'paste') {
        const text = await navigator.clipboard.readText();
        const active = document.activeElement;
        if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA')) {
          active.value += text;
        }
      } else if (action === 'cut') {
        const active = document.activeElement;
        if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA')) {
          await navigator.clipboard.writeText(active.value);
          active.value = '';
        }
      } else if (action === 'selectall') {
        const active = document.activeElement;
        if (active && (active.tagName === 'INPUT' || active.tagName === 'TEXTAREA')) {
          active.select();
        } else {
          document.execCommand('selectAll');
        }
      }
    } catch {
      // Clipboard fallback
    }
    contextMenu.classList.remove('open');
  });
});
