import assert from 'node:assert';
import { socksData } from '../js/products.js';
import { CurrencyManager } from '../js/currency.js';
import { SockCartManager } from '../js/cart.js';
import { calculateSubscriptionPlan } from '../js/subscription.js';

console.log('--- Running Sydney Sock Co Tests ---');

// Mock localStorage
global.localStorage = (() => {
  let store = {};
  return {
    getItem: (key) => store[key] || null,
    setItem: (key, value) => { store[key] = value.toString(); },
    removeItem: (key) => { delete store[key]; },
    clear: () => { store = {}; }
  };
})();

// Test 1: Product catalog integrity and image assets
assert.strictEqual(socksData.length, 6, 'Should have 6 sock products');
const koala = socksData.find(s => s.id === 'syd-koala-crew');
assert.ok(koala);
assert.strictEqual(koala.basePriceAUD, 18.00);
socksData.forEach(s => {
  assert.ok(s.image, `Product ${s.id} must have an image property`);
  assert.ok(typeof s.image === 'string' && s.image.endsWith('.jpg'), `Product ${s.id} image must be a .jpg`);
});
console.log('✓ Product catalog and image assets verified');

// Test 2: Multi-currency conversion
const curr = new CurrencyManager();
const audPrice = curr.convert(100);
assert.strictEqual(audPrice.amount, 100);
assert.strictEqual(audPrice.code, 'AUD');

curr.setCurrency('USD');
const usdPrice = curr.convert(100);
assert.strictEqual(usdPrice.amount, 66);
assert.strictEqual(usdPrice.code, 'USD');

curr.setCurrency('GBP');
const gbpPrice = curr.convert(100);
assert.strictEqual(gbpPrice.amount, 51);
assert.strictEqual(gbpPrice.code, 'GBP');
console.log('✓ Multi-currency calculations verified');

// Test 3: Cart calculations & Social Impact
const cart = new SockCartManager('test_sydney_cart');
cart.clearCart();

cart.addItem(koala, 'M / L', 2); // 2 * 18 = 36 AUD
const sunset = socksData.find(s => s.id === 'syd-sunset-merino'); // 22.50 AUD
cart.addItem(sunset, 'S / M', 1);

let totals = cart.getTotals();
assert.strictEqual(totals.subtotalAUD, 58.50);
assert.strictEqual(totals.itemCount, 3);
assert.strictEqual(totals.totalDonations, 3, 'Should donate 3 items to shelters');
assert.strictEqual(totals.isFreeShipping, false, '58.50 is under 60.00 threshold');
assert.strictEqual(totals.amountForFreeShippingAUD, 1.50);

// Add another pair to pass threshold
cart.addItem(koala, 'M / L', 1); // +18 = 76.50 AUD
totals = cart.getTotals();
assert.strictEqual(totals.subtotalAUD, 76.50);
assert.strictEqual(totals.isFreeShipping, true, '76.50 qualifies for free shipping');
console.log('✓ Cart items, donation metrics, and free shipping progress verified');

// Test 4: Promo code SYDNEY10
const promo = cart.applyPromo('SYDNEY10');
assert.strictEqual(promo.success, true);
totals = cart.getTotals();
// 10% of 76.50 = 7.65
assert.strictEqual(totals.discountAmountAUD, 7.65);
assert.strictEqual(totals.finalSubtotalAUD, 68.85);
console.log('✓ Promo code SYDNEY10 verified');

// Test 5: Subscription Plan
const subPlan = calculateSubscriptionPlan({ pairCount: 3, theme: 'mixed', frequency: 'monthly' });
assert.strictEqual(subPlan.priceAUD, 45.00);
assert.strictEqual(subPlan.pricePerPairAUD, 15.00);
assert.strictEqual(subPlan.discountPercent, 15);
assert.strictEqual(subPlan.impactDonations, 3);
console.log('✓ Subscription plan builder verified');

console.log('\nAll Sydney Sock Co tests passed successfully! (5/5)');
