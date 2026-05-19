#!/usr/bin/env python3
"""Generate standalone case study HTML pages from project definitions."""

import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "projects")

PROJECTS = [
    {
        "slug": "classneighbors",
        "title": "ClassNeighbors",
        "tagline": "K-12 EdTech SaaS — peer nomination, AI classroom insights, and district-wide reporting",
        "domain": "EdTech",
        "domain_class": "domain-edtech",
        "stack": ["Laravel 10", "PHP 8.1", "MySQL", "OpenAI GPT-4o", "Stripe", "Clever", "ClassLink OneRoster", "Google Classroom", "AWS S3"],
        "production_url": None,
        "overview": """ClassNeighbors is a multi-tenant K-12 SaaS platform that enables anonymous student peer-nomination voting, AI-powered classroom social analysis, and school-wide reporting for individual teachers, schools, and entire districts. The system replaces ad-hoc spreadsheets and manual observation with auditable, role-scoped workflows built for educators and administrators.""",
        "challenge": """Districts needed automated roster provisioning from existing SIS tools, tiered billing across teacher/school/district levels, and AI insights that respect FERPA-style data boundaries—without re-processing entire datasets on every student submission.""",
        "solution": """A Laravel service-layer architecture with Clever OAuth and ClassLink OneRoster v1.1 delta-sync provisions organizations, teachers, classes, and students with full audit logs. A custom RAG pipeline (chunking → text-embedding-3-small → vector store → GPT-4o Assistants API) powers stateful classroom conversations. Stripe Cashier handles tiered subscriptions; Google Classroom import and DomPDF/PhpSpreadsheet reporting round out the educator toolkit.""",
        "features": [
            "Anonymous peer-nomination voting with school and district roll-ups",
            "Clever OAuth + ClassLink OneRoster v1.1 automated roster delta-sync",
            "RAG pipeline with OpenAI embeddings and GPT-4o Assistants API",
            "Stripe tiered subscriptions (teacher / school / district)",
            "Google Classroom import and multi-format PDF/Excel reports",
            "5-role RBAC with tenant isolation",
        ],
        "technical": [
            ("Roster sync", "Full delta-sync of orgs, teachers, classes, students with audit trail and error recovery."),
            ("AI pipeline", "Document chunking, embedding-3-small vector store, multi-turn GPT-4o conversations."),
            ("Multi-tenancy", "Scoped data access per teacher, school, and district with service-layer authorization."),
            ("Billing", "Laravel Cashier subscription tiers, webhooks, and plan-gated feature flags."),
        ],
        "role": "Senior full-stack Laravel developer — system architecture, roster integrations, RAG pipeline, Stripe billing, and reporting modules.",
        "impact": "Delivered a production EdTech platform that scales from single classrooms to district deployments with automated provisioning and AI-driven insights.",
    },
    {
        "slug": "classpeers",
        "title": "ClassPeers",
        "tagline": "AI-powered classroom insights with Vue.js islands and automated behavioral reports",
        "domain": "EdTech",
        "domain_class": "domain-edtech",
        "stack": ["Laravel 10", "Vue.js", "MySQL", "OpenAI GPT-4o", "Stripe", "ClassLink OneRoster", "AWS S3"],
        "production_url": None,
        "overview": """ClassPeers is a parallel K-12 EdTech SaaS focused on AI-powered classroom insights. Vue.js component islands deliver interactive dashboards while Laravel handles roster sync, billing, and queued report generation at scale.""",
        "challenge": """Generating embeddings for entire schools on every nomination was cost-prohibitive and slow. The platform also needed six distinct report types delivered reliably via email without blocking web requests.""",
        "solution": """Built EmbeddingMeta—an incremental sync layer that pushes only changed class/student data to OpenAI vector stores. Six automated report types (seating preference, behavioral nominations, cross-class comparisons, and more) dispatch through queued jobs. ClassLink OneRoster v1.1 full tenant-to-student sync spans 95+ migrations with Clever OAuth and Stripe plans including coupons and trials.""",
        "features": [
            "Vue.js component islands for interactive classroom dashboards",
            "6 automated report types via queued email jobs",
            "EmbeddingMeta incremental AI sync (changed records only)",
            "ClassLink OneRoster v1.1 + Clever OAuth",
            "Stripe billing with tiers, coupons, and trial periods",
        ],
        "technical": [
            ("EmbeddingMeta", "Diff-based sync to vector stores—avoids redundant OpenAI calls per submission."),
            ("Queue architecture", "Report generation, email dispatch, and roster jobs on Laravel queues."),
            ("Frontend islands", "Vue components embedded in Blade for progressive enhancement."),
            ("Schema evolution", "95+ migrations supporting full roster hierarchy and sync states."),
        ],
        "role": "Full-stack developer — Vue islands, AI embedding optimization, ClassLink/Clever integrations, Stripe billing.",
        "impact": "Cut AI API costs significantly while delivering rich behavioral analytics and seating insights to educators automatically.",
    },
    {
        "slug": "storatax",
        "title": "StoraTax",
        "tagline": "Bilingual AI tax management SaaS for Canadian filers, gig workers, and accountants",
        "domain": "FinTech",
        "domain_class": "domain-fintech",
        "stack": ["Laravel 10", "PHP 8", "MySQL", "OpenAI GPT-4.1", "Stripe", "Apple IAP", "AWS S3", "QuickBooks Online"],
        "production_url": None,
        "overview": """StoraTax is a bilingual (EN/FR) multi-tenant SaaS for Canadian tax workflows—serving individual filers, Uber/Lyft gig workers (Quebec GST/QST), and accountants managing multiple client portfolios from a single dashboard.""",
        "challenge": """Receipt capture had to work across photos, PDFs, and mobile—with accurate Canadian tax breakdowns (GST/HST/PST/QST). Payments needed to route correctly on iOS (Apple IAP) vs web (Stripe) while staying CRA-compliant.""",
        "solution": """End-to-end AI OCR: uploads → GPT-4.1 Vision extracts merchant, totals, and tax lines → structured JSON auto-populates forms, with Tesseract as fallback. Platform-aware payment routing sends iOS users to Apple IAP and web users to Stripe Checkout in USD/CAD. Automated PDF/Excel reports cover T776, T1, and Quebec GST/QST requirements.""",
        "features": [
            "Bilingual EN/FR UI and document generation",
            "GPT-4.1 Vision receipt OCR with Tesseract fallback",
            "Apple IAP (iOS) and Stripe Checkout (web)",
            "Multi-currency USD/CAD support",
            "CRA-compliant T776, T1, and Quebec GST/QST exports",
            "Accountant multi-client portfolio management",
        ],
        "technical": [
            ("AI OCR pipeline", "Vision API → validated JSON schema → form auto-fill with human review hooks."),
            ("Payment routing", "User-agent and platform detection for IAP vs Stripe with shared entitlement layer."),
            ("Tax engine", "Province-aware GST/HST/PST/QST calculation and report templates."),
            ("QuickBooks", "Online integration for accountant workflow sync."),
        ],
        "role": "Lead architect — AI OCR pipeline, bilingual UX, platform billing, CRA report generation, QuickBooks integration.",
        "impact": "Digitized receipt-to-form workflows for Canadian compliance, reducing manual data entry for filers and accounting firms.",
    },
    {
        "slug": "kontalio",
        "title": "Kontalio",
        "tagline": "All-in-one multi-tenant SMB platform — HR, inventory, e-commerce, and AI documents",
        "domain": "B2B SaaS",
        "domain_class": "domain-b2b",
        "stack": ["Laravel 8", "PHP 8", "MySQL", "OpenAI GPT-4.1", "Stripe", "Laravel Sanctum", "REST API"],
        "production_url": None,
        "overview": """Kontalio consolidates HR/attendance, invoicing, multi-warehouse inventory, e-commerce, and AI document intelligence into one multi-tenant SMB SaaS spanning 25+ admin modules—replacing disconnected tools with a unified operations hub.""",
        "challenge": """SMBs needed granular permissions across many modules, a reliable quote-to-invoice pipeline, and a mobile app fed by a secure API—all without duplicating business logic.""",
        "solution": """GPT-4.1 Vision invoice OCR returns structured JSON for instant form auto-fill. A 5-role RBAC matrix grants per-module CRUD permissions. Quotation → Proforma → Invoice flows preserve line-item integrity. A Sanctum-powered REST API (34+ endpoints) powers the companion mobile app for auth, planning, attendance, check-in/out, and timetables.""",
        "features": [
            "25+ admin modules (HR, inventory, e-commerce, finance)",
            "GPT-4.1 Vision invoice OCR with JSON auto-fill",
            "5-role RBAC with per-module CRUD matrix",
            "Quotation → Proforma → Invoice pipeline",
            "34+ Sanctum API endpoints for mobile companion app",
        ],
        "technical": [
            ("Permission matrix", "JSON-driven module permissions evaluated in middleware and policies."),
            ("Service layer", "Shared business rules between web admin and mobile API controllers."),
            ("Document AI", "PDF/image upload → Vision extraction → validated DTO → Eloquent persistence."),
            ("Multi-warehouse", "Stock transfers, reservations, and order allocation across locations."),
        ],
        "role": "Full-stack Laravel developer — module architecture, AI OCR, RBAC design, mobile REST API.",
        "impact": "Unified SMB operations in one auditable platform with mobile workforce support.",
    },
    {
        "slug": "limiria",
        "title": "Limiria Distri",
        "tagline": "B2B/B2C e-commerce and inventory for a French specialty food distributor",
        "domain": "E-Commerce",
        "domain_class": "domain-ecommerce",
        "stack": ["Laravel 11", "PHP 8.2", "MySQL", "Stripe", "AWS SES", "DomPDF", "Maatwebsite Excel"],
        "production_url": None,
        "overview": """Limiria Distri is a full commercial lifecycle platform for a French specialty distributor—covering storefront, multi-warehouse inventory, financial documents, and real-time profit analytics in one Laravel application.""",
        "challenge": """Concurrent orders against shared stock caused overselling. Profit had to be computed consistently across catalog, orders, and invoices. Shipping rules varied by customer country.""",
        "solution": """A custom profit engine tracks margins across the product catalog, orders, and invoices. The SafeQuantityMutation Eloquent trait prevents race conditions on stock decrements. Country-aware IP-geolocation drives shipping rules. A 13-class notification system alerts staff and customers across order and fulfillment events.""",
        "features": [
            "B2B/B2C storefront with multi-warehouse inventory",
            "Real-time profit engine across catalog, orders, invoices",
            "SafeQuantityMutation trait for race-safe stock updates",
            "Country-aware IP-geolocation shipping",
            "13-class notification system",
            "DomPDF invoices and Maatwebsite Excel exports",
        ],
        "technical": [
            ("Profit engine", "Margin rules applied at catalog, order, and invoice stages with audit trail."),
            ("Concurrency", "DB-level locking and atomic quantity mutations on high-traffic SKUs."),
            ("Notifications", "Event-driven notification classes for order, stock, and fulfillment states."),
            ("Exports", "PDF and Excel generation for finance and operations teams."),
        ],
        "role": "Senior Laravel developer — profit engine, inventory safety, shipping logic, notification architecture.",
        "impact": "Real-time profit visibility and race-safe inventory for multi-warehouse French distribution.",
    },
    {
        "slug": "sparetrac",
        "title": "Sparetrac",
        "tagline": "B2B industrial spare parts — BOM-driven dynamic pricing in production",
        "domain": "B2B / Manufacturing",
        "domain_class": "domain-b2b",
        "stack": ["Laravel 9", "PHP 8", "MySQL", "Blade", "jQuery", "DomPDF"],
        "production_url": "https://order.sparetrac.com",
        "overview": """Sparetrac is a dual-portal B2B platform for industrial spare parts ordering. Raw-material price updates in INR/USD cascade through linked BOMs to catalog prices and customer carts in real time—eliminating manual repricing for procurement teams.""",
        "challenge": """Complex BOM hierarchies, multi-currency raw materials, and fine-grained staff permissions across 30+ modules required a pricing engine that stayed consistent from admin updates to customer checkout.""",
        "solution": """BOM-driven dynamic pricing recalculates catalog and cart line items when material costs change. Three-tier staff RBAC (Admin/Contributor/Viewer) uses 20+ JSON feature-key permissions. managed_by and contact_visibilities scope records across modules. Eight Excel/DomPDF export classes support operations reporting.""",
        "features": [
            "BOM-driven dynamic pricing (INR/USD raw materials → catalog → cart)",
            "Dual-portal B2B (staff admin + customer ordering)",
            "3-tier RBAC with 20+ JSON feature-key permissions",
            "managed_by + contact_visibilities scoping (30+ modules)",
            "8 Excel/DomPDF export classes",
        ],
        "technical": [
            ("Pricing cascade", "Observer-driven recalculation through BOM trees to active carts."),
            ("Permission keys", "Feature flags stored as JSON, evaluated in middleware per route/action."),
            ("Data scoping", "managed_by and visibility pivots limit CRM and order data per user."),
            ("Exports", "Maatwebsite and DomPDF classes for orders, BOMs, and inventory reports."),
        ],
        "role": "Full-stack developer — pricing engine, RBAC matrix, export pipelines, dual-portal UX.",
        "impact": "Live BOM-linked pricing on order.sparetrac.com—production system for industrial B2B buyers.",
    },
    {
        "slug": "3pl-portal",
        "title": "3PL Customer Portal",
        "tagline": "Multi-tenant logistics — inbound, outbound, warehouse stock, and idempotent billing",
        "domain": "Logistics",
        "domain_class": "domain-logistics",
        "stack": ["Laravel 12", "PHP 8.2", "MySQL", "Stripe Checkout", "DomPDF", "Bootstrap 5"],
        "production_url": None,
        "overview": """A multi-tenant logistics platform for 3PL operations: inbound receiving (local and China multi-leg shipments), single and bulk outbound fulfillment with label PDFs, and warehouse stock tracking including CBM measurements.""",
        "challenge": """Billing had to be idempotent across six charge types, with invoices that flow through PDF generation, email, Stripe Checkout, webhook confirmation, and overdue cron—without duplicate charges on retries.""",
        "solution": """An idempotent billing ledger records charges with unique keys per operation type. Full invoice lifecycle: DomPDF generation → email delivery → Stripe Checkout link → webhook marks paid → scheduled overdue processing. Multi-tenant isolation separates 3PL customers and warehouse operators.""",
        "features": [
            "Inbound receiving (local + China multi-leg)",
            "Single/bulk outbound with shipping label PDFs",
            "Warehouse stock with CBM tracking",
            "Idempotent billing ledger (6 charge types)",
            "Invoice → email → Stripe Checkout → webhook → overdue cron",
        ],
        "technical": [
            ("Idempotent ledger", "Unique idempotency keys per charge; safe retries on queue failures."),
            ("Fulfillment", "Bulk outbound batching with label generation and tracking numbers."),
            ("Stripe lifecycle", "Checkout sessions, webhooks, and reconciliation against ledger entries."),
            ("Multi-tenancy", "Tenant-scoped warehouses, customers, and billing accounts."),
        ],
        "role": "Senior Laravel developer — billing ledger, fulfillment workflows, Stripe integration, multi-tenant architecture.",
        "impact": "Replaced spreadsheet-based 3PL billing with auditable, idempotent charge tracking and automated collections.",
    },
    {
        "slug": "usst",
        "title": "USST Verification Platform",
        "tagline": "Industrial safety certification, QR verification, and geolocation analytics",
        "domain": "Compliance / Industrial",
        "domain_class": "domain-logistics",
        "stack": ["Laravel 10", "PHP 8.1", "MySQL", "Google Maps API", "Maatwebsite Excel", "DomPDF"],
        "production_url": None,
        "overview": """Compliance platform built for US ServTech: public certificate verification via QR deep links, dynamic per-category MySQL schema management, work-order job tracking, and inspection checklist workflows for field technicians.""",
        "challenge": """Different equipment categories required different data fields—static schemas would not scale. Field inspections needed GPS analytics without storing redundant points.""",
        "solution": """Dynamic schema management creates category-specific tables/columns at runtime with migration safety. Geolocation pipeline: browser GPS → Haversine deduplication (500 m) → 100 m cluster grouping → Google Maps visualization with OSM Nominatim reverse geocoding for readable addresses.""",
        "features": [
            "Public certificate verification via QR deep links",
            "Dynamic per-category MySQL schema management",
            "Work-order tracking and inspection checklists",
            "GPS → Haversine dedup → cluster → Maps visualization",
            "OSM Nominatim reverse geocoding",
        ],
        "technical": [
            ("Dynamic schema", "Category-driven field definitions with admin UI and safe migrations."),
            ("Geo pipeline", "Client GPS batches, server-side dedup and clustering before map render."),
            ("QR verification", "Signed deep links to public certificate status pages."),
            ("Reporting", "DomPDF certificates and Maatwebsite Excel compliance exports."),
        ],
        "role": "Full-stack developer — dynamic schema engine, compliance workflows, geolocation analytics.",
        "impact": "Field-verifiable certificates and map-based inspection analytics for industrial safety compliance.",
    },
    {
        "slug": "dpms",
        "title": "Design Production Management System",
        "tagline": "Multi-portal design ops — workflows, credits, FCFS marketplace, designer payroll",
        "domain": "Operations / HR",
        "domain_class": "domain-b2b",
        "stack": ["Laravel 12", "PHP 8.2", "MySQL", "Blade", "Bootstrap 5", "Spatie RBAC"],
        "production_url": None,
        "overview": """DPMS is a multi-portal design production platform managing the full lifecycle from client requests through designer assignment, revisions, credits, and automated payroll in PKR.""",
        "challenge": """Urgent jobs needed fair first-come-first-served assignment without double-booking designers. Credits, revision overages, and monthly payroll had to stay atomic under concurrent load.""",
        "solution": """12-state request workflow with two-stage Complete Listings pipeline and workload-based auto-assignment. Urgent FCFS marketplace uses database row locking. Centralized credit engine applies priority multipliers with atomic ledger entries. Designer payroll runs on schedule: credit-payout, tiered KPI bonuses, monthly generation via Laravel Scheduler.""",
        "features": [
            "12-state request workflow + two-stage Complete Listings",
            "Workload-based auto-assignment",
            "Urgent FCFS marketplace with DB row locking",
            "Credit engine (priority multipliers, atomic ledger, revision overages)",
            "Designer payroll automation (PKR, KPI bonuses, monthly cron)",
        ],
        "technical": [
            ("Workflow engine", "State machine with guards, transitions, and audit log per request."),
            ("Row locking", "SELECT FOR UPDATE on marketplace picks to prevent double assignment."),
            ("Credit ledger", "Atomic debit/credit with revision overage rules and priority multipliers."),
            ("Spatie RBAC", "Roles and permissions across client, designer, and admin portals."),
        ],
        "role": "Senior Laravel developer — workflow engine, credit ledger, marketplace locking, payroll automation.",
        "impact": "Automated design-ops assignment and payroll replaced manual coordination spreadsheets.",
    },
    {
        "slug": "mrmechanic",
        "title": "MR. Mechanic",
        "tagline": "On-demand automotive marketplace API — ~100 endpoints for Pakistan",
        "domain": "Marketplace / Mobile",
        "domain_class": "domain-ecommerce",
        "stack": ["Laravel 12", "PHP 8.2", "MySQL", "Laravel Sanctum", "Firebase FCM", "Laravel Breeze"],
        "production_url": None,
        "overview": """MR. Mechanic is the production backend for an on-demand automotive marketplace in Pakistan—connecting drivers with mechanics through geo-tagged service requests, bidding, job lifecycle management, and real-time proximity notifications.""",
        "challenge": """Mechanics needed instant alerts within 10 km without exceeding FCM batch limits. The API required strict validation, OTP rate limiting, and a consistent JSON envelope across ~100 endpoints for mobile clients.""",
        "solution": """Firebase FCM with queued Haversine proximity matching notifies approved mechanics within 10 km (500-token batches, 3 retries). Multi-step KYC onboarding gates marketplace access. Distance-based PKR pricing engine. 14 PHP enums, 41 Form Request validators, OTP rate limiting, and ApexCharts admin analytics.""",
        "features": [
            "~100 REST API endpoints (Sanctum-authenticated)",
            "Geo-tagged requests, mechanic bidding, job lifecycle",
            "Offline payment confirmation, dual ratings, disputes",
            "FCM proximity alerts (10 km, 500-token batches, 3 retries)",
            "Multi-step KYC and distance-based PKR pricing",
        ],
        "technical": [
            ("API design", "Standardized JSON envelope, resource transformers, and Form Request validation."),
            ("Proximity queue", "Haversine query → chunked FCM dispatch with retry and dead-letter handling."),
            ("KYC workflow", "Document upload, admin review states, and mechanic approval gates."),
            ("Admin analytics", "ApexCharts dashboards for jobs, revenue, and mechanic performance."),
        ],
        "role": "Backend lead — API architecture, FCM matching, KYC flows, pricing engine, admin dashboard.",
        "impact": "Production marketplace backend enabling real-time mechanic matching for on-demand automotive services.",
    },
    {
        "slug": "invoice-scraper",
        "title": "Invoice Scraper",
        "tagline": "AI invoice capture SaaS + Chrome MV3 extension — email and web pipelines",
        "domain": "FinTech / AI",
        "domain_class": "domain-fintech",
        "stack": ["Laravel 11", "PHP 8.3", "MySQL", "GPT-4o", "Chrome MV3", "Sanctum", "Google/Microsoft OAuth"],
        "production_url": None,
        "overview": """Invoice Scraper captures invoices from IMAP/OAuth email inboxes and from any website via a Chrome Manifest V3 extension—both pipelines converge on a shared GPT-4o extraction API for consistent structured output.""",
        "challenge": """Duplicate invoices from email forwards and re-scraped pages needed reliable deduplication. Extraction had to work across 15+ languages with 25+ fields per document.""",
        "solution": """GPT-4o Vision and text modes return 25+ structured fields. Two-layer deduplication: SHA-256 content hash plus semantic invoice_number/vendor matching. Cascade lifecycle cleanup keeps email, extension, and SaaS records in sync. Google and Microsoft OAuth for inbox access.""",
        "features": [
            "IMAP/OAuth email inbox ingestion",
            "Chrome MV3 extension for any-website capture",
            "Shared GPT-4o extraction API (Vision + text)",
            "25+ fields, 15+ languages",
            "SHA-256 + semantic deduplication",
        ],
        "technical": [
            ("Extension ↔ API", "Sanctum tokens, CORS-safe upload, and shared extraction endpoint."),
            ("Deduplication", "Content hash first, then fuzzy match on vendor + invoice number."),
            ("OAuth inboxes", "Google/Microsoft token refresh and scoped mailbox polling."),
            ("Lifecycle", "Cascade delete/archive across extension events and SaaS records."),
        ],
        "role": "Full-stack developer — extraction API, Chrome extension integration, deduplication, OAuth mail pipelines.",
        "impact": "Unified multilingual invoice intake from email and web with production-grade deduplication.",
    },
    {
        "slug": "parade-deck",
        "title": "Parade Deck",
        "tagline": "Military veteran creator economy — events, billing, and 15+ integrations",
        "domain": "SaaS / Community",
        "domain_class": "domain-b2b",
        "stack": ["Laravel 8", "PHP 8", "MySQL", "Stripe", "PayPal", "Twilio", "WATI", "Zoom", "YouTube API", "ID.me"],
        "production_url": None,
        "overview": """Parade Deck is a full-stack SaaS for military podcast creators—covering event lifecycle (booking → QR check-in), dual payment providers, awards voting, networking directory, and in-app messaging with veteran verification.""",
        "challenge": """Creators needed one platform for events, monetization, and community—with reliable reminders across SMS, WhatsApp, email, Zoom, and YouTube without manual sync.""",
        "solution": """Stripe Cashier and PayPal for billing. Event lifecycle with QR check-in. ID.me military verification. Integrations: Twilio SMS, WATI WhatsApp, Brevo/SendGrid, HubSpot CRM, Google Calendar, Zoom OAuth, YouTube Data API v3, TikTok OAuth. Six scheduled cron workflows, database-backed async queue, and 10 Excel export classes.""",
        "features": [
            "Event lifecycle: booking → reminders → QR check-in",
            "Stripe Cashier + PayPal billing",
            "Awards voting and networking directory",
            "In-app messaging between creators and members",
            "ID.me military verification",
            "15+ third-party API integrations",
        ],
        "technical": [
            ("Integration hub", "Service classes per provider with token refresh and webhook handlers."),
            ("Cron workflows", "Event reminders, Zoom alerts, YouTube sync, and digest emails on Scheduler."),
            ("Queue system", "Database-backed jobs for SMS, email, and CRM sync with failure retries."),
            ("Exports", "10 Maatwebsite Excel classes for events, members, and revenue reporting."),
        ],
        "role": "Full-stack Laravel developer — integrations, billing, event automation, messaging, veteran verification.",
        "impact": "All-in-one creator platform for the military podcast community with verified onboarding and automated event ops.",
    },
]


