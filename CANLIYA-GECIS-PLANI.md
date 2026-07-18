# drsemakoc.com Canlıya Geçiş Planı (v14 Tasarım + 9 LP)

> Durum: PLAN ONAY BEKLİYOR. "Başla" onayı gelene kadar canlı siteye hiçbir müdahale yapılmayacak.
> İlke: Organik trafik kaybı SIFIR. URL'ler değişmez, tasarım mevcut WordPress'in üzerine giydirilir.

## Mimari Karar: Nasıl Uygulanacak?

**Yöntem: Hibrit statik gömme** (staging projesinde kanıtlanmış yaklaşım)

1. **Global chrome:** Yeni tasarımın CSS + JS + header + footer + WhatsApp butonu, Code Snippets eklentisiyle `wp_head` / `wp_body_open` / `wp_footer` kancalarına enjekte edilir. Tek anahtarla açılır kapanır.
2. **Çekirdek 15 sayfa:** Mevcut WP sayfalarının gövdesi yerinde değiştirilir (aynı ID, aynı slug, aynı URL). WP revizyon sistemi = anında geri alma.
3. **9 LP:** `/lp/...` altında yeni sayfalar olarak eklenir, noindex kalır (Ads trafiği için).
4. **Blog ve kapsam dışı 20+ sayfa:** İçeriğe dokunulmaz; global chrome sayesinde yeni header/footer/tipografiyi otomatik alır. Sıralama sinyalleri aynen korunur.

Neden özel tema değil: PHP tema geliştirme daha uzun sürer, Elementor içerikleriyle çakışır; gömme yöntemi pixel-perfect, hızlı ve geri dönüşü dakikalar mertebesindedir.

## FAZ 0: Yedek ve Erişim (yayın gününden önce)

- [ ] cPanel tam hesap yedeği + 3 ayrı DB dump (tr `/`, en `/en`, ru `/ru`)
- [ ] WP admin doğrulama + Application Password oluşturma
- [ ] Tüm canlı sayfaların HTML snapshot'ı (wget mirror) → geçiş sonrası fark analizi bazı
- [ ] GSC: son 12 ay top queries + top pages CSV export (kıyas bazı)
- [ ] SEMrush + rank tracker pozisyon snapshot (ana keywordler: antalya rinoplasti, antalya kbb, antalya vertigo tedavisi, antalya işitme kaybı, horlama tedavisi antalya...)

## FAZ 1: Keşif ve Teknik Temizlik (yarım gün)

- [ ] WP sürüm / tema / eklenti envanteri
- [ ] **Rank Math + AIOSEO çift SEO eklentisi tespiti:** Hangisi title/meta/schema basıyor belirlenir; metalar export edilip TEK eklentiye indirilir (çift schema/meta basımı sıralama riski; geçişten önce ayrı adım olarak temizlenir)
- [ ] REST API ile sayfa ID ↔ slug haritası
- [ ] Mevcut title / meta description / H1 envanteri → **yeni tasarım eşleştirme tablosu** (neyin korunduğu, neyin iyileştirildiği satır satır; ONAYA sunulur)
- [ ] LiteSpeed cache davranışı + purge stratejisi
- [ ] 404 / redirect envanteri

## FAZ 2: Altyapı Kurulumu (canlıda görünmez)

- [ ] Assets yükleme: `/wp-content/uploads/yeni-tasarim/` altına css, js, font, görseller (hero videoları zaten `/hero/` altında canlı sunucuda)
- [ ] Code Snippets eklentisi kurulumu; chrome snippet'i PASİF olarak hazır
- [ ] 9 LP sayfası draft olarak oluşturulur (noindex meta hazır)
- [ ] Gizli bir test sayfasında chrome aktif edilip kontrol edilir

## FAZ 3: Yayına Alma (önerilen: gece 00:00-06:00 TR)

Sıra önemli:

1. **LP'ler publish** — indexte olmadıkları için SEO riski sıfır; Google Ads final URL'leri hemen `drsemakoc.com/lp/...` yapılabilir
2. **Chrome snippet aktif** — tüm site yeni header/footer/tipografiye geçer
3. **Çekirdek 15 sayfa gövde değişimi** — sayfa başına döngü: içerik değiştir → cache purge → görsel kontrol. Aynı URL, aynı ID
4. **Ana sayfa en son** (en kritik sayfa, en son ve en dikkatli)
5. LiteSpeed tam purge + masaüstü/mobil smoke test

## FAZ 4: SEO Doğrulama (yayın gecesi + ertesi gün)

- [ ] noindex kontrolü: çekirdek sayfalarda YOK, LP'lerde VAR (en kritik kontrol; önizlemedeki noindex'ler canlıya TAŞINMAZ)
- [ ] Title / meta / H1 diff → Faz 1 tablosuyla birebir karşılaştırma
- [ ] Schema testi (Physician + FAQPage) → Rich Results Test
- [ ] XML sitemap yenile + GSC'ye gönder; 15 çekirdek URL için URL Inspection + indexleme talebi
- [ ] Site içi kırık link taraması (0 olmalı)
- [ ] PageSpeed / Core Web Vitals ölçümü (mobil öncelikli)
- [ ] Dönüşüm testleri: tüm WhatsApp formları, tel linkleri, video autoplay (iOS dahil)

## FAZ 5: İzleme ve Rollback (2-4 hafta)

- İlk hafta günlük: GSC coverage, 404, pozisyonlar (rank tracker haftalık cron'a bağlanır)
- Müdahale eşikleri: bir keywordde -5..-10 pozisyon → içerik/iç link güçlendirme; sayfa bazlı sorun → WP revizyonundan eski gövdeye dönüş (dakikalar)
- **Tam rollback senaryosu:** chrome snippet kapat + gövde revizyonlarını geri al → eski site ≤1 saatte aynen geri gelir

## FAZ 6: EN / RU (+ UA kararı) — TR stabilledikten 1-2 hafta sonra

- Aynı yöntem `/en` ve `/ru` kurulumlarına uygulanır (ayrı WP kurulumları)
- UA (Ukraynaca) için yeni kurulum/dizin kararı ayrıca verilecek (çeviri kapsamı + hosting)

## Risk Tablosu

| Risk | Önlem |
|---|---|
| Çift SEO eklentisi çakışması | Faz 1'de tekilleştirme, meta export ile |
| Sayfa gövdesi ezme | WP revizyonları + Faz 0 HTML snapshot |
| LiteSpeed eski cache gösterimi | Agresif purge + cache-bypass testler |
| Önizleme noindex'inin canlıya sızması | Faz 4'te ilk kontrol maddesi |
| Geçiş anında ziyaretçi görmesi | Gece penceresi + sayfa başına <1 dk değişim |

## Zaman Planı

| Gün | İş |
|---|---|
| 1. gün | Faz 0 + Faz 1 (yedek, keşif, meta eşleştirme tablosu → ONAY) |
| 2. gün | Faz 2 kurulum + gece Faz 3 yayın |
| 3. gün | Faz 4 doğrulama + Ads final URL değişimi |
| +2-4 hafta | Faz 5 izleme → ardından Faz 6 EN/RU |

## Başlamadan Önce Kullanıcıdan Gerekenler

1. **"Başla" onayı**
2. Faz 1 sonunda çıkacak title/meta eşleştirme tablosuna onay
3. Yayın gecesi tercihi (hangi gece uygulanacak?)
4. Rank Math mi AIOSEO mu tercihi (tercih yoksa mevcut veriye göre öneri sunulur)
