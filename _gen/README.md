# Site Üreteci

Tüm sayfalar `build_site.py` ile üretilir (statik jeneratör, tek bağımlılık: Python 3 + Pillow yalnızca görsel hazırlıkta).

- `build_site.py` — tüm sayfa şablonları ve içerik (tedaviler, LP'ler, diller)
- `style.css` / `main.js` — kaynak stiller ve script (assets/ altına kopyalanır)
- `reviews.json` — elden geçirilmiş 41 gerçek Google yorumu (etiketli)
- `icons_solar/` + `icons_ph/` — Solar Bold Duotone (öncelikli) + Phosphor (yedek) ikonlar

Not: script içindeki SCRATCH/BASE yolları üretim ortamına göre düzenlenmelidir; görsel kaynakları `../assets/img/` altında hazır durumdadır.
