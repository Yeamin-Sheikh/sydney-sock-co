# Sydney Sock Co

An ethical fashion eCommerce website and subscription box service for **Sydney Sock Co**, an Australian sock brand located in Sydney, New South Wales.

## Brand information

- **Brand:** Sydney Sock Co
- **Location:** Surry Hills, Sydney, NSW 2010, Australia
- **Social impact:** 1-for-1 giveback program donating fresh warm socks and hot meals to Sydney homeless missions
- **Materials:** Non-mulesed Australian Merino wool (19.5 micron), certified organic bamboo fiber, and combed cotton

## Key features

- **Heritage catalog:** Signature sock designs with Australian botanical and wildlife themes (Koala Canopy, Bondi Trail, Kangaroo Boot, Sunset Merino).
- **Multi-currency support:** Live exchange rate toggling across AUD ($), USD ($), EUR (&euro;), and GBP (&pound;).
- **Interactive subscription builder:** Configure monthly sock packages (2, 3, or 4 pairs) with discounts up to 20%.
- **Impact tracker:** Real-time calculation of donated shelter meals and socks based on active cart contents.
- **Size guide converter:** Interactive modal comparing Australian, UK, US Men, US Women, and European shoe sizes.
- **Cart drawer and free shipping bar:** Tracks order progress toward the $60 AUD free shipping threshold across Australia.
- **Custom imagery and vector icons:** High-resolution product flat lay and Australian SVG sprites.
- **Responsive high-DPI scaling:** Designed for desktop 125% and 150% scaling, tablet, and mobile views.

## Project structure

```
sydney-sock-co/
├── assets/
│   ├── images/
│   │   ├── hero.jpg
│   │   ├── koala-crew.jpg
│   │   ├── sunset-merino.jpg
│   │   ├── bondi-cushion.jpg
│   │   ├── roo-boot.jpg
│   │   ├── surry-hills.jpg
│   │   └── cockatoo-ankle.jpg
│   └── svgs/
│       ├── logo.svg
│       └── icons.svg
├── css/
│   ├── main.css
│   └── components.css
├── js/
│   ├── app.js
│   ├── cart.js
│   ├── currency.js
│   ├── products.js
│   └── subscription.js
├── tests/
│   └── runner.js
├── config.json
├── index.html
├── package.json
└── README.md
```

## Running locally

Serve using Python or Node:

```powershell
# Using Python
python -m http.server 8000

# Or using Node
npm start
```

Visit `http://localhost:8000` in your web browser.

## Running tests

Run the automated test suite:

```powershell
npm test
# or
node tests/runner.js
```

## License

MIT License.
