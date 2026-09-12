/**
 * Multi-Currency Conversion Engine
 * Base currency is Australian Dollars (AUD)
 */
export class CurrencyManager {
  constructor(defaultCurrency = 'AUD') {
    this.currentCurrency = defaultCurrency;
    this.rates = {
      'AUD': { rate: 1.00, symbol: '$', code: 'AUD' },
      'USD': { rate: 0.66, symbol: '$', code: 'USD' },
      'EUR': { rate: 0.60, symbol: '€', code: 'EUR' },
      'GBP': { rate: 0.51, symbol: '£', code: 'GBP' }
    };
  }

  setCurrency(currencyCode) {
    if (this.rates[currencyCode]) {
      this.currentCurrency = currencyCode;
      return true;
    }
    return false;
  }

  convert(amountInAUD) {
    const info = this.rates[this.currentCurrency];
    const converted = amountInAUD * info.rate;
    return {
      amount: Math.round(converted * 100) / 100,
      formatted: `${info.symbol}${converted.toFixed(2)} ${info.code}`,
      symbol: info.symbol,
      code: info.code
    };
  }
}
