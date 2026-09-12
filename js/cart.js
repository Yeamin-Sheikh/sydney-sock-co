/**
 * Shopping Cart & Australian Giveback Impact Engine
 */
export class SockCartManager {
  constructor(storageKey = 'sydney_sock_cart') {
    this.storageKey = storageKey;
    this.freeShippingThresholdAUD = 60.00;
    this.activePromo = null;
    this.promoCodes = {
      'SYDNEY10': { discountPercent: 10, label: '10% Sydney Welcome Offer' },
      'AUSSIE20': { discountPercent: 20, label: '20% Aussie Bundle Discount' }
    };
    this.items = this.loadCart();
  }

  loadCart() {
    try {
      const saved = localStorage.getItem(this.storageKey);
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  }

  saveCart() {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.items));
    } catch (e) {
      console.warn('Cart persistence failed', e);
    }
  }

  addItem(product, size = 'M / L', quantity = 1) {
    const itemKey = `${product.id}-${size}`;
    const existing = this.items.find(i => i.itemKey === itemKey);
    if (existing) {
      existing.quantity += quantity;
    } else {
      this.items.push({
        itemKey,
        id: product.id,
        title: product.title,
        basePriceAUD: Number(product.basePriceAUD),
        size,
        material: product.material,
        impact: product.impact,
        image: product.image || 'koala-crew.jpg',
        quantity
      });
    }
    this.saveCart();
    return this.items;
  }

  removeItem(itemKey) {
    this.items = this.items.filter(i => i.itemKey !== itemKey);
    this.saveCart();
    return this.items;
  }

  updateQuantity(itemKey, delta) {
    const item = this.items.find(i => i.itemKey === itemKey);
    if (!item) return;
    item.quantity += delta;
    if (item.quantity <= 0) {
      this.removeItem(itemKey);
    } else {
      this.saveCart();
    }
  }

  clearCart() {
    this.items = [];
    this.activePromo = null;
    this.saveCart();
  }

  applyPromo(code) {
    const cleanCode = (code || '').trim().toUpperCase();
    if (this.promoCodes[cleanCode]) {
      this.activePromo = {
        code: cleanCode,
        ...this.promoCodes[cleanCode]
      };
      return { success: true, promo: this.activePromo };
    }
    return { success: false, message: 'Invalid promo code. Try SYDNEY10' };
  }

  getTotals() {
    const rawSubtotalAUD = this.items.reduce((sum, item) => sum + (item.basePriceAUD * item.quantity), 0);
    const subtotalAUD = Math.round(rawSubtotalAUD * 100) / 100;

    const discountAmountAUD = this.activePromo
      ? Math.round((subtotalAUD * (this.activePromo.discountPercent / 100)) * 100) / 100
      : 0;

    const finalSubtotalAUD = Math.max(0, Math.round((subtotalAUD - discountAmountAUD) * 100) / 100);
    
    // Free shipping check against base subtotal
    const isFreeShipping = subtotalAUD >= this.freeShippingThresholdAUD;
    const amountForFreeShippingAUD = Math.max(0, Math.round((this.freeShippingThresholdAUD - subtotalAUD) * 100) / 100);
    const shippingProgressPercent = Math.min(100, Math.round((subtotalAUD / this.freeShippingThresholdAUD) * 100));

    // Social impact count: total items = total donations
    const totalDonations = this.items.reduce((sum, item) => sum + item.quantity, 0);

    return {
      itemCount: this.items.reduce((sum, item) => sum + item.quantity, 0),
      subtotalAUD,
      discountAmountAUD,
      finalSubtotalAUD,
      isFreeShipping,
      amountForFreeShippingAUD,
      shippingProgressPercent,
      totalDonations,
      activePromo: this.activePromo
    };
  }
}
