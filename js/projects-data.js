/* Project index data — full case studies are static HTML in /projects/ */
const PORTFOLIO_PROJECTS = {
  classneighbors: {
    slug: 'classneighbors',
    title: 'ClassNeighbors',
    tagline: 'K-12 EdTech SaaS — peer nomination, AI classroom insights, district reporting',
    excerpt: 'Multi-tenant K-12 platform with Clever/ClassLink roster sync, RAG-powered GPT-4o insights, and Stripe tiered billing.',
    domain: 'EdTech',
    stack: ['Laravel 10', 'PHP 8.1', 'MySQL', 'OpenAI GPT-4o', 'Stripe', 'Clever', 'ClassLink OneRoster', 'Google Classroom', 'AWS S3']
  },
  classpeers: {
    slug: 'classpeers',
    title: 'ClassPeers',
    tagline: 'AI-powered classroom insights with Vue.js islands and automated reports',
    excerpt: 'Vue.js component islands, 6 queued report types, and EmbeddingMeta incremental AI sync to cut OpenAI costs.',
    domain: 'EdTech',
    stack: ['Laravel 10', 'Vue.js', 'MySQL', 'OpenAI GPT-4o', 'Stripe', 'ClassLink OneRoster', 'AWS S3']
  },
  storatax: {
    slug: 'storatax',
    title: 'StoraTax',
    tagline: 'Bilingual AI tax management SaaS for Canadian filers and accountants',
    excerpt: 'EN/FR SaaS with GPT-4.1 Vision receipt OCR, Apple IAP / Stripe routing, and CRA-compliant tax exports.',
    domain: 'FinTech',
    stack: ['Laravel 10', 'PHP 8', 'MySQL', 'OpenAI GPT-4.1', 'Stripe', 'Apple IAP', 'AWS S3', 'QuickBooks Online']
  },
  kontalio: {
    slug: 'kontalio',
    title: 'Kontalio',
    tagline: 'Multi-tenant SMB platform — HR, inventory, e-commerce, AI document intelligence',
    excerpt: '25+ modules, GPT-4.1 invoice OCR, quote-to-invoice pipeline, and 34+ Sanctum API endpoints for mobile.',
    domain: 'B2B SaaS',
    stack: ['Laravel 8', 'PHP 8', 'MySQL', 'OpenAI GPT-4.1', 'Stripe', 'Laravel Sanctum', 'REST API']
  },
  limiria: {
    slug: 'limiria',
    title: 'Limiria Distri',
    tagline: 'B2B/B2C e-commerce and inventory for a French specialty distributor',
    excerpt: 'Storefront to profit analytics with race-safe inventory, custom margin engine, and 13 notification classes.',
    domain: 'E-Commerce',
    stack: ['Laravel 11', 'PHP 8.2', 'MySQL', 'Stripe', 'AWS SES', 'DomPDF', 'Maatwebsite Excel']
  },
  sparetrac: {
    slug: 'sparetrac',
    title: 'Sparetrac',
    tagline: 'B2B industrial spare parts — BOM-driven dynamic pricing',
    excerpt: 'Live BOM cascade pricing on order.sparetrac.com with 20+ permission keys across dual B2B portals.',
    domain: 'B2B / Manufacturing',
    stack: ['Laravel 9', 'PHP 8', 'MySQL', 'Blade', 'jQuery', 'DomPDF'],
    production_url: 'https://order.sparetrac.com'
  },
  '3pl-portal': {
    slug: '3pl-portal',
    title: '3PL Customer Portal',
    tagline: 'Multi-tenant logistics — inbound, outbound, warehouse stock, billing',
    excerpt: 'Idempotent billing ledger, China multi-leg inbound, label PDFs, and full Stripe invoice lifecycle.',
    domain: 'Logistics',
    stack: ['Laravel 12', 'PHP 8.2', 'MySQL', 'Stripe Checkout', 'DomPDF', 'Bootstrap 5']
  },
  usst: {
    slug: 'usst',
    title: 'USST Verification Platform',
    tagline: 'Industrial safety certification, QR verification, geolocation analytics',
    excerpt: 'QR certificate verification, dynamic per-category schemas, and GPS clustering on Google Maps.',
    domain: 'Compliance / Industrial',
    stack: ['Laravel 10', 'PHP 8.1', 'MySQL', 'Google Maps API', 'Maatwebsite Excel', 'DomPDF']
  },
  dpms: {
    slug: 'dpms',
    title: 'Design Production Management System',
    tagline: 'Multi-portal design production — workflows, credits, designer payroll',
    excerpt: '12-state workflows, FCFS marketplace with row locking, credit engine, and automated PKR payroll.',
    domain: 'Operations / HR',
    stack: ['Laravel 12', 'PHP 8.2', 'MySQL', 'Blade', 'Bootstrap 5', 'Spatie RBAC']
  },
  mrmechanic: {
    slug: 'mrmechanic',
    title: 'MR. Mechanic',
    tagline: 'On-demand automotive marketplace API for Pakistan',
    excerpt: '~100 Sanctum API endpoints, FCM proximity matching within 10 km, KYC, and distance-based PKR pricing.',
    domain: 'Marketplace / Mobile',
    stack: ['Laravel 12', 'PHP 8.2', 'MySQL', 'Laravel Sanctum', 'Firebase FCM', 'Laravel Breeze']
  },
  'invoice-scraper': {
    slug: 'invoice-scraper',
    title: 'Invoice Scraper',
    tagline: 'AI invoice capture SaaS + Chrome MV3 extension',
    excerpt: 'Email + Chrome extension pipelines converging on GPT-4o extraction with SHA-256 deduplication.',
    domain: 'FinTech / AI',
    stack: ['Laravel 11', 'PHP 8.3', 'MySQL', 'GPT-4o', 'Chrome MV3', 'Sanctum', 'Google/Microsoft OAuth']
  },
  'parade-deck': {
    slug: 'parade-deck',
    title: 'Parade Deck',
    tagline: 'Military veteran creator economy — events, billing, 15+ integrations',
    excerpt: 'Creator SaaS with ID.me verification, dual billing, QR events, and 15+ API integrations.',
    domain: 'SaaS / Community',
    stack: ['Laravel 8', 'PHP 8', 'MySQL', 'Stripe', 'PayPal', 'Twilio', 'WATI', 'Zoom', 'YouTube API', 'ID.me']
  }
};

const PROJECT_LIST = Object.values(PORTFOLIO_PROJECTS);
