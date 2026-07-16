# Doç. Dr. Sema Koç - Yeni Site Tasarımı (Premium)

Tek dosyalık, tamamen kendi kendine yeten site tasarımı (`index.html`). Harici bağımlılık yoktur: fontlar, ikonlar ve görsel dosyanın içine gömülüdür.

## Tasarım Kararları

- **Renk paleti:** Kliniğin gerçek iç mekanından türetildi: antrasit-yeşil lake (`#16211C`), mermer fildişi (`#F5F1E9`), pirinç altın (`#A98A52` / `#C6A76C`).
- **Tipografi:** Fraunces (başlıklar) + Figtree (gövde), Google Fonts, dosyaya gömülü woff2.
- **İkonlar:** [Lucide](https://lucide.dev) (ISC lisansı, ücretsiz), inline SVG.
- **Tema:** Açık/koyu tema desteği (`prefers-color-scheme`).
- **Erişilebilirlik:** Semantik HTML, focus-visible, `prefers-reduced-motion` desteği.

## Mevzuat Uyumu (Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Yönetmeliği)

Eski tasarımdaki şu unsurlar bilgilendirme diline çevrildi veya kaldırıldı:

- "En iyi deneyim", "mükemmelliyetçi", "hayatınızın en güzel deneyimi" gibi övücü ve talep yaratıcı ifadeler kaldırıldı.
- Operasyon sayısı gibi üstünlük iması taşıyan rakamlar kaldırıldı; yerine doğrulanabilir akademik özgeçmiş bilgileri kullanıldı.
- Google yorumları (hasta değerlendirmeleri) bölümü kaldırıldı.
- "Rinoplasti Fiyatları" bölümü kaldırıldı (fiyat bilgisi paylaşımı yasak).
- "Estetik tatili", "ultra lüks araç", "en iyi oteller" söylemi, nötr bir "şehir dışından gelen hastalar için bilgilendirme" bölümüne dönüştürüldü.
- Tüm hizmet açıklamaları sonuç vaadi içermeyen, bilgilendirici dille yazıldı.
- Alt bilgiye yasal bilgilendirme uyarısı eklendi.

## Yayınlama

GitHub Pages: Settings → Pages → Deploy from branch → `main` / root.
