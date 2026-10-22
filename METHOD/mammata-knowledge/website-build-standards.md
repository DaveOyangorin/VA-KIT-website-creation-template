> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

<!-- MAMMATA reference module — extracted verbatim from the agent definition 2026-06-11. The agent def mandates reading this file before the matching task. -->

## WEBSITE CREATION WITH SEO (2026 Standards)

When building websites, MAMMATA follows this SEO-first structure:

### Page Architecture
```
Homepage (brand + primary keyword + MedicalBusiness or Organization schema)
├── Services/Products (commercial keywords + Service schema + FAQPage)
│   ├── Service Page 1 (specific keyword + MedicalTherapy or Service schema)
│   └── Service Page 2 (specific keyword + MedicalTherapy or Service schema)
├── Blog/Resources (informational keywords)
│   ├── Pillar Page (broad topic — 3,000+ words)
│   └── Cluster Pages (specific subtopics — 1,200-2,000 words + MedicalWebPage schema)
├── About (E-E-A-T signals + Physician or Person schema with hasCredential)
├── Contact (LocalBusiness or MedicalBusiness schema)
└── Location Pages (local SEO — unique content per city, not templated)
```

### Every Page Must Have (2026 Minimum Standard)
1. Unique title tag — primary keyword first, 50-60 chars
2. Meta description — 150-160 chars
3. H1 — single intent, includes primary keyword
4. 800+ words of original, experience-based content (300+ for location pages)
5. At least 3 internal links with descriptive anchors
6. 2-3 outbound links to authoritative primary sources
7. Relevant schema markup (always)
8. Named author with credentials on all content pages
9. Optimized images with alt text and explicit dimensions
10. Fast load time — LCP < 2.5s on mobile
11. First paragraph directly answering the primary query

### Schema Templates (2026)

**Homepage — MedicalBusiness:**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalBusiness",
      "@id": "https://example.com/#medicalbusiness",
      "name": "Business Name",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png",
      "description": "...",
      "medicalSpecialty": "Musculoskeletal",
      "telephone": "+1-000-000-0000",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "...",
        "addressLocality": "City",
        "addressRegion": "State",
        "postalCode": "00000",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 00.0000,
        "longitude": -000.0000
      },
      "openingHoursSpecification": [...],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5.0",
        "reviewCount": "00",
        "bestRating": "5",
        "worstRating": "1"
      },
      "areaServed": [...],
      "sameAs": ["https://facebook.com/...", "https://linkedin.com/..."]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "name": "Business Name",
      "publisher": {"@id": "https://example.com/#medicalbusiness"}
    }
  ]
}
```

**Homepage — Standard Organization (non-medical):**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Business Name",
      "url": "https://example.com",
      "logo": "https://example.com/logo.png",
      "description": "...",
      "telephone": "+1-000-000-0000",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "...",
        "addressLocality": "City",
        "addressRegion": "State",
        "postalCode": "00000",
        "addressCountry": "US"
      },
      "sameAs": ["https://facebook.com/...", "https://linkedin.com/...", "https://twitter.com/..."]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "name": "Business Name",
      "publisher": {"@id": "https://example.com/#organization"},
      "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": "https://example.com/?s={search_term_string}"},
        "query-input": "required name=search_term_string"
      }
    }
  ]
}
```

**Author/About Page — Physician (medical) or Person (non-medical):**
```json
{
  "@context": "https://schema.org",
  "@type": "Physician",
  "@id": "https://example.com/about#physician",
  "name": "Dr. First Last",
  "honorificPrefix": "Dr.",
  "honorificSuffix": "DC",
  "jobTitle": "Chiropractic Physician",
  "description": "...",
  "url": "https://example.com/about",
  "image": "https://example.com/images/doctor.jpg",
  "worksFor": {"@id": "https://example.com/#medicalbusiness"},
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "credentialCategory": "certification",
      "name": "Certification Name",
      "recognizedBy": {"@type": "Organization", "name": "Issuing Organization"}
    }
  ],
  "knowsAbout": ["Topic 1", "Topic 2", "Topic 3"],
  "sameAs": ["https://linkedin.com/in/..."]
}
```

**Service Page:**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "name": "Service Name",
      "description": "...",
      "provider": {"@id": "https://example.com/#organization"},
      "areaServed": {"@type": "City", "name": "City Name"},
      "serviceType": "Service Category",
      "url": "https://example.com/services/service-name/"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Question text?",
          "acceptedAnswer": {"@type": "Answer", "text": "Answer text."}
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://example.com/services"},
        {"@type": "ListItem", "position": 3, "name": "Service Name", "item": "https://example.com/services/service-name/"}
      ]
    }
  ]
}
```

**Blog/Content Page — MedicalWebPage (health topics) or Article (general):**
```json
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "headline": "Article Title",
  "description": "Meta description.",
  "url": "https://example.com/blog/article-slug/",
  "datePublished": "2026-05-22",
  "dateModified": "2026-05-22",
  "author": {
    "@type": "Physician",
    "name": "Dr. First Last, DC",
    "@id": "https://example.com/about#physician"
  },
  "reviewedBy": {
    "@type": "Physician",
    "name": "Dr. First Last, DC",
    "@id": "https://example.com/about#physician"
  },
  "publisher": {"@id": "https://example.com/#medicalbusiness"},
  "image": "https://example.com/images/article-image.jpg",
  "medicalAudience": {"@type": "MedicalAudience", "audienceType": "Patient"},
  "about": {"@type": "MedicalCondition", "name": "Condition Name"},
  "specialty": {"@type": "MedicalSpecialty", "name": "Musculoskeletal"}
}
```
