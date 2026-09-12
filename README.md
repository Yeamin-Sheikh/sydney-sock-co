# Sydney Sock Co

Ethical Australian Merino wool and organic bamboo sock eCommerce platform and subscription service, based in Surry Hills, Sydney NSW.

## Brand information

- Store: Sydney Sock Co
- Studio address: 42 Crown St, Surry Hills NSW 2010, Australia
- Phone: (02) 9358 1290
- Giving model: 1 pair purchased = 1 pair of warm socks or hot meal donated to Sydney homeless shelters
- Materials: 19.5-micron non-mulesed Australian Merino wool, organic bamboo fiber, combed cotton

## Complete site structure (6 full pages)

1. `index.html`: Home page featuring pastoral provenance, bestseller highlights, monthly sock club teaser, and shelter donation metrics.
2. `shop.html`: Complete catalog displaying all 6 signature sock styles with size selectors, live pricing, and cart integration.
3. `about.html`: Heritage narrative detailing non-mulesed wool sourcing, 200-needle circular knitting technology, shelter distribution vans, and the Surry Hills design studio.
4. `subscription.html`: Interactive monthly box builder with pair count selection (2, 3, 4 pairs), style themes, and previous edition previews.
5. `care-guide.html`: Comprehensive wool and bamboo longevity guide covering cold-water washing, eucalyptus detergent, inside-out laundry methods, and shade drying.
6. `contact.html`: Studio location, opening hours, interactive inquiry form, and operational gallery.

Every page contains at least 7 high-resolution content photographs, inlined SVG icons eliminating CORS issues when loaded locally or served over HTTP, an interactive slide-over cart drawer, multi-currency conversion, and custom context menus.

## Image assets

- `assets/images/hero.jpg`: Australian Merino wool and shelter giving distribution
- `assets/images/merino-farm.jpg`: Certified non-mulesed Merino sheep pasture in New South Wales
- `assets/images/knitting-mill.jpg`: Circular 200-needle precision knitting machinery
- `assets/images/subscription-box.jpg`: Kraft monthly sock subscription unboxing box
- `assets/images/sock-care.jpg`: Hand-washing basin and gentle wool care
- `assets/images/lifestyle-socks.jpg`: Everyday socks worn on Sydney streets
- `assets/images/koala-crew.jpg`: The Koala Canopy Crew organic bamboo socks
- `assets/images/sunset-merino.jpg`: Sydney Harbour Sunset Gradient fine Merino socks
- `assets/images/bondi-cushion.jpg`: Bondi Coastal Trail cushioned athletic socks
- `assets/images/roo-boot.jpg`: Red Earth Kangaroo heavy duty boot socks
- `assets/images/surry-hills.jpg`: Surry Hills Heritage Houndstooth executive socks
- `assets/images/cockatoo-ankle.jpg`: Sulphur-Crested Cockatoo ankle athletic socks

## Key features

- Multi-currency switcher: Live conversion across AUD, USD, EUR, and GBP
- Dynamic cart drawer: Tracks items, subtotal, and progress toward the $60 AUD free express shipping threshold
- Impact tracker: Counts shelter donations dynamically as items are added to the cart
- Inlined SVG sprites: Guaranteed zero-CORS icon rendering across all browsers and file protocols
- Shoe size modal: Cross-reference AU/UK, US Men, US Women, and EU sizing standards
- High-DPI support: Optimized for Windows scaling at 125% and 150%

## Project structure

```
sydney-sock-co/
├── assets/
│   ├── images/
│   │   ├── bondi-cushion.jpg
│   │   ├── cockatoo-ankle.jpg
│   │   ├── hero.jpg
│   │   ├── knitting-mill.jpg
│   │   ├── koala-crew.jpg
│   │   ├── lifestyle-socks.jpg
│   │   ├── merino-farm.jpg
│   │   ├── roo-boot.jpg
│   │   ├── sock-care.jpg
│   │   ├── subscription-box.jpg
│   │   ├── sunset-merino.jpg
│   │   └── surry-hills.jpg
│   └── svgs/
│       ├── icons.svg
│       └── logo.svg
├── css/
│   ├── components.css
│   └── main.css
├── js/
│   ├── app.js
│   ├── cart.js
│   ├── currency.js
│   ├── products.js
│   └── subscription.js
├── tests/
│   ├── runner.js
│   └── verify_pages.py
├── about.html
├── build_sydney_pages.py
├── care-guide.html
├── config.json
├── contact.html
├── index.html
├── package.json
├── README.md
├── shop.html
└── subscription.html
```

## Running locally

Serve the project with Python or Node:

```powershell
# Using Python
python -m http.server 8000

# Or using Node
npm start
```

Open `http://localhost:8000` in Google Chrome.

## Automated verification

Run the comprehensive test suites:

```powershell
# Run business logic tests
node tests/runner.js

# Verify all 6 pages have 6+ pictures and working inlined SVG icons
python tests/verify_pages.py
```

## License

MIT License.
