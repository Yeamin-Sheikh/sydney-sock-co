/**
 * Sydney Sock Subscription Box Engine
 */
export function calculateSubscriptionPlan({ pairCount = 3, theme = 'mixed', frequency = 'monthly' }) {
  const tiers = {
    2: { basePriceAUD: 32.00, discount: 10, label: 'The Explorer (2 Pairs)' },
    3: { basePriceAUD: 45.00, discount: 15, label: 'The Local Favorite (3 Pairs)' },
    4: { basePriceAUD: 56.00, discount: 20, label: 'The Aussie Collector (4 Pairs)' }
  };

  const selectedTier = tiers[pairCount] || tiers[3];
  const pricePerPairAUD = Math.round((selectedTier.basePriceAUD / pairCount) * 100) / 100;

  return {
    pairCount,
    tierName: selectedTier.label,
    priceAUD: selectedTier.basePriceAUD,
    pricePerPairAUD,
    discountPercent: selectedTier.discount,
    theme,
    frequency,
    impactDonations: pairCount
  };
}
