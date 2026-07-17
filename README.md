# Doç. Dr. Sema Koç - Yeni Site Tasarımı (Siyah / Beyaz / Gold)

Çok sayfalı statik önizleme sitesi. Onay sonrası tasarım, canlı drsemakoc.com'a (WordPress) taşınacaktır.

**Önizleme:** https://novavitamedia-lgtm.github.io/drsemakoc-yeni-site/

## Tasarım

- **Palet:** Siyah (#0B0B0C), beyaz (#FCFCFA) ve gold (#A8863D / #D6B879).
- **Tipografi:** Fraunces (başlıklar) + Figtree (gövde), gömülü woff2.
- **İkonlar:** [Solar Bold Duotone](https://icon-sets.iconify.design/solar/) (CC BY 4.0) + [Phosphor](https://phosphoricons.com) yedek (MIT), inline SVG.
- **Görseller:** Canlı drsemakoc.com'dan alınan gerçek klinik ve tedavi görselleri (optimize edilmiş).
- Açık/koyu tema, erişilebilirlik (focus-visible, reduced-motion), responsive.

## Sayfalar (15)

Ana sayfa, Hakkımızda, Sunulan Hizmetler, Blog, örnek blog yazısı, İletişim ve 9 tedavi sayfası:
Rinoplasti, Revizyon Burun Estetiği, Ultrasonik Piezo, Burun Ucu (Tipplasti), Septoplasti,
Horlama & Uyku Apnesi, Kulak & İşitme, Baş-Boyun, Vertigo.

Tedavi sayfası şablonu: breadcrumb → hero (gerçek görsel) → bilgi bölümleri → yan menü + randevu kartı → süreç adımları → SSS (accordion + FAQ JSON-LD) → CTA bandı.

## SEO: Sıfır Trafik Kaybı İlkesi

- **URL eşleme 1:1:** Önizlemedeki klasör yapısı canlı sitenin slug'larını birebir taklit eder
  (`/our-services/rhinoplasty/`, `/septoplasti/`, `/revizyon-burun-estetigi/` vb.).
  Canlıya geçişte URL değişikliği OLMAYACAK; tasarım mevcut WordPress URL'lerinin üzerine giydirilecek.
- **Title/H1 korunumu:** Canlı sayfaların anahtar kelime taşıyan title ve H1 yapıları korundu
  (ör. "Antalya Rinoplasti", "Antalya Horlama ve Uyku Apnesi Tedavisi").
- **Önizleme noindex:** Tüm sayfalarda `<meta name="robots" content="noindex, nofollow">` var;
  önizleme, canlı siteyle duplicate content oluşturmaz. Canlıya geçişte bu etiket KULLANILMAYACAK.
- **Schema:** Ana sayfada Physician, tedavi sayfalarında FAQPage JSON-LD.

## Mevzuat Uyumu (Sağlık Tanıtım Yönetmeliği)

- Övücü ve talep yaratıcı ifadeler ("en iyi", "kusursuz", "vaat ediyorum") kaldırıldı.
- Hasta yorumları, fiyat bilgisi ve "ücretsiz danışmanlık" ifadeleri kaldırıldı.
- Operasyon sayısı gibi üstünlük iması taşıyan rakamlar yerine akademik özgeçmiş kullanıldı.
- Tüm içerik bilgilendirme dilinde; her sayfada yasal uyarı mevcut.

## Yapı

```
index.html                  ana sayfa
<slug>/index.html           iç sayfalar (canlı slug'larla birebir)
assets/style.css            tek CSS (tema tokenları)
assets/main.js              nav + dropdown + reveal
assets/fonts/*.woff2        Fraunces + Figtree
assets/img/*.jpg            optimize gerçek görseller
```