def esc(s):
    return html.escape(str(s), quote=True)


def tag_html(tags, domain_class=""):
    return "".join(f'<span class="tag {domain_class}">{esc(t)}</span>' for t in tags)


def list_html(items):
    return "".join(f"<li>{esc(i)}</li>" for i in items)


def tech_html(items):
    return "".join(
        f'<div class="cs-tech-item"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t, d in items
    )


def render_project(p, all_slugs):
    idx = all_slugs.index(p["slug"])
    prev_slug = all_slugs[idx - 1] if idx > 0 else None
    next_slug = all_slugs[idx + 1] if idx < len(all_slugs) - 1 else None

    prod = ""
    if p.get("production_url"):
        prod = f'<p class="cs-production"><i class="fas fa-link"></i> Production: <a href="{esc(p["production_url"])}" target="_blank" rel="noopener">{esc(p["production_url"])}</a></p>'

    prev_link = (
        f'<a href="{prev_slug}.html" class="btn cs-nav-btn">← {esc(PROJECTS[idx-1]["title"])}</a>'
        if prev_slug
        else '<span></span>'
    )
    next_link = (
        f'<a href="{next_slug}.html" class="btn cs-nav-btn">{esc(PROJECTS[idx+1]["title"])} →</a>'
        if next_slug
        else '<span></span>'
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d1117">
  <meta name="description" content="{esc(p["tagline"])} — Case study by Aleem Zada.">
  <title>{esc(p["title"])} — Case Study | Aleem Zada</title>
  <link rel="stylesheet" href="../css/plugins/font-awesome.min.css">
  <link rel="stylesheet" href="../css/developer-portfolio.css">
</head>
<body class="case-study-page">
  <header class="site-header">
    <div class="container container-wide">
      <a href="../index.html" class="logo"><img class="logo-img" src="../img/aleem.png" alt="" width="32" height="32"><span>aleemxada</span></a>
      <button class="nav-toggle" type="button" aria-label="Menu">☰</button>
      <nav class="nav-links">
        <a href="../index.html">Home</a>
        <a href="../index.html#projects">Projects</a>
        <a href="../files/Aleem_Zada_Resume.docx" class="btn btn-primary" download><i class="fas fa-download"></i> Resume</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="cs-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../index.html">Portfolio</a>
          <span>/</span>
          <a href="../index.html#projects">Projects</a>
          <span>/</span>
          <span>{esc(p["title"])}</span>
        </nav>
        <span class="tag {esc(p.get("domain_class", ""))}">{esc(p["domain"])}</span>
        <h1>{esc(p["title"])}</h1>
        <p class="cs-tagline">{esc(p["tagline"])}</p>
        {prod}
        <div class="cs-stack">{tag_html(p["stack"], p.get("domain_class", ""))}</div>
      </div>
    </section>

    <section class="cs-body">
      <div class="container cs-layout">
        <article class="cs-main">
          <div class="cs-box">
            <h2><span class="cs-hash">#</span> Overview</h2>
            <p>{esc(p["overview"])}</p>
          </div>

          <div class="cs-box">
            <h2><span class="cs-hash">#</span> The challenge</h2>
            <p>{esc(p["challenge"])}</p>
          </div>

          <div class="cs-box">
            <h2><span class="cs-hash">#</span> Solution</h2>
            <p>{esc(p["solution"])}</p>
          </div>

          <div class="cs-box">
            <h2><span class="cs-hash">#</span> Key features</h2>
            <ul class="cs-check-list">{list_html(p["features"])}</ul>
          </div>

          <div class="cs-box">
            <h2><span class="cs-hash">#</span> Technical highlights</h2>
            <div class="cs-tech-grid">{tech_html(p["technical"])}</div>
          </div>

          <div class="cs-box cs-highlight-box">
            <h2><span class="cs-hash">#</span> Impact</h2>
            <p class="cs-impact">{esc(p["impact"])}</p>
          </div>
        </article>

        <aside class="cs-sidebar">
          <div class="cs-sidebar-card">
            <h3>My role</h3>
            <p>{esc(p["role"])}</p>
          </div>
          <div class="cs-sidebar-card">
            <h3>Tech stack</h3>
            <ul class="cs-sidebar-stack">{list_html(p["stack"])}</ul>
          </div>
          <div class="cs-sidebar-card">
            <h3>Links</h3>
            <p><a href="../index.html#projects">All projects</a></p>
            <p><a href="../files/Aleem_Zada_Resume.docx" download>Download resume</a></p>
            <p><a href="mailto:aleemdeveloper@gmail.com">Contact Aleem</a></p>
          </div>
        </aside>
      </div>
    </section>

    <section class="cs-nav-section">
      <div class="container cs-nav-row">
        {prev_link}
        <a href="../index.html#projects" class="btn btn-accent">All case studies</a>
        {next_link}
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>© 2025 Aleem Zada · <a href="../index.html">Portfolio</a></p>
    </div>
  </footer>
  <script src="../js/portfolio.js"></script>
</body>
</html>
"""


def main():
    slugs = [p["slug"] for p in PROJECTS]
    os.makedirs(OUT_DIR, exist_ok=True)
    for p in PROJECTS:
        content = render_project(p, slugs)
        content = content.replace("<div ", "<div ").replace("</div>", "</div>")
        content = content.replace("</div>", "</div>")
        path = os.path.join(OUT_DIR, f"{p['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Wrote", path)
    print(f"Generated {len(PROJECTS)} case study pages.")


if __name__ == "__main__":
    main()
