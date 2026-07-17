# -*- coding: utf-8 -*-
"""Doç. Dr. Sema Koç — çok sayfalı statik önizleme sitesi üreteci.
Canlı drsemakoc.com slug yapısını birebir taklit eder (SEO geçiş haritası 1:1)."""
import os, re, json, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.dirname(BASE)
OUT = os.path.join(SCRATCH, 'site2')

def icon(name):
    path = f'{SCRATCH}/icons_solar/{name}.svg'
    if not os.path.exists(path):
        path = f'{SCRATCH}/icons_ph/{name}.svg'
    raw = open(path).read()
    raw = re.sub(r'\swidth="1em"|\sheight="1em"', '', raw)
    raw = re.sub(r'\s+', ' ', raw).strip()
    return raw.replace('<svg', '<svg class="ic" aria-hidden="true"', 1)

IC = {n[:-4]: icon(n[:-4]) for n in os.listdir(f'{SCRATCH}/icons_ph')}

MAPS_URL = 'https://www.google.com/maps/place/Do%C3%A7.+Dr.+Sema+Ko%C3%A7+KBB+ve+Ba%C5%9F+Boyun+Cerrahisi+Klini%C4%9Fi/@36.8536797,30.7500137,17z'
IG_URL = 'https://www.instagram.com/drsemakoc/'

REVIEWS = json.load(open(os.path.join(BASE, 'reviews.json')))

VIDEOS = [
 ('Ii-D1-M3rGU', 'Horlama ve Uyku Apnesi Hakkında Bilgilendirme'),
 ('NYPHTR8VnRU', 'Endoskopik Muayene Hakkında Bilgilendirme'),
 ('IiOLQFT3BPE', 'Gırtlak Kanserinin Görülme Sıklığı Nedir?'),
 ('82gZvB0gFUc', 'Apne Tedavisi Nasıl Yapılıyor?'),
 ('c_iYRugePQs', 'Kulak Burun ve Boğaz Sağlığı Üzerine'),
]

PHONE = '+90 543 913 65 95'
TEL = 'tel:+905439136595'
WA = 'https://wa.me/905439136595'
MAIL = 'info@drsemakoc.com'
ADDR = 'Tekelioğlu Cad. 1947. Sk. No: 29/3, Muratpaşa / Antalya'
MAPQ = 'https://maps.google.com/?q=Tekelio%C4%9Flu+Cad.+1947.+Sk.+No:29/3+Antalya'
MAPE = 'https://www.google.com/maps?q=Tekelio%C4%9Flu+Cad.+1947.+Sk.+No:29/3+Muratpa%C5%9Fa+Antalya&output=embed'

# ---------------- TEDAVİLER ----------------
T = [
 dict(slug='our-services/rhinoplasty/', nav='Rinoplasti (Burun Estetiği)', ic='scan-face', img='rinoplasti.jpg',
  title='Rinoplasti (Burun Estetiği) | Doç. Dr. Sema Koç, Antalya',
  meta='Antalya rinoplasti (burun estetiği): operasyonun kapsamı, uygunluk değerlendirmesi, piezo teknolojisi, süreç ve sık sorulan sorular hakkında bilgilendirme.',
  h1='Antalya Rinoplasti (Burun Estetiği)',
  lead='Rinoplasti, burnun yapısal ve işlevsel özelliklerinin cerrahi olarak değerlendirildiği ve düzenlendiği bir operasyondur. Uygunluk, muayene ve değerlendirme sonrasında hastayla birlikte karara bağlanır.',
  sections=[
   ('Rinoplasti Nedir?', 'p', ['Rinoplasti, burun şeklinin ve iç yapısının cerrahi olarak yeniden düzenlenmesidir. Operasyon yalnızca görünüme yönelik olabileceği gibi; septum deviasyonu, konka hipertrofisi gibi nefes almayı zorlaştıran durumların düzeltilmesini de kapsayabilir.',
     'Her burun yapısı farklıdır. Bu nedenle planlama, yüz yapısı, cilt kalınlığı, kıkırdak ve kemik yapısı ile solunum fonksiyonlarının birlikte değerlendirilmesiyle kişiye özel yapılır.']),
   ('Operasyonda Kullanılan Teknikler', 'p', ['Kliniğimizde ultrasonik (piezo) cihazlar dahil olmak üzere güncel cerrahi teknikler kullanılmaktadır. Piezo teknolojisi, kemik şekillendirmeyi ses dalgalarıyla yapar; çevre yumuşak dokunun korunmasına yardımcı olur.',
     'Kıkırdak desteği gereken durumlarda öncelik hastanın kendi burun dokusudur. Doku yetersizliği durumunda kulak veya kaburga kıkırdağı kullanımı muayene sırasında değerlendirilir ve hastayla birlikte planlanır.']),
   ('Kimler İçin Değerlendirilir?', 'ul', ['Burun şekli veya boyutundan kaynaklı yapısal düzeltme ihtiyacı olanlar',
     'Septum deviasyonu gibi nedenlerle nefes alma güçlüğü yaşayanlar',
     'Travma sonrası burun yapısında değişiklik oluşanlar',
     'Kemik ve kıkırdak gelişimini tamamlamış, genel sağlık durumu uygun kişiler']),
  ],
  faq=[
   ('Ameliyat öncesinde neler yapılır?', 'Ön görüşmede kullandığınız ilaçlar ve alışkanlıklarınız hakkında bilgi alınır. Genel anestezi öncesi standart testler yapılır ve anestezi uzmanının değerlendirmesi alınır. Kan sulandırıcı ilaç kullanımı varsa hekim kontrolünde düzenlenir.'),
   ('Hastanede kalış süresi ne kadardır?', 'Hastalar genellikle operasyon günü akşamı veya ertesi sabah taburcu edilir. Süre, operasyonun kapsamına ve hastanın genel durumuna göre hekim tarafından belirlenir.'),
   ('Kulaktan veya kaburgadan kıkırdak ne zaman kullanılır?', 'Öncelik her zaman burnun kendi kıkırdak ve kemik dokusudur. Önceki ameliyatlar, travma veya yapısal eksiklik nedeniyle doku yetersizse kulak veya kaburga kıkırdağı gündeme gelir. Karar, muayene bulgularına göre hastayla birlikte verilir.'),
   ('İyileşme süreci nasıl ilerler?', 'İlk haftalarda ödem ve hassasiyet görülebilir; kontrol muayeneleriyle süreç düzenli olarak takip edilir. İyileşme hızı kişiden kişiye farklılık gösterir.'),
  ]),
 dict(slug='revizyon-burun-estetigi/', nav='Revizyon Burun Estetiği', ic='wind', img='revizyon.jpg',
  title='Revizyon Burun Estetiği | Doç. Dr. Sema Koç, Antalya',
  meta='Revizyon burun estetiği: daha önce rinoplasti geçirmiş hastalarda ikinci operasyonun kapsamı, değerlendirme süreci ve sık sorulan sorular.',
  h1='Revizyon Burun Estetiği',
  lead='Revizyon burun estetiği, daha önce rinoplasti operasyonu geçirmiş hastalarda yapısal veya işlevsel sorunların yeniden değerlendirildiği ikincil bir operasyondur.',
  sections=[
   ('Revizyon Burun Estetiği Nedir?', 'p', ['Önceki operasyon sonrasında nefes alma güçlüğü, yapısal düzensizlik veya iyileşme sürecine bağlı değişiklikler ortaya çıkabilir. Revizyon operasyonu, bu durumların cerrahi olarak yeniden ele alınmasıdır.',
     'Revizyon cerrahisi, ilk operasyona göre daha ayrıntılı bir planlama gerektirir. Doku durumu, skar yapısı ve kıkırdak yeterliliği muayenede ayrıntılı olarak değerlendirilir.']),
   ('Değerlendirme Süreci', 'p', ['Revizyon kararından önce burnun iç ve dış yapısı muayene edilir; gerekirse görüntüleme yöntemlerinden yararlanılır. Önceki operasyonun üzerinden yeterli iyileşme süresi geçmiş olması beklenir; bu süre genellikle en az bir yıldır ve hekim tarafından kişiye göre belirlenir.']),
   ('Kimler İçin Değerlendirilir?', 'ul', ['Önceki rinoplasti sonrası nefes alma sorunu yaşayanlar',
     'Yapısal düzensizlik veya asimetri gelişen hastalar',
     'İyileşme süreci tamamlanmış ve genel sağlık durumu uygun kişiler']),
  ],
  faq=[
   ('Revizyon için ne kadar beklenmelidir?', 'Dokuların iyileşmesi ve sonucun oturması için önceki operasyondan sonra genellikle en az bir yıl beklenmesi önerilir. Kesin zamanlama muayene ile belirlenir.'),
   ('Revizyon ilk ameliyattan farklı mıdır?', 'Evet. Skar dokusu ve değişmiş anatomi nedeniyle planlama daha ayrıntılıdır; kıkırdak desteği için kulak veya kaburga kıkırdağı gerekebilir.'),
   ('Her hastaya revizyon uygulanabilir mi?', 'Hayır. Uygunluk; doku durumu, beklentiler ve genel sağlık durumu birlikte değerlendirilerek hekim tarafından belirlenir.'),
  ]),
 dict(slug='ultrasonik-piezo-burun-estetigi/', nav='Ultrasonik Piezo Burun Estetiği', ic='activity', img='piezo.jpg',
  title='Ultrasonik Piezo Burun Estetiği | Doç. Dr. Sema Koç, Antalya',
  meta='Ultrasonik piezo burun estetiği: yöntemin kapsamı, klasik tekniklerden farkları ve iyileşme sürecine dair bilgilendirme.',
  h1='Ultrasonik Piezo Burun Estetiği',
  lead='Piezo burun estetiği, kemik şekillendirmenin ultrasonik ses dalgalarıyla yapıldığı bir rinoplasti tekniğidir.',
  sections=[
   ('Piezo Tekniği Nedir?', 'p', ['Ultrasonik piezo cihazı, kemik dokusunu ses dalgaları ile keser ve şekillendirir. Yumuşak dokulara teması sınırlı olduğu için çevre dokunun korunmasına yardımcı olur.',
     'Teknik, özellikle kemik yapının hassas şekillendirilmesi gereken operasyonlarda tercih edilebilir. Hangi tekniğin kullanılacağı muayene bulgularına göre belirlenir.']),
   ('Yöntemin Özellikleri', 'ul', ['Kemik şekillendirmede yüksek hassasiyet sağlar',
     'Yumuşak dokuların korunmasına yardımcı olur',
     'Operasyon sonrası ödem ve morarmanın seyri kişiye göre değişmekle birlikte takip sürecinde düzenli olarak değerlendirilir']),
  ],
  faq=[
   ('Piezo tekniği her hastaya uygun mudur?', 'Teknik seçimi; burun yapısı, planlanan düzeltmenin kapsamı ve muayene bulgularına göre hekim tarafından yapılır.'),
   ('Klasik yöntemden farkı nedir?', 'Klasik yöntemde kemik şekillendirme mekanik aletlerle yapılırken, piezo tekniğinde ultrasonik ses dalgaları kullanılır ve yumuşak doku teması sınırlıdır.'),
   ('İyileşme süreci nasıl ilerler?', 'İyileşme süreci kişiden kişiye farklılık gösterir; kontrol muayeneleriyle düzenli olarak takip edilir.'),
  ]),
 dict(slug='burun-ucu-estetigi-tipplasti/', nav='Burun Ucu Estetiği (Tipplasti)', ic='scan-face', img='tipplasti.jpg',
  title='Burun Ucu Estetiği (Tipplasti) | Doç. Dr. Sema Koç, Antalya',
  meta='Burun ucu estetiği (tipplasti): yalnızca burun ucuna yönelik operasyonun kapsamı, kimler için değerlendirildiği ve süreç bilgilendirmesi.',
  h1='Burun Ucu Estetiği (Tipplasti)',
  lead='Tipplasti, burnun yalnızca uç kısmındaki kıkırdak yapının düzenlendiği, kemik müdahalesi içermeyen bir operasyondur.',
  sections=[
   ('Tipplasti Nedir?', 'p', ['Burun ucu estetiği; burun ucunun şekli, açısı veya genişliği ile ilgili düzenlemelerin yapıldığı sınırlı kapsamlı bir operasyondur. Kemik yapıya müdahale edilmediği için kapsamı klasik rinoplastiden daha dardır.',
     'Burun sırtında da düzeltme gereken durumlarda tipplasti yeterli olmayabilir; bu ayrım muayene sırasında yapılır.']),
   ('Kimler İçin Değerlendirilir?', 'ul', ['Burun sırtı düzgün olup yalnızca burun ucunda düzenleme ihtiyacı olanlar',
     'Burun ucu düşüklüğü veya genişliği olan hastalar',
     'Kıkırdak gelişimini tamamlamış, genel sağlık durumu uygun kişiler']),
  ],
  faq=[
   ('Tipplasti ile rinoplasti arasındaki fark nedir?', 'Tipplasti yalnızca burun ucu kıkırdaklarını kapsar; rinoplasti ise kemik yapı dahil burnun bütününü ele alır. Hangi operasyonun uygun olduğu muayene ile belirlenir.'),
   ('Operasyon ne kadar sürer?', 'Kapsama bağlı olarak değişmekle birlikte tipplasti genellikle klasik rinoplastiden daha kısa sürer. Ayrıntılar ön görüşmede paylaşılır.'),
   ('İyileşme süreci nasıldır?', 'Kemik müdahalesi olmadığı için iyileşme genellikle daha kısa seyreder; süreç kontrol muayeneleriyle takip edilir.'),
  ]),
 dict(slug='septoplasti/', nav='Septoplasti', ic='wind', img='septoplasti.jpg',
  title='Septoplasti (Burun Eğriliği Ameliyatı) | Doç. Dr. Sema Koç, Antalya',
  meta='Septoplasti: septum deviasyonuna bağlı nefes alma güçlüğünün cerrahi tedavisi, değerlendirme süreci ve sık sorulan sorular.',
  h1='Septoplasti: Burun Eğriliği Ameliyatı',
  lead='Septoplasti, burun içindeki septum adı verilen kıkırdak ve kemik yapıdaki eğriliklerin düzeltildiği, solunum fonksiyonuna yönelik bir operasyondur.',
  sections=[
   ('Septoplasti Nedir?', 'p', ['Septum, burun boşluğunu ikiye ayıran kıkırdak ve kemik yapıdır. Doğuştan veya travmaya bağlı eğrilikler (deviasyon), burun tıkanıklığına, ağızdan nefes almaya, horlamaya ve tekrarlayan sinüzite yol açabilir.',
     'Septoplasti bu eğriliğin düzeltilmesine yönelik bir operasyondur; amaç solunum yolunun açılmasıdır. Gerekli durumlarda konka küçültme gibi ek işlemlerle birlikte planlanabilir.']),
   ('Hangi Şikâyetlerde Değerlendirilir?', 'ul', ['Sürekli veya tek taraflı burun tıkanıklığı',
     'Ağızdan nefes alma ve buna bağlı ağız kuruluğu',
     'Horlama ve uyku kalitesinde bozulma',
     'Tekrarlayan sinüzit atakları']),
  ],
  faq=[
   ('Septoplasti burnun şeklini değiştirir mi?', 'Septoplasti solunum fonksiyonuna yöneliktir ve tek başına burun şeklini değiştirmez. Şekle yönelik düzenleme gerekiyorsa bu ayrıca değerlendirilir.'),
   ('Operasyon sonrası tampon kullanılır mı?', 'Güncel tekniklerde genellikle silikon splint veya eriyebilen materyaller kullanılır. Uygulama, operasyonun kapsamına göre hekim tarafından belirlenir.'),
   ('İyileşme süreci ne kadar sürer?', 'Hastaların çoğu kısa sürede günlük yaşama döner. Tam iyileşme kişiye göre değişir ve kontrol muayeneleriyle takip edilir.'),
  ]),
 dict(slug='our-services/snooring-sleep-apnea/', nav='Horlama ve Uyku Apnesi', ic='moon-star', img='horlama.jpg',
  title='Horlama ve Uyku Apnesi Tedavisi | Doç. Dr. Sema Koç, Antalya',
  meta='Antalya horlama ve uyku apnesi: belirtiler, tanı süreci, cerrahi ve cerrahi dışı tedavi seçenekleri hakkında bilgilendirme.',
  h1='Antalya Horlama ve Uyku Apnesi Tedavisi',
  lead='Horlama ve uyku apnesi, uyku sırasında solunum düzenini etkileyen ve yaşam kalitesini düşürebilen rahatsızlıklardır. Tanı ve tedavi süreci kliniğimizde planlanmaktadır.',
  sections=[
   ('Horlama ve Uyku Apnesi Nedir?', 'p', ['Horlama, uyku sırasında üst solunum yolundaki daralma nedeniyle oluşan sesli solunumdur. Uyku apnesi ise solunumun uyku sırasında tekrarlayıcı şekilde durması veya yüzeyselleşmesidir.',
     'Tedavi edilmeyen uyku apnesi; gündüz uykululuk, yorgunluk, dikkat sorunları ve kalp-damar sağlığı üzerinde olumsuz etkilerle ilişkili olabilir. Bu nedenle belirtilerin hekim tarafından değerlendirilmesi önemlidir.']),
   ('Tanı Süreci', 'p', ['Tanıda ayrıntılı KBB muayenesi ile üst solunum yolunun değerlendirilmesi esastır. Gerekli görüldüğünde uyku testi (polisomnografi) planlanır; apnenin varlığı ve şiddeti bu testle belirlenir.']),
   ('Tedavi Seçenekleri', 'ul', ['Yaşam tarzı düzenlemeleri: kilo kontrolü, uyku pozisyonu, alkol ve sedatif kullanımının gözden geçirilmesi',
     'Ağız içi araçlar ve pozitif havayolu basıncı (PAP) cihazları',
     'Burun tıkanıklığına yönelik cerrahi: septoplasti, konka küçültme',
     'Yumuşak damak ve dil köküne yönelik cerrahi yöntemler: uygunluk muayene ile belirlenir']),
  ],
  faq=[
   ('Her horlama uyku apnesi belirtisi midir?', 'Hayır. Ancak tanıklı solunum durması, gündüz aşırı uykululuk veya yorgunlukla birlikte olan horlamada apne açısından değerlendirme önerilir.'),
   ('Uyku testi ne zaman gerekir?', 'Muayene bulguları ve şikâyetler apne olasılığını düşündürüyorsa polisomnografi planlanır. Testin gerekliliğine hekim karar verir.'),
   ('Tedavi her hastada cerrahi midir?', 'Hayır. Tedavi; apnenin şiddetine, tıkanıklığın yerine ve hastanın genel durumuna göre planlanır. Cerrahi, uygun hastalarda seçeneklerden biridir.'),
  ]),
 dict(slug='our-services/ear-hearing-treatments/', nav='Kulak ve İşitme Cerrahisi', ic='ear', img='kulak.jpg',
  title='Kulak Hastalıkları ve İşitme Kaybı Tedavisi | Doç. Dr. Sema Koç, Antalya',
  meta='Antalya işitme kaybı ve kulak hastalıkları: işitme testleri, orta kulak hastalıkları, cerrahi ve klinik tedavi süreçleri hakkında bilgilendirme.',
  h1='Antalya İşitme Kaybı Tedavisi ve Kulak Hastalıkları',
  lead='İşitme; iletişim, sosyal yaşam ve güvenlik açısından temel bir duyudur. Kliniğimizde işitme kaybının ve kulak hastalıklarının tanı ve tedavi süreçleri planlanmaktadır.',
  sections=[
   ('İşitme Kaybı ve Nedenleri', 'p', ['İşitme kaybı; kulak kiri birikiminden orta kulak iltihaplarına, kulak zarı hasarından iç kulak ve yaşa bağlı değişikliklere kadar farklı nedenlerle ortaya çıkabilir. Doğru tedavi, kaybın tipinin ve nedeninin belirlenmesiyle mümkündür.',
     'Doç. Dr. Sema Koç, KBB uzmanlığının yanı sıra odyoloji alanında yüksek lisans derecesine sahiptir; işitme ve denge değerlendirmeleri bu birikimle yürütülmektedir.']),
   ('Tanı ve Değerlendirme', 'ul', ['Mikroskopik ve endoskopik kulak muayenesi',
     'İşitme testleri (odyometri) ve orta kulak basınç ölçümleri (timpanometri)',
     'Gerekli durumlarda görüntüleme yöntemleri']),
   ('Tedavi Alanları', 'ul', ['Orta kulak iltihapları ve kronik otit tedavisi',
     'Kulak zarı onarımı (timpanoplasti) ve orta kulak cerrahisi',
     'Kulak kireçlenmesi (otoskleroz) değerlendirmesi',
     'Çınlama (tinnitus) değerlendirme ve yönetimi']),
  ],
  faq=[
   ('İşitme kaybı her zaman kalıcı mıdır?', 'Hayır. Kulak kiri veya orta kulak sıvısı gibi nedenlere bağlı kayıplar tedaviyle düzelebilir. Kaybın tipi yapılan testlerle belirlenir.'),
   ('İşitme testi nasıl yapılır?', 'Odyometri, ses geçirmez kabinde farklı frekanslardaki sesleri duyma eşiğinizin ölçülmesidir; kısa sürer ve ağrısızdır.'),
   ('Kulak çınlaması tedavi edilebilir mi?', 'Çınlamanın altında yatan neden belirlenerek yönetim planı oluşturulur. Yaklaşım nedene göre kişiden kişiye farklılık gösterir.'),
  ]),
 dict(slug='our-services/head-neck-cancer/', nav='Baş ve Boyun Cerrahisi', ic='ribbon', img='bas-boyun.jpg',
  title='Baş ve Boyun Kanseri Tedavisi | Doç. Dr. Sema Koç, Antalya',
  meta='Antalya baş ve boyun kanseri: belirtiler, tanı süreci, cerrahi tedavi ve multidisipliner takip hakkında bilgilendirme.',
  h1='Antalya Baş ve Boyun Kanseri Tedavisi',
  lead='Baş-boyun kanserleri; gırtlak, dil, bademcik, tükürük bezleri ve boyun bölgesindeki dokularda gelişebilen tümörleri kapsar. Erken tanı, tedavi başarısında belirleyicidir.',
  sections=[
   ('Belirtiler ve Erken Tanı', 'p', ['Uzun süren ses kısıklığı, yutma güçlüğü, boyunda ele gelen şişlik, iyileşmeyen ağız içi yaralar ve tek taraflı kulak ağrısı gibi belirtiler baş-boyun bölgesi hastalıklarının habercisi olabilir.',
     'İki-üç haftadan uzun süren bu tür şikâyetlerde KBB muayenesi önerilir. Erken evrede tanı konulan hastalıklarda tedavi seçenekleri daha geniştir.']),
   ('Tanı ve Tedavi Yaklaşımı', 'p', ['Tanıda endoskopik muayene, görüntüleme yöntemleri ve gerekli durumlarda biyopsi kullanılır. Tedavi planı; tümörün yeri, evresi ve hastanın genel durumuna göre cerrahi, radyoterapi ve onkoloji ekipleriyle multidisipliner olarak oluşturulur.',
     'Doç. Dr. Sema Koç, 2012 yılında Da Vinci Transoral Robotik Cerrahi eğitimini tamamlamıştır; uygun vakalarda robotik cerrahi deneyimi değerlendirme sürecine katkı sağlar.']),
   ('Hangi Belirtilerde Muayene Önerilir?', 'ul', ['İki-üç haftadan uzun süren ses kısıklığı',
     'Boyunda ele gelen ve büyüyen şişlik',
     'Yutma güçlüğü veya yutarken ağrı',
     'İyileşmeyen ağız içi yara',
     'Nedeni açıklanamayan tek taraflı kulak ağrısı']),
  ],
  faq=[
   ('Boyundaki her şişlik kanser midir?', 'Hayır. Boyun şişliklerinin önemli bölümü iltihabi nedenlere bağlıdır. Ancak uzun süren veya büyüyen şişliklerin muayene ile değerlendirilmesi gerekir.'),
   ('Tanı nasıl konulur?', 'Endoskopik muayene ve görüntüleme sonrasında kesin tanı genellikle biyopsi ile konulur. Süreç hastayla birlikte planlanır.'),
   ('Tedavi nasıl planlanır?', 'Tedavi; hastalığın yeri ve evresine göre cerrahi, radyoterapi ve kemoterapi seçeneklerinin birlikte değerlendirildiği multidisipliner bir yaklaşımla planlanır.'),
  ]),
 dict(slug='our-services/antalya-vertigo-tedavisi/', nav='Vertigo (Baş Dönmesi)', ic='orbit', img='vertigo.jpg',
  title='Antalya Vertigo Tedavisi | Doç. Dr. Sema Koç',
  meta='Antalya vertigo tedavisi: baş dönmesinin nedenleri, tanı süreci, Epley ve Semont manevraları ile tedavi seçenekleri hakkında bilgilendirme.',
  h1='Antalya Vertigo (Baş Dönmesi) Tedavisi',
  lead='Vertigo; kişinin kendisinin veya çevresinin döndüğünü hissettiği bir denge bozukluğu belirtisidir. Nedeni belirlendiğinde çoğu vertigo tablosu tedavi edilebilir.',
  sections=[
   ('Vertigo Nedir, Neden Olur?', 'p', ['Vertigonun en sık nedenlerinden biri iç kulaktaki kristallerin yer değiştirmesiyle oluşan BPPV, yani kulak kristali kaymasıdır. Meniere hastalığı, vestibüler nörit ve migrenle ilişkili baş dönmeleri de sık görülen nedenler arasındadır.',
     'Tanıda ayrıntılı öykü, KBB ve denge muayenesi esastır. Doç. Dr. Sema Koç, odyoloji alanındaki yüksek lisans birikimiyle işitme ve denge testlerini birlikte değerlendirmektedir.']),
   ('Tedavi Seçenekleri', 'ul', ['Pozisyonel manevralar: BPPV tanısı konulan hastalarda Epley ve Semont manevraları uygulanır',
     'İlaç tedavisi: altta yatan nedene yönelik olarak hekim tarafından planlanır',
     'Vestibüler rehabilitasyon: denge sisteminin yeniden uyumunu destekleyen egzersiz programları',
     'Altta yatan hastalığın tedavisi: Meniere, migren gibi durumlarda nedene yönelik yaklaşım']),
  ],
  faq=[
   ('Kulak kristali kayması nedir?', 'İç kulaktaki kalsiyum karbonat kristallerinin yer değiştirmesiyle oluşan ve baş hareketleriyle tetiklenen kısa süreli baş dönmesidir. Tanı muayene ile konulur ve manevra tedavisi uygulanır.'),
   ('Epley manevrası nedir?', 'Yer değiştiren kristallerin baş ve gövde hareketleriyle ait oldukları bölgeye yönlendirilmesini amaçlayan, muayenehane koşullarında uygulanan bir tedavi yöntemidir.'),
   ('Vertigo tekrarlar mı?', 'Nedene bağlı olarak tekrarlayabilir. Düzenli takip ve nedene yönelik tedavi, atakların yönetiminde önemlidir.'),
  ]),
]

# blog yazıları
POSTS = [
 dict(img='blog-bas-donmesi.jpg', cat='Vertigo', date='7 Haziran 2026', t='Baş Dönmesi: Nedenleri, Belirtileri ve Tedavisi',
      d='Baş dönmesinin sık görülen nedenleri, eşlik eden belirtiler ve tanı sonrasında uygulanabilen tedavi yaklaşımları.',
      href='bas-donmesi-nedenleri-belirtileri-ve-tedavisi/', local=True),
 dict(img='blog-kristal.jpg', cat='Vertigo', date='6 Haziran 2026', t='Kulakta Kristal Kayması (BPPV)',
      d='İç kulaktaki kristallerin yer değiştirmesiyle ortaya çıkan pozisyonel baş dönmesi ve manevra tedavileri hakkında bilgiler.',
      href='https://drsemakoc.com/kristal-kaymasi/', local=False),
 dict(img='blog-otoplasti.jpg', cat='KBB', date='5 Haziran 2026', t='Kepçe Kulak Ameliyatı (Otoplasti)',
      d='Otoplasti operasyonunun kapsamı, uygulanış şekli ve iyileşme sürecine dair genel bilgilendirme.',
      href='https://drsemakoc.com/kepce-kulak-ameliyati-otoplasti/', local=False),
 dict(img='blog-ses.jpg', cat='KBB', date='31 Mayıs 2026', t='Ses Kısıklığı: Nedenleri ve Tedavi Seçenekleri',
      d='Ses kısıklığına yol açan durumlar, tanı yöntemleri ve tedavi seçenekleri üzerine bilgilendirme.',
      href='https://drsemakoc.com/antalya-ses-kisikligi-tedavisi/', local=False),
 dict(img='blog-geniz.jpg', cat='Geniz Eti', date='30 Mayıs 2026', t='Geniz Eti: Çocuklarda ve Yetişkinlerde Belirtiler',
      d='Geniz etinin işlevi, büyümesi durumunda görülen belirtiler ve değerlendirme süreci.',
      href='https://drsemakoc.com/antalya-geniz-eti-tedavisi-2/', local=False),
 dict(img='blog-apne.jpg', cat='Uyku', date='29 Mayıs 2026', t='Uyku Apnesi: Belirtiler ve Tedavi Yöntemleri',
      d='Uyku apnesinin belirtileri, tanı süreci ve tedavi seçenekleri hakkında genel bilgiler.',
      href='https://drsemakoc.com/antalya-uyku-apnesi-tedavisi/', local=False),
]

# ---------------- ORTAK PARÇALAR ----------------

def wa_form(title, konu, subject_select=False):
    opts = ''
    if subject_select:
        items = ['Genel Bilgi ve Randevu'] + [t['nav'] for t in T]
        opts = '<select name="konu" aria-label="Konu">' + ''.join(
            f'<option value="{o}"{" selected" if o == konu else ""}>{o}</option>' for o in items) + '</select>'
    return f'''<div class="lead-form">
  <div class="lf-head">{IC['message-circle']}<b>{title}</b></div>
  <p>Bilgilerinizi bırakın, görüşme WhatsApp üzerinden otomatik başlasın.</p>
  <form class="wa-form" data-konu="{konu}">
    <input name="ad" placeholder="Adınız Soyadınız" autocomplete="name" required>
    <input name="tel" type="tel" placeholder="Telefon Numaranız" autocomplete="tel" required>
    {opts}
    <button class="btn btn-gold" type="submit">{IC['send']} WhatsApp'tan Devam Et</button>
  </form>
</div>'''

LANGS = [('', 'Türkçe', 'TR'), ('en/', 'English', 'EN'), ('ru/', 'Русский', 'RU'), ('ua/', 'Українська', 'UA')]

def lang_menu(R, active='TR'):
    items = '\n'.join(
        f'<a href="{R}{path}"{" style=\'color: var(--brass-2);\'" if code == active else ""}>{label}</a>'
        for path, label, code in LANGS)
    return f'''<div class="dropdown lang-dd">
        <button type="button" aria-expanded="false" aria-haspopup="true" aria-label="Dil seçimi">{IC['globe']} {active} {IC['chevron-right']}</button>
        <div class="drop-menu">{items}</div>
      </div>'''

def head(R, title, meta):
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%230B0B0C'/%3E%3Ctext x='50' y='68' font-family='Georgia,serif' font-size='52' fill='%23D6B879' text-anchor='middle'%3ESK%3C/text%3E%3C/svg%3E">
<link rel="preload" href="{R}assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}assets/fonts/figtree-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}assets/style.css">
</head>
<body>'''

def header(R, active=''):
    drops = '\n'.join(f'<a href="{R}{t["slug"]}">{t["nav"]}</a>' for t in T)
    def cls(k): return ' class="active"' if k == active else ''
    return f'''<header class="site-head">
  <div class="wrap head-in">
    <a class="wordmark" href="{R}index.html" aria-label="Doç. Dr. Sema Koç, ana sayfa">
      <strong>Doç. Dr. Sema Koç</strong>
      <span>KBB ve Baş-Boyun Cerrahisi</span>
    </a>
    <nav class="site-nav" id="siteNav" aria-label="Ana menü">
      <a href="{R}index.html"{cls('home')}>Ana Sayfa</a>
      <a href="{R}about-us/"{cls('about')}>Hakkımızda</a>
      <div class="dropdown">
        <button type="button" aria-expanded="false" aria-haspopup="true">Tedaviler {IC['chevron-right']}</button>
        <div class="drop-menu">
          <div class="drop-label">Tedavi ve Uygulamalar</div>
          {drops}
          <a href="{R}sunulan-hizmetler/"><b>Tüm Hizmetler →</b></a>
        </div>
      </div>
      <a href="{R}blog/"{cls('blog')}>Blog</a>
      <a href="{R}contacts/"{cls('contact')}>İletişim</a>
      {lang_menu(R)}
    </nav>
    <div style="display:flex; align-items:center; gap:.7rem;">
      <a class="head-cta" href="{R}contacts/">{IC['phone']}<span>Randevu Talebi</span></a>
      <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" aria-label="Menüyü aç">{IC['menu']}</button>
    </div>
  </div>
</header>'''

def footer(R):
    tlinks = '\n'.join(f'<li><a href="{R}{t["slug"]}">{t["nav"]}</a></li>' for t in T[:5])
    return f'''<footer class="site-foot">
  <div class="wrap foot-in">
    <div class="foot-cols">
      <div>
        <a class="wordmark" href="{R}index.html"><strong>Doç. Dr. Sema Koç</strong><span>KBB ve Baş-Boyun Cerrahisi</span></a>
        <p>Rinoplasti, kulak burun boğaz hastalıkları, baş-boyun cerrahisi, vertigo ve odyoloji alanlarında tanı ve tedavi hizmetleri, Antalya.</p>
      </div>
      <div>
        <h4>Tedaviler</h4>
        <ul>{tlinks}<li><a href="{R}sunulan-hizmetler/">Tüm Hizmetler</a></li></ul>
      </div>
      <div>
        <h4>İletişim</h4>
        <ul>
          <li><a href="{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="{MAPQ}" target="_blank" rel="noopener">{ADDR}</a></li>
        </ul>
      </div>
    </div>
    <p class="disclaimer">{IC['shield-check']}<span>Bu sitede yer alan içerikler bilgilendirme amacıyla hazırlanmıştır. İçerikler hekim muayenesinin ve tıbbi tanının yerini tutmaz. Sitede anlatılan hiçbir tedavi yöntemini hekim kontrolü dışında uygulamayınız. Tanı ve tedavi için lütfen hekiminize başvurunuz.</span></p>
    <div class="foot-base">
      <span>© 2026 Doç. Dr. Sema Koç. Tüm hakları saklıdır.</span>
      <a href="#top">Başa Dön ↑</a>
    </div>
  </div>
</footer>
<a class="wa-cta" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp ile iletişime geçin">{IC['message-circle']}<span>WhatsApp</span></a>
<script src="{R}assets/main.js"></script>
</body>
</html>'''

def cta_band(R):
    return f'''<section class="cta-band">
  <div class="wrap cta-band-in">
    <p class="eyebrow reveal">Randevu ve Bilgi</p>
    <h2 class="reveal reveal-d1">Muayene ve değerlendirme randevusu için bize ulaşın</h2>
    <p class="reveal reveal-d2">Durumunuza uygun tanı ve tedavi sürecinin planlanması için kliniğimizle iletişime geçebilirsiniz. Görüşmeler Türkçe, İngilizce, Rusça ve Ukraynaca yapılabilmektedir.</p>
    <div class="hero-ctas reveal reveal-d3">
      <a class="btn btn-gold" href="{R}contacts/">Randevu Talebi {IC['arrow-right']}</a>
      <a class="btn btn-ghost" href="{TEL}">{PHONE}</a>
    </div>
  </div>
</section>'''

def steps_sec():
    return f'''<section class="sec sec-stone">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow reveal">Muayene Süreci</p>
      <h2 class="reveal reveal-d1">Süreç nasıl ilerler?</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Ön Görüşme ve Bilgilendirme</h3><p>Şikâyetleriniz ve beklentileriniz dinlenir. Sürecin kapsamı, olası riskler ve seçenekler hakkında ayrıntılı bilgilendirme yapılır.</p></div>
      <div class="step reveal reveal-d1"><h3>Muayene ve Tanı</h3><p>Gerekli muayene ve tetkikler gerçekleştirilir. Bulgular sizinle birlikte değerlendirilir.</p></div>
      <div class="step reveal reveal-d2"><h3>Tedavi Planlaması</h3><p>Muayene bulgularına göre uygun tedavi seçenekleri belirlenir; süreç ve takvim birlikte planlanır.</p></div>
      <div class="step reveal reveal-d3"><h3>Kontrol ve Takip</h3><p>Tedavi sonrasında kontrol muayeneleri planlanır; iyileşme süreci düzenli olarak takip edilir.</p></div>
    </div>
  </div>
</section>'''

def ba_slider(R, on='ba-anat-on', so='ba-anat-so', cap=''):
    caption = f'<figcaption class="ba-cap">{cap}</figcaption>' if cap else ''
    return f"""<div class="ba-slider reveal" style="--pos: 50%;">
      <img class="ba-under" src="{R}assets/img/{so}.jpg" alt="Rinoplasti sonrası, klinik arşivi" loading="lazy">
      <div class="ba-over"><img src="{R}assets/img/{on}.jpg" alt="Rinoplasti öncesi, klinik arşivi" loading="lazy"></div>
      <div class="ba-handle" aria-hidden="true"><span>{IC['chevron-right']}</span></div>
      <input type="range" class="ba-range" min="0" max="100" value="50" aria-label="Öncesi sonrası karşılaştırma kaydırıcısı">
      <span class="ba-label on">Öncesi</span>
      <span class="ba-label so">Sonrası</span>
      {caption}
    </div>"""

def ba_real(R, n, tedavi='Rinoplasti'):
    return f"""<figure class="ba-frame reveal reveal-d{n % 3}">
        <img src="{R}assets/img/ba-gercek-{n}.jpg" alt="{tedavi} öncesi ve sonrası, klinik arşivi" loading="lazy">
        <span class="ba-label on">Öncesi</span>
        <span class="ba-label so">Sonrası</span>
        <figcaption class="ba-cap">Klinik arşivi · {tedavi}</figcaption>
      </figure>"""

def ba_sec(R, stone=False):
    return f"""<section class="sec{' sec-stone' if stone else ''}" id="oncesi-sonrasi">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow reveal">Öncesi ve Sonrası</p>
      <h2 class="reveal reveal-d1">Kliniğimizden gerçek sonuçlar</h2>
      <p class="reveal reveal-d2">Kareler klinik arşivimizden alınmıştır. Her burun yapısı farklıdır; operasyonun kapsamı muayenede birlikte belirlenir.</p>
    </div>
    <div class="ba-band reveal">
      <div class="ba-track">{ba_real(R, 1)}{ba_real(R, 2)}{ba_real(R, 3)}{ba_real(R, 1)}{ba_real(R, 2)}{ba_real(R, 3)}</div>
    </div>
    <div class="hero-ctas reveal reveal-d1" style="margin-top: var(--space-6);">
      <a class="btn btn-ghost" href="{IG_URL}" target="_blank" rel="noopener" style="border-color: var(--line); color: var(--text);">Instagram'da Daha Fazlasını Görün {IC['arrow-right']}</a>
    </div>
  </div>
</section>"""

def gallery_sec(R):
    imgs = ['klinik', 'ofis-2', 'ofis-4', 'ofis-5', 'ofis-6', 'ofis-7', 'ofis-8']
    items = ''.join(f'<img src="{R}assets/img/{i}.jpg" alt="Doç. Dr. Sema Koç kliniği" loading="lazy">' for i in imgs)
    return f"""<section class="gallery-band" aria-label="Klinik galerisi">
    <div class="marquee-track">{items}{items}</div>
  </section>"""

def pick_reviews(tags=None, n=6):
    pool = REVIEWS
    if tags:
        matched = [r for r in REVIEWS if set(r['tags']) & set(tags)]
        others = [r for r in REVIEWS if r not in matched]
        pool = matched + others
    return pool[:n]

def rev_cards_html(tags=None, n=6, delay_mod=3):
    stars5 = ''.join(IC['star'] for _ in range(5))
    return '\n'.join(
        f"""<article class="rev-card liquid-glass reveal{' reveal-d' + str(i % delay_mod) if i % delay_mod else ''}">
      <div class="stars">{stars5}</div>
      <blockquote>\u201c{r['text']}\u201d</blockquote>
      <footer><b>{r['name']}</b><span>{r['when']} · Google</span></footer>
    </article>""" for i, r in enumerate(pick_reviews(tags, n)))

GOOGLE_G = '<svg class="gg" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="#4285F4" d="M45.12 24.5c0-1.56-.14-3.06-.4-4.5H24v8.51h11.84c-.51 2.75-2.06 5.08-4.39 6.64v5.52h7.11c4.16-3.83 6.56-9.47 6.56-16.17z"/><path fill="#34A853" d="M24 46c5.94 0 10.92-1.97 14.56-5.33l-7.11-5.52c-1.97 1.32-4.49 2.1-7.45 2.1-5.73 0-10.58-3.87-12.31-9.07H4.34v5.7C7.96 41.07 15.4 46 24 46z"/><path fill="#FBBC05" d="M11.69 28.18C11.25 26.86 11 25.45 11 24s.25-2.86.69-4.18v-5.7H4.34C2.85 17.09 2 20.45 2 24c0 3.55.85 6.91 2.34 9.88l7.35-5.7z"/><path fill="#EA4335" d="M24 10.75c3.23 0 6.13 1.11 8.41 3.29l6.31-6.31C34.91 4.18 29.93 2 24 2 15.4 2 7.96 6.93 4.34 14.12l7.35 5.7c1.73-5.2 6.58-9.07 12.31-9.07z"/></svg>'

TR_STATS = [('20', '+', 'Yıl Hekimlik Deneyimi'), ('4.8', '', 'Google Puanı'),
            ('529', '', 'Google Yorumu'), ('9', '', 'Uzmanlık Alanı')]

def hero_cards(stats, gtitle, rev_tags=None):
    """Hero altindaki genis stat bandi yerine yan yana 2 kart:
       1) Google yorumlari (puan + yildizlar + yorum sayisi + tek yorum onizleme)
       2) Yil hekimlik deneyimi + uzmanlik alani"""
    exp, rating, revs, areas = stats[0], stats[1], stats[2], stats[3]
    r = pick_reviews(rev_tags, 1)[0]
    stars5 = ''.join(IC['star'] for _ in range(5))
    txt = ' '.join(r['text'].split())
    if len(txt) > 96:
        txt = txt[:96].rsplit(' ', 1)[0] + '…'
    ini = r['name'].strip()[0].upper()
    sfx = lambda s: f' data-suffix="{s}"' if s else ''
    return f'''<div class="hero-cards">
      <div class="hcard gcard liquid-glass">
        <div class="gcard-l">
          <p class="gcard-eyebrow">{gtitle}</p>
          <div class="grow">{GOOGLE_G}<b data-count="{rating[0]}">0</b><span class="gstars">{stars5}</span></div>
          <p class="gcount"><b data-count="{revs[0]}">0</b> <span>{revs[2]}</span></p>
        </div>
        <div class="gcard-sep" aria-hidden="true"></div>
        <div class="gcard-r">
          <div class="rev-av" aria-hidden="true">{ini}</div>
          <div class="rev-mini">
            <p class="rev-mn">{r['name']} <span class="gstars sm">{stars5}</span></p>
            <p class="rev-mt">{txt}</p>
          </div>
        </div>
      </div>
      <div class="hcard scard liquid-glass">
        <div class="stat"><b data-count="{exp[0]}"{sfx(exp[1])}>0</b><span>{exp[2]}</span></div>
        <div class="stat"><b data-count="{areas[0]}"{sfx(areas[1])}>0</b><span>{areas[2]}</span></div>
      </div>
    </div>'''

def rev_slider_html(tags=None, n=10):
    stars5 = ''.join(IC['star'] for _ in range(5))
    cards = '\n'.join(
        f"""<article class="rev-card liquid-glass">
      <div class="stars">{stars5}</div>
      <blockquote>\u201c{r['text']}\u201d</blockquote>
      <footer><b>{r['name']}</b><span>{r['when']} · Google</span></footer>
    </article>""" for r in pick_reviews(tags, n))
    return f"""<div class="rev-slider-wrap reveal">
      <div class="rev-slider" tabindex="0">{cards}</div>
      <div class="rev-nav">
        <button type="button" class="rev-btn" data-dir="-1" aria-label="Önceki yorumlar">{IC['chevron-right']}</button>
        <button type="button" class="rev-btn" data-dir="1" aria-label="Sonraki yorumlar">{IC['chevron-right']}</button>
      </div>
    </div>"""

def reviews_sec(tags=None, n=10):
    stars5 = ''.join(IC['star'] for _ in range(5))
    return f"""<section class="sec dark-sec" id="yorumlar">
  <div class="wrap">
    <div class="rev-head">
      <div>
        <p class="eyebrow reveal">Google Değerlendirmeleri</p>
        <h2 class="reveal reveal-d1" style="font-size: var(--text-2xl); margin-top: var(--space-3);">Hastalarımız ne diyor?</h2>
      </div>
      <div class="rev-score-inline reveal reveal-d1">
        <b data-count="4.8">4,8</b>
        <div>
          <div class="stars">{stars5}</div>
          <p><span data-count="529">529</span> Google yorumu</p>
        </div>
        <a class="btn btn-gold" href="{MAPS_URL}" target="_blank" rel="noopener">Tümünü Gör {IC['arrow-right']}</a>
      </div>
    </div>
    {rev_slider_html(tags, n)}
    <p class="rev-note reveal">Yorumlar, hastaların Google Haritalar üzerinde kamuya açık olarak paylaştığı değerlendirmelerden alınmıştır.</p>
  </div>
</section>"""

def media_sec(R):
    play = '<span class="play-btn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="6,3 21,12 6,21"/></svg></span>'
    cards = '\n'.join(f'''<button type="button" class="vid-card reveal{' reveal-d' + str(i % 3) if i % 3 else ''}" data-yt="{vid}" aria-label="Videoyu oynat: {title}">
      <span class="vid-thumb"><img src="{R}assets/img/yt-{vid}.jpg" alt="{title}" loading="lazy"><span class="play">{play}</span></span>
      <p class="card-t">{title}</p>
    </button>''' for i, (vid, title) in enumerate(VIDEOS))
    return f'''<section class="sec" id="medya">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow reveal">Medya ve TV</p>
      <h2 class="reveal reveal-d1">Televizyon programları ve bilgilendirme videoları</h2>
      <p class="reveal reveal-d2">Doç. Dr. Sema Koç'un ulusal kanallarda ve dijital platformlarda kulak burun boğaz sağlığı üzerine yaptığı bilgilendirmelerden seçkiler.</p>
    </div>
    <div class="vid-grid">{cards}</div>
    <div class="tv-strip">
      <img class="reveal" src="{R}assets/img/tv-1.jpg" alt="Doç. Dr. Sema Koç televizyon programında" loading="lazy">
      <img class="reveal reveal-d1" src="{R}assets/img/tv-2.jpg" alt="Doç. Dr. Sema Koç TV8 Günaydın Doktor programında" loading="lazy">
      <img class="reveal reveal-d2" src="{R}assets/img/tv-3.jpg" alt="Doç. Dr. Sema Koç TV yayınında" loading="lazy">
    </div>
  </div>
</section>'''

def side(R, current_slug, konu='Genel Bilgi ve Randevu'):
    items = '\n'.join(
        f'<li><a href="{R}{t["slug"]}"{" class=\"here\"" if t["slug"] == current_slug else ""}>{t["nav"]} {IC["chevron-right"]}</a></li>'
        for t in T)
    return f'''<aside class="side">
  <div class="side-card reveal">
    <h3>Tedavi ve Uygulamalar</h3>
    <ul>{items}</ul>
  </div>
  <div class="side-cta reveal reveal-d1">
    <h3>Randevu Talebi</h3>
    {wa_form('Hızlı Randevu', konu, subject_select=True)}
    <a class="btn btn-ghost" href="{TEL}" style="width: 100%; justify-content: center; margin-top: var(--space-3); font-size: .9rem;">{IC['phone']} {PHONE}</a>
  </div>
</aside>'''

# ---------------- SAYFALAR ----------------
def treatment_page(t):
    depth = t['slug'].count('/')
    R = '../' * depth
    secs = []
    for h2, kind, items in t['sections']:
        if kind == 'p':
            body = '\n'.join(f'<p>{p}</p>' for p in items)
        else:
            body = '<ul>' + '\n'.join(f'<li>{IC["check"]}<span>{i}</span></li>' for i in items) + '</ul>'
        secs.append(f'<h2>{h2}</h2>\n{body}')
    prose = '\n'.join(secs)
    faq_html = '\n'.join(
        f'<details class="reveal"><summary>{q} {IC["x"]}</summary><div class="faq-a">{a}</div></details>'
        for q, a in t['faq'])
    faq_ld = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t['faq']]
    }, ensure_ascii=False)
    return f'''{head(R, t['title'], t['meta'])}
{header(R)}
<main id="top">
  <section class="page-hero">
    <div class="wrap page-hero-in">
      <div>
        <nav class="breadcrumb reveal" aria-label="breadcrumb">
          <a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']}
          <a href="{R}sunulan-hizmetler/">Tedaviler</a> {IC['chevron-right']}
          <b>{t['nav']}</b>
        </nav>
        <h1 class="reveal reveal-d1">{t['h1']}</h1>
        <p class="lead reveal reveal-d2">{t['lead']}</p>
        <div class="hero-ctas reveal reveal-d3">
          <a class="btn btn-gold" href="{R}contacts/">Randevu Talebi {IC['arrow-right']}</a>
          <a class="btn btn-ghost" href="{TEL}">{PHONE}</a>
        </div>
      </div>
      <div class="page-hero-img reveal reveal-d2"><img src="{R}assets/img/{t['img']}" alt="{t['h1']}" loading="eager"></div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap content-grid">
      <article class="prose reveal">{prose}</article>
      {side(R, t['slug'], t['nav'])}
    </div>
  </section>

  {steps_sec()}

  {ba_sec('../' * t['slug'].count('/')) if t['slug'] == 'our-services/rhinoplasty/' else ''}

  <section class="sec">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">Sık Sorulan Sorular</p>
        <h2 class="reveal reveal-d1">{t['nav']} hakkında merak edilenler</h2>
      </div>
      <div class="faq">{faq_html}</div>
    </div>
  </section>

  {cta_band(R)}
</main>
<script type="application/ld+json">{faq_ld}</script>
{footer(R)}'''

def home_page():
    R = ''
    svc_cards = '\n'.join(
        f'''<a class="pcard reveal{' reveal-d' + str(i % 4) if i % 4 else ''}" href="{t['slug']}">
        <img src="assets/img/{t['img']}" alt="{t['h1']}" loading="lazy">
        <span class="pbody"><p class="card-t">{t['nav']}</p><p>{t['lead'][:110].rsplit(' ', 1)[0]}…</p>
        <span class="more">Ayrıntılı Bilgi {IC['arrow-right']}</span></span></a>'''
        for i, t in enumerate(T[:8]))
    posts = '\n'.join(
        f'''<a class="post reveal{' reveal-d' + str(i % 3) if i % 3 else ''}" href="{p['href'] if not p['local'] else R + p['href']}"{' target="_blank" rel="noopener"' if not p['local'] else ''}>
        <img src="assets/img/{p['img']}" alt="{p['t']}" loading="lazy">
        <span class="pbody"><span class="post-meta"><span class="cat">{p['cat']}</span><span class="date">{p['date']}</span></span>
        <p class="card-t">{p['t']}</p><p>{p['d']}</p><span class="more">Yazıyı Oku {IC['arrow-right']}</span></span></a>'''
        for i, p in enumerate(POSTS[:3]))
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Physician",
        "name": "Doç. Dr. Sema Koç", "medicalSpecialty": "Otolaryngologic",
        "telephone": "+905439136595", "email": MAIL,
        "address": {"@type": "PostalAddress", "streetAddress": "Tekelioğlu Cad. 1947. Sk. No: 29/3",
                    "addressLocality": "Muratpaşa", "addressRegion": "Antalya", "addressCountry": "TR"}
    }, ensure_ascii=False)
    return f'''{head(R, 'Doç. Dr. Sema Koç | KBB ve Baş-Boyun Cerrahisi, Antalya', "Doç. Dr. Sema Koç, Antalya'da rinoplasti, kulak burun boğaz hastalıkları, baş-boyun cerrahisi, vertigo ve odyoloji alanlarında tanı ve tedavi hizmetleri sunmaktadır.")}
{header(R, 'home')}
<main id="top">
  <section class="hero3">
    <video class="kbvid" autoplay muted loop playsinline preload="metadata" poster="https://drsemakoc.com/hero/hero_poster_desktop.jpg" aria-hidden="true">
      <source src="https://drsemakoc.com/hero/hero_mobile.mp4" media="(max-width: 768px)" type="video/mp4">
      <source src="https://drsemakoc.com/hero/hero_desktop.mp4" type="video/mp4">
    </video>
    <div class="ov" aria-hidden="true"></div>
    <div class="wrap hero3-in hero3-center">
      <p class="eyebrow fade-rise">Doç. Dr. Sema Koç · KBB ve Baş-Boyun Cerrahisi · Antalya</p>
      <h1 class="fade-rise-d1">Yirmi yılı aşkın deneyim, <em>akademik titizlikle.</em></h1>
      <p class="lead fade-rise-d2">Rinoplasti, KBB, baş-boyun cerrahisi, vertigo ve odyolojide tanı ve tedavi. Randevu için bize ulaşın.</p>
      <div class="hero-ctas fade-rise-d3">
        <a class="btn btn-gold" href="contacts/">Randevu Talebi {IC['arrow-right']}</a>
        <a class="btn btn-glass liquid-glass" href="sunulan-hizmetler/">Tedavi ve Uygulamalar</a>
      </div>
      <p class="hero-note fade-rise-d4">{IC['globe']} Görüşmeler Türkçe, İngilizce, Rusça ve Ukraynaca yapılabilmektedir.</p>
    </div>
    <div class="wrap hero3-stats fade-rise-d4">{hero_cards(TR_STATS, 'Google Yorumları')}</div>
  </section>

  <div class="creds">
    <div class="wrap creds-in">
      <div class="cred reveal">{IC['graduation-cap']}<div><b>Gazi Üniversitesi Tıp Fakültesi</b><small>2001 · Tıp Doktoru</small></div></div>
      <div class="cred reveal reveal-d1">{IC['microscope']}<div><b>Da Vinci Transoral Robotik Cerrahi</b><small>2012 · Eğitim</small></div></div>
      <div class="cred reveal reveal-d2">{IC['award']}<div><b>Doçentlik, Kulak Burun Boğaz</b><small>2013 · Akademik Unvan</small></div></div>
      <div class="cred reveal reveal-d3">{IC['audio-lines']}<div><b>Odyoloji Yüksek Lisansı</b><small>2014 · Uzman Odyolog</small></div></div>
    </div>
  </div>

  <section class="sec">
    <div class="wrap about-grid">
      <div class="about-copy">
        <p class="eyebrow reveal">Hakkında</p>
        <h2 class="reveal reveal-d1">Akademik birikim, yirmi yılı aşkın klinik deneyim</h2>
        <p class="big reveal reveal-d2">Doç. Dr. Sema Koç, 2001 yılında Gazi Üniversitesi Tıp Fakültesi'nden mezun oldu ve uzmanlık eğitimini Kulak Burun Boğaz alanında tamamladı.</p>
        <p class="reveal reveal-d2">2012 yılında Da Vinci Transoral Robotik Cerrahi eğitimini tamamladı, 2013 yılında KBB alanında doçentlik unvanını aldı. 2014 yılında Yıldırım Beyazıt Üniversitesi'nde Odyoloji alanında yüksek lisansını bitirerek uzman odyolog unvanını kazandı.</p>
        <div class="hero-ctas reveal reveal-d3" style="margin-top: var(--space-5);">
          <a class="btn btn-ghost" href="about-us/" style="border-color: var(--line); color: var(--text);">Özgeçmişin Tamamı {IC['arrow-right']}</a>
        </div>
      </div>
      <img class="about-photo reveal reveal-d1" src="assets/img/portre-2.jpg" alt="Doç. Dr. Sema Koç" loading="lazy" style="align-self: start;">
    </div>
    <div class="wrap">
      <ol class="timeline-h reveal">
        <li><span class="yr">2001</span><b>Tıp Fakültesi Mezuniyeti</b><small>Gazi Üniversitesi, Ankara</small></li>
        <li><span class="yr">2012</span><b>Robotik Cerrahi Eğitimi</b><small>Da Vinci Transoral Robotik Cerrahi</small></li>
        <li><span class="yr">2013</span><b>Doçentlik Unvanı</b><small>Kulak Burun Boğaz Hastalıkları</small></li>
        <li><span class="yr">2014</span><b>Odyoloji Yüksek Lisansı</b><small>Yıldırım Beyazıt Ü. · Uzman Odyolog</small></li>
      </ol>
    </div>
  </section>

  {reviews_sec()}

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">Uzmanlık Alanları</p>
        <h2 class="reveal reveal-d1">Tanı ve tedavi hizmetleri</h2>
        <p class="reveal reveal-d2">Aşağıdaki alanlarda muayene, tanı ve tedavi süreçleri kliniğimizde planlanmaktadır. Her tedavi kararı, muayene ve değerlendirme sonrasında hastayla birlikte verilir.</p>
      </div>
      <div class="photo-grid svc-photo">{svc_cards}</div>
    </div>
  </section>

  {ba_sec(R)}

  {gallery_sec(R)}

  {media_sec(R)}

  {steps_sec()}

  <section class="sec sec-stone" style="padding-top:0; background: var(--ivory);">
    <div class="wrap">
      <div class="travel reveal">
        <div>
          <p class="eyebrow">Şehir Dışından Gelenler</p>
          <h3>Şehir dışından ve yurt dışından gelen hastalar için</h3>
          <p>Antalya dışından gelen hastaların muayene ve kontrol randevuları, seyahat planlarına uygun şekilde düzenlenebilmektedir. Ulaşım ve konaklama konularında bilgilendirme desteği sağlanır.</p>
        </div>
        <div class="travel-list">
          <div class="travel-item"><div class="badge">{IC['plane']}</div><div><b>Randevu planlaması</b><p>Muayene ve kontrol randevuları seyahat tarihlerinize göre düzenlenir.</p></div></div>
          <div class="travel-item"><div class="badge">{IC['building-2']}</div><div><b>Konaklama bilgilendirmesi</b><p>Kliniğe yakın konaklama seçenekleri hakkında bilgi verilir.</p></div></div>
          <div class="travel-item"><div class="badge">{IC['globe']}</div><div><b>Üç dilde iletişim</b><p>Görüşmeler Türkçe, İngilizce, Rusça ve Ukraynaca yapılabilmektedir.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">Bilgilendirme Yazıları</p>
        <h2 class="reveal reveal-d1">Kulak burun boğaz sağlığı üzerine yazılar</h2>
        <p class="reveal reveal-d2">Hasta bilgilendirmesi amacıyla hazırlanan yazılar. İçerikler tıbbi tanı ve tedavinin yerini tutmaz.</p>
      </div>
      <div class="post-grid">{posts}</div>
      <div class="hero-ctas reveal" style="margin-top: var(--space-6);">
        <a class="btn btn-ghost" href="blog/" style="border-color: var(--line); color: var(--text);">Tüm Yazılar {IC['arrow-right']}</a>
      </div>
    </div>
  </section>

  {cta_band(R)}
</main>
<script type="application/ld+json">{ld}</script>
{footer(R)}'''

def about_page():
    R = '../'
    return f'''{head(R, 'Hakkımızda | Doç. Dr. Sema Koç', 'Doç. Dr. Sema Koç: Gazi Üniversitesi Tıp Fakültesi mezunu, KBB doçenti, uzman odyolog. Akademik özgeçmiş ve klinik deneyim.')}
{header(R, 'about')}
<main id="top">
  <section class="page-hero">
    <div class="wrap page-hero-in">
      <div>
        <nav class="breadcrumb reveal" aria-label="breadcrumb"><a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']} <b>Hakkımızda</b></nav>
        <h1 class="reveal reveal-d1">Doç. Dr. Sema Koç</h1>
        <p class="lead reveal reveal-d2">Kulak Burun Boğaz ve Baş-Boyun Cerrahisi Uzmanı, Uzman Odyolog. Yirmi yılı aşkın hekimlik deneyimini Antalya'daki kliniğinde sürdürmektedir.</p>
      </div>
      <div class="page-hero-img reveal reveal-d2"><img src="{R}assets/img/portre-2.jpg" alt="Doç. Dr. Sema Koç" loading="eager" style="object-fit: cover; object-position: top;"></div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap about-grid">
      <div class="about-copy">
        <p class="eyebrow reveal">Özgeçmiş</p>
        <h2 class="reveal reveal-d1">Akademik birikim ve klinik deneyim</h2>
        <p class="big reveal reveal-d2">Doç. Dr. Sema Koç 1978 yılında Ankara'da doğdu. Gazi Üniversitesi Tıp Fakültesi'nden 2001 yılında mezun oldu ve uzmanlık eğitimini Kulak Burun Boğaz alanında tamamladı.</p>
        <p class="reveal reveal-d2">2012 yılında Da Vinci Transoral Robotik Cerrahi eğitimini alarak ileri cerrahi teknolojileri klinik pratiğine ekledi. 2013 yılında KBB alanında doçentlik unvanını aldı.</p>
        <p class="reveal reveal-d2">2014 yılında Yıldırım Beyazıt Üniversitesi'nde Odyoloji alanında yüksek lisansını tamamlayarak uzman odyolog unvanını kazandı. İşitme ve denge bozukluklarının değerlendirilmesinde bu birikim klinik süreçlere katkı sağlamaktadır.</p>
        <ul class="focus-list reveal reveal-d3">
          <li>{IC['check']} Rinoplasti ve fonksiyonel burun cerrahisi</li>
          <li>{IC['check']} Baş-boyun cerrahisi ve robotik cerrahi eğitimi</li>
          <li>{IC['check']} Vertigo tanı ve tedavisi</li>
          <li>{IC['check']} Odyoloji: işitme ve denge değerlendirmesi</li>
        </ul>
      </div>
      <img class="about-photo reveal reveal-d2" src="{R}assets/img/klinik.jpg" alt="Doç. Dr. Sema Koç kliniği" loading="lazy" style="align-self: start; aspect-ratio: 3 / 4;">
    </div>
    <div class="wrap">
      <ol class="timeline-h reveal">
        <li><span class="yr">2001</span><b>Tıp Fakültesi Mezuniyeti</b><small>Gazi Üniversitesi Tıp Fakültesi</small></li>
        <li><span class="yr">2012</span><b>Robotik Cerrahi Eğitimi</b><small>Da Vinci Transoral Robotik Cerrahi</small></li>
        <li><span class="yr">2013</span><b>Doçentlik Unvanı</b><small>Kulak Burun Boğaz Hastalıkları</small></li>
        <li><span class="yr">2014</span><b>Odyoloji Yüksek Lisansı</b><small>Yıldırım Beyazıt Ü. · Uzman Odyolog</small></li>
      </ol>
    </div>
  </section>

  {cta_band(R)}
</main>
{footer(R)}'''

def services_page():
    R = '../'
    cards = '\n'.join(
        f'''<a class="pcard reveal{' reveal-d' + str(i % 3) if i % 3 else ''}" href="{R}{t['slug']}">
        <img src="{R}assets/img/{t['img']}" alt="{t['h1']}" loading="lazy">
        <span class="pbody"><p class="card-t">{t['nav']}</p><p>{t['lead'][:140].rsplit(' ', 1)[0]}…</p>
        <span class="more">Ayrıntılı Bilgi {IC['arrow-right']}</span></span></a>'''
        for i, t in enumerate(T))
    return f'''{head(R, 'Sunulan Hizmetler | Doç. Dr. Sema Koç, Antalya', 'Doç. Dr. Sema Koç kliniğinde sunulan tanı ve tedavi hizmetleri: rinoplasti, septoplasti, horlama ve uyku apnesi, kulak ve işitme cerrahisi, baş-boyun cerrahisi, vertigo.')}
{header(R)}
<main id="top">
  <section class="page-hero">
    <div class="wrap" style="padding-block: clamp(2.8rem, 5.5vw, 4.5rem);">
      <nav class="breadcrumb reveal" aria-label="breadcrumb"><a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']} <b>Sunulan Hizmetler</b></nav>
      <h1 class="reveal reveal-d1" style="font-size: var(--text-2xl); font-weight: 500; margin-top: var(--space-4);">Tedavi ve Uygulamalar</h1>
      <p class="lead reveal reveal-d2" style="margin-top: var(--space-4); font-size: var(--text-lg); font-weight: 300; color: var(--text-inv-soft); max-width: 40em;">Aşağıdaki alanlarda muayene, tanı ve tedavi süreçleri kliniğimizde planlanmaktadır. Her tedavi kararı, muayene ve değerlendirme sonrasında hastayla birlikte verilir.</p>
    </div>
  </section>
  <section class="sec">
    <div class="wrap"><div class="photo-grid">{cards}</div></div>
  </section>
  {steps_sec()}
  {cta_band(R)}
</main>
{footer(R)}'''

def blog_page():
    R = '../'
    posts = '\n'.join(
        f'''<a class="post reveal{' reveal-d' + str(i % 3) if i % 3 else ''}" href="{p['href'] if not p['local'] else R + p['href']}"{' target="_blank" rel="noopener"' if not p['local'] else ''}>
        <img src="{R}assets/img/{p['img']}" alt="{p['t']}" loading="lazy">
        <span class="pbody"><span class="post-meta"><span class="cat">{p['cat']}</span><span class="date">{p['date']}</span></span>
        <p class="card-t">{p['t']}</p><p>{p['d']}</p><span class="more">Yazıyı Oku {IC['arrow-right']}</span></span></a>'''
        for i, p in enumerate(POSTS))
    return f'''{head(R, 'Blog | Doç. Dr. Sema Koç', 'Kulak burun boğaz sağlığı üzerine bilgilendirme yazıları: vertigo, uyku apnesi, ses kısıklığı, geniz eti ve daha fazlası.')}
{header(R, 'blog')}
<main id="top">
  <section class="page-hero">
    <div class="wrap" style="padding-block: clamp(2.8rem, 5.5vw, 4.5rem);">
      <nav class="breadcrumb reveal" aria-label="breadcrumb"><a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']} <b>Blog</b></nav>
      <h1 class="reveal reveal-d1" style="font-size: var(--text-2xl); font-weight: 500; margin-top: var(--space-4);">Bilgilendirme Yazıları</h1>
      <p class="lead reveal reveal-d2" style="margin-top: var(--space-4); font-size: var(--text-lg); font-weight: 300; color: var(--text-inv-soft); max-width: 40em;">Hasta bilgilendirmesi amacıyla hazırlanan yazılar. İçerikler tıbbi tanı ve tedavinin yerini tutmaz.</p>
    </div>
  </section>
  <section class="sec">
    <div class="wrap"><div class="post-grid">{posts}</div></div>
  </section>
  {cta_band(R)}
</main>
{footer(R)}'''

def post_page():
    R = '../'
    others = '\n'.join(
        f'''<li><a href="{p['href'] if not p['local'] else '#'}"{' target="_blank" rel="noopener"' if not p['local'] else ''}>{p['t']} {IC['chevron-right']}</a></li>'''
        for p in POSTS[1:])
    sidebar = f'''<aside class="side">
  <div class="side-card reveal">
    <h3>Diğer Yazılar</h3>
    <ul>{others}</ul>
  </div>
  <div class="side-cta reveal reveal-d1">
    <h3>Randevu Talebi</h3>
    {wa_form('Hızlı Randevu', 'Vertigo (Baş Dönmesi)', subject_select=True)}
    <a class="btn btn-ghost" href="{TEL}" style="width: 100%; justify-content: center; margin-top: var(--space-3); font-size: .9rem;">{IC['phone']} {PHONE}</a>
  </div>
  <div class="side-card reveal reveal-d2">
    <h3>İletişim</h3>
    <p class="side-contact">{IC['map-pin']} <span>{ADDR}</span></p>
    <p class="side-contact"><a href="{TEL}">{IC['phone']} <span>{PHONE}</span></a></p>
    <p class="side-contact"><a href="mailto:{MAIL}">{IC['mail']} <span>{MAIL}</span></a></p>
    <p class="side-contact"><a href="{WA}" target="_blank" rel="noopener">{IC['message-circle']} <span>WhatsApp ile yazın</span></a></p>
  </div>
</aside>'''
    return f'''{head(R, 'Baş Dönmesi: Nedenleri, Belirtileri ve Tedavisi | Doç. Dr. Sema Koç', 'Baş dönmesinin (vertigo) sık görülen nedenleri, eşlik eden belirtiler, tanı süreci ve tedavi yaklaşımları hakkında bilgilendirme yazısı.')}
{header(R, 'blog')}
<main id="top">
  <section class="page-hero">
    <div class="wrap" style="padding-block: clamp(2.8rem, 5.5vw, 4.5rem);">
      <nav class="breadcrumb reveal" aria-label="breadcrumb"><a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']} <a href="{R}blog/">Blog</a> {IC['chevron-right']} <b>Baş Dönmesi</b></nav>
      <h1 class="reveal reveal-d1" style="font-size: var(--text-2xl); font-weight: 500; margin-top: var(--space-4); max-width: 18em;">Baş Dönmesi: Nedenleri, Belirtileri ve Tedavisi</h1>
      <p class="reveal reveal-d2" style="margin-top: var(--space-4); display:flex; gap:.8rem; font-size:.8rem; letter-spacing:.08em; text-transform:uppercase;"><span style="color:var(--brass-2); font-weight:600;">Vertigo</span><span style="color:var(--text-inv-soft);">7 Haziran 2026 · Doç. Dr. Sema Koç</span></p>
    </div>
  </section>
  <section class="sec">
    <div class="wrap content-grid">
      <div>
        <img class="reveal" src="{R}assets/img/blog-bas-donmesi.jpg" alt="Baş dönmesi tedavisi" style="border-radius: var(--radius); border: 1px solid var(--line); margin-bottom: var(--space-6); width: 100%;" loading="eager">
        <article class="prose reveal">
          <p class="big">Baş dönmesi, kişinin kendisinin veya çevresinin döndüğü ya da hareket ettiği hissine kapıldığı yaygın bir sağlık sorunudur. Tıbbi adıyla vertigo, tek başına bir hastalık değil, altta yatan bir durumun belirtisidir.</p>
          <h2>Baş Dönmesinin Sık Görülen Nedenleri</h2>
          <p>Vertigonun en sık nedeni, iç kulaktaki kalsiyum karbonat kristallerinin yer değiştirmesiyle oluşan iyi huylu pozisyonel vertigodur (BPPV). Bunun dışında Meniere hastalığı, vestibüler nörit, migrenle ilişkili baş dönmesi ve bazı ilaçların yan etkileri de vertigo tablosuna yol açabilir.</p>
          <h2>Hangi Belirtilere Dikkat Edilmeli?</h2>
          <ul>
            <li>{IC['check']}<span>Baş hareketleriyle tetiklenen kısa süreli dönme hissi</span></li>
            <li>{IC['check']}<span>Dengesizlik ve yürüme güçlüğü</span></li>
            <li>{IC['check']}<span>Bulantı veya kusmanın eşlik etmesi</span></li>
            <li>{IC['check']}<span>İşitme kaybı, çınlama veya kulakta dolgunluk hissi</span></li>
          </ul>
          <p>Bu belirtilerin görüldüğü durumlarda kulak burun boğaz muayenesi önerilir. Ani başlayan, şiddetli baş ağrısı, görme bozukluğu veya konuşma güçlüğü eşlik eden baş dönmelerinde vakit kaybetmeden sağlık kuruluşuna başvurulmalıdır.</p>
          {wa_form('Baş dönmesi şikâyetiniz mi var?', 'Baş Dönmesi (Vertigo)')}
          <h2>Tanı Süreci</h2>
          <p>Tanıda ayrıntılı öykü ve denge muayenesi esastır. Pozisyonel testler, işitme testleri ve gerekli görüldüğünde görüntüleme yöntemleri kullanılır. Vertigonun tipi ve nedeni belirlendiğinde tedavi buna göre planlanır.</p>
          <h2>Tedavi Yaklaşımları</h2>
          <p>BPPV tanısı konulan hastalarda Epley ve Semont gibi pozisyonel manevralar uygulanır. Diğer nedenlerde ilaç tedavisi, vestibüler rehabilitasyon egzersizleri veya altta yatan hastalığa yönelik tedaviler gündeme gelir. Tedavi planı hekim tarafından kişiye özel oluşturulur.</p>
          {wa_form('Muayene randevusu planlayalım mı?', 'Baş Dönmesi (Vertigo)')}
          <p><em>Bu yazı bilgilendirme amacıyla hazırlanmıştır; tanı ve tedavi için lütfen hekiminize başvurunuz.</em></p>
        </article>
      </div>
      {sidebar}
    </div>
  </section>
  {cta_band(R)}
</main>
{footer(R)}'''

def contact_page():
    R = '../'
    return f'''{head(R, 'İletişim ve Randevu | Doç. Dr. Sema Koç, Antalya', 'Doç. Dr. Sema Koç kliniği iletişim bilgileri: adres, telefon, e-posta ve randevu talebi. Muratpaşa, Antalya.')}
{header(R, 'contact')}
<main id="top">
  <section class="sec dark-sec" style="padding-top: clamp(2.8rem, 5.5vw, 4.5rem);">
    <div class="wrap">
      <nav class="breadcrumb reveal" aria-label="breadcrumb" style="margin-bottom: var(--space-6);"><a href="{R}index.html">Ana Sayfa</a> {IC['chevron-right']} <b>İletişim</b></nav>
      <div class="contact-grid">
        <div>
          <p class="eyebrow reveal">İletişim ve Randevu</p>
          <h2 class="reveal reveal-d1">Muayene randevusu için bize ulaşın</h2>
          <p class="intro reveal reveal-d2">Randevu oluşturmak veya bilgi almak için telefon, e-posta ya da sosyal medya kanallarından ulaşabilirsiniz. Görüşmeler Türkçe, İngilizce, Rusça ve Ukraynaca yapılabilmektedir.</p>
          <div class="socials reveal reveal-d3">
            <a href="https://www.instagram.com/drsemakoc/" target="_blank" rel="noopener" aria-label="Instagram">{IC['instagram']}</a>
            <a href="https://www.facebook.com/doc.dr.SemaKoc" target="_blank" rel="noopener" aria-label="Facebook">{IC['facebook']}</a>
            <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{IC['message-circle']}</a>
          </div>
          <div class="lp-form reveal reveal-d3" style="margin-top: var(--space-6);">{wa_form('Hızlı Randevu Talebi', 'Genel Bilgi ve Randevu', subject_select=True)}</div>
        </div>
        <div class="contact-cards">
          <div class="ccard reveal">{IC['map-pin']}<b>Adres</b><p>Tekelioğlu Cad. 1947. Sk. No: 29/3<br>Muratpaşa / Antalya</p><a class="maplink" href="{MAPQ}" target="_blank" rel="noopener">Haritada Görüntüle {IC['arrow-up-right']}</a></div>
          <div class="ccard reveal reveal-d1">{IC['phone']}<b>Telefon</b><a href="{TEL}">{PHONE}</a></div>
          <div class="ccard reveal reveal-d2">{IC['mail']}<b>E-Posta</b><a href="mailto:{MAIL}">{MAIL}</a></div>
          <div class="ccard reveal reveal-d3">{IC['clock-3']}<b>Çalışma Saatleri</b><p>Güncel çalışma saatleri ve müsaitlik için lütfen telefonla bilgi alınız.</p></div>
        </div>
      </div>
      <div class="map-embed reveal"><iframe src="{MAPE}" title="Klinik konumu haritası" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
    </div>
  </section>
</main>
{footer(R)}'''


L10N = {
 'en': dict(code='EN', lang='en', title='Assoc. Prof. Sema Koç, MD | ENT and Head-Neck Surgery, Antalya',
  meta='Assoc. Prof. Sema Koç, MD provides diagnosis and treatment in rhinoplasty, ENT, head and neck surgery, vertigo and audiology in Antalya.',
  eyebrow='Assoc. Prof. Sema Koç, MD · ENT and Head-Neck Surgery · Antalya',
  h1='More than twenty years of experience, <em>with academic rigor.</em>',
  lead='Diagnosis and treatment in rhinoplasty, ENT diseases, head and neck surgery, vertigo and audiology. Contact our clinic to schedule an examination and evaluation appointment.',
  cta1='Request an Appointment', cta2='Treatments',
  note='Consultations are available in Turkish, English, Russian and Ukrainian.',
  stats=[('20', '+', 'Years of Experience'), ('4.8', '', 'Google Rating'), ('529', '', 'Google Reviews'), ('9', '', 'Areas of Expertise')],
  gtitle='Google Reviews',
  sec_eyebrow='Areas of Expertise', sec_h2='Diagnosis and treatment services',
  services=['Rhinoplasty', 'Revision Rhinoplasty', 'Ultrasonic Piezo Rhinoplasty', 'Nasal Tip Surgery (Tip Plasty)', 'Septoplasty', 'Snoring and Sleep Apnea', 'Ear and Hearing Surgery', 'Head and Neck Surgery', 'Vertigo (Dizziness)'],
  c_eyebrow='Contact and Appointments', c_h2='Contact us for an examination appointment',
  c_addr='Address', c_phone='Phone', c_mail='E-mail', c_hours='Working Hours',
  c_hours_txt='Please call for current availability.', c_map='View on Map',
  disclaimer='The content on this site is for informational purposes only and does not replace a medical examination or diagnosis. Please consult your physician for diagnosis and treatment.',
  rights='All rights reserved.', back='Back to Top ↑', wa_label='Chat on WhatsApp',
  nav=dict(home='Home', about='About', treat='Treatments', blog='Blog', contact='Contact', all='All Treatments →', drop='Treatments and Procedures')),
 'ru': dict(code='RU', lang='ru', title='Доц. д-р Сема Коч | ЛОР и хирургия головы и шеи, Анталья',
  meta='Доц. д-р Сема Коч: диагностика и лечение в области ринопластики, ЛОР-заболеваний, хирургии головы и шеи, вертиго и аудиологии в Анталье.',
  eyebrow='Доц. д-р Сема Коч · ЛОР и хирургия головы и шеи · Анталья',
  h1='Более двадцати лет опыта, <em>с академической точностью.</em>',
  lead='Диагностика и лечение: ринопластика, ЛОР-заболевания, хирургия головы и шеи, вертиго и аудиология. Свяжитесь с клиникой, чтобы записаться на осмотр и консультацию.',
  cta1='Записаться на приём', cta2='Направления',
  note='Консультации проводятся на турецком, английском, русском и украинском языках.',
  stats=[('20', '+', 'Лет опыта'), ('4.8', '', 'Рейтинг Google'), ('529', '', 'Отзывов в Google'), ('9', '', 'Направлений')],
  gtitle='Отзывы Google',
  sec_eyebrow='Направления', sec_h2='Диагностика и лечение',
  services=['Ринопластика', 'Ревизионная ринопластика', 'Ультразвуковая пьезо-ринопластика', 'Пластика кончика носа', 'Септопластика', 'Храп и апноэ сна', 'Хирургия уха и слуха', 'Хирургия головы и шеи', 'Вертиго (головокружение)'],
  c_eyebrow='Контакты и запись', c_h2='Свяжитесь с нами для записи на приём',
  c_addr='Адрес', c_phone='Телефон', c_mail='Эл. почта', c_hours='Часы работы',
  c_hours_txt='Актуальное расписание уточняйте по телефону.', c_map='Показать на карте',
  disclaimer='Материалы сайта носят информационный характер и не заменяют медицинский осмотр и диагностику. По вопросам диагностики и лечения обращайтесь к врачу.',
  rights='Все права защищены.', back='Наверх ↑', wa_label='Написать в WhatsApp',
  nav=dict(home='Главная', about='О враче', treat='Направления', blog='Блог', contact='Контакты', all='Все направления →', drop='Направления и процедуры')),
 'ua': dict(code='UA', lang='uk', title='Доц. д-р Сема Коч | ЛОР та хірургія голови і шиї, Анталія',
  meta='Доц. д-р Сема Коч: діагностика та лікування у сферах ринопластики, ЛОР-захворювань, хірургії голови та шиї, вертиго й аудіології в Анталії.',
  eyebrow='Доц. д-р Сема Коч · ЛОР та хірургія голови і шиї · Анталія',
  h1='Понад двадцять років досвіду, <em>з академічною точністю.</em>',
  lead="Діагностика та лікування: ринопластика, ЛОР-захворювання, хірургія голови та шиї, вертиго й аудіологія. Зв'яжіться з клінікою, щоб записатися на огляд і консультацію.",
  cta1='Записатися на прийом', cta2='Напрямки',
  note='Консультації проводяться турецькою, англійською, російською та українською мовами.',
  stats=[('20', '+', 'Років досвіду'), ('4.8', '', 'Рейтинг Google'), ('529', '', 'Відгуків у Google'), ('9', '', 'Напрямків')],
  gtitle='Відгуки Google',
  sec_eyebrow='Напрямки', sec_h2='Діагностика та лікування',
  services=['Ринопластика', 'Ревізійна ринопластика', 'Ультразвукова пєзо-ринопластика', 'Пластика кінчика носа', 'Септопластика', 'Хропіння та апное сну', 'Хірургія вуха та слуху', 'Хірургія голови та шиї', 'Вертиго (запаморочення)'],
  c_eyebrow='Контакти та запис', c_h2="Зв'яжіться з нами для запису на прийом",
  c_addr='Адреса', c_phone='Телефон', c_mail='Ел. пошта', c_hours='Години роботи',
  c_hours_txt='Актуальний розклад уточнюйте за телефоном.', c_map='Показати на мапі',
  disclaimer='Матеріали сайту мають інформаційний характер і не замінюють медичний огляд та діагностику. З питань діагностики та лікування звертайтеся до лікаря.',
  rights='Усі права захищено.', back='Догори ↑', wa_label='Написати у WhatsApp',
  nav=dict(home='Головна', about='Про лікаря', treat='Напрямки', blog='Блог', contact='Контакти', all='Усі напрямки →', drop='Напрямки та процедури')),
}

def lang_page(key):
    L = L10N[key]
    R = '../'
    drops = '\n'.join(f'<a href="{R}{t["slug"]}">{L["services"][i]}</a>' for i, t in enumerate(T))
    icons9 = ['scan-face', 'wind', 'activity', 'scan-face', 'wind', 'moon-star', 'ear', 'ribbon', 'orbit']
    svc = '\n'.join(
        f'''<a class="svc reveal{' reveal-d' + str(i % 4) if i % 4 else ''}" href="{R}{t['slug']}"><div class="badge">{IC[icons9[i]]}</div><p class="card-t">{L['services'][i]}</p><span class="more">{IC['arrow-right']}</span></a>'''
        for i, t in enumerate(T))
    stats = '\n'.join(
        f'<div class="stat"><b data-count="{v}"{f" data-suffix={sx}" if sx else ""}>0</b><span>{lb}</span></div>'
        for v, sx, lb in L['stats'])
    return f'''<!doctype html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{L['title']}</title>
<meta name="description" content="{L['meta']}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%230B0B0C'/%3E%3Ctext x='50' y='68' font-family='Georgia,serif' font-size='52' fill='%23D6B879' text-anchor='middle'%3ESK%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{R}assets/style.css">
</head>
<body>
<header class="site-head">
  <div class="wrap head-in">
    <a class="wordmark" href="{R}index.html"><strong>Doç. Dr. Sema Koç</strong><span>{'ENT & Head-Neck Surgery' if key == 'en' else 'ЛОР · Хирургия головы и шеи' if key == 'ru' else 'ЛОР · Хірургія голови і шиї'}</span></a>
    <nav class="site-nav" id="siteNav">
      <a href="#top" class="active">{L['nav']['home']}</a>
      <a href="#services">{L['nav']['treat']}</a>
      <a href="#contact">{L['nav']['contact']}</a>
      {lang_menu(R, L['code'])}
    </nav>
    <div style="display:flex; align-items:center; gap:.7rem;">
      <a class="head-cta" href="#contact">{IC['phone']}<span>{L['cta1']}</span></a>
      <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" aria-label="Menu">{IC['menu']}</button>
    </div>
  </div>
</header>
<main id="top">
  <section class="hero3">
    <video class="kbvid" autoplay muted loop playsinline preload="metadata" poster="https://drsemakoc.com/hero/hero_poster_desktop.jpg" aria-hidden="true">
      <source src="https://drsemakoc.com/hero/hero_mobile.mp4" media="(max-width: 768px)" type="video/mp4">
      <source src="https://drsemakoc.com/hero/hero_desktop.mp4" type="video/mp4">
    </video>
    <div class="ov" aria-hidden="true"></div>
    <div class="wrap hero3-in hero3-center">
      <p class="eyebrow fade-rise">{L['eyebrow']}</p>
      <h1 class="fade-rise-d1">{L['h1']}</h1>
      <p class="lead fade-rise-d2">{L['lead']}</p>
      <div class="hero-ctas fade-rise-d3">
        <a class="btn btn-gold" href="#contact">{L['cta1']} {IC['arrow-right']}</a>
        <a class="btn btn-glass liquid-glass" href="#services">{L['cta2']}</a>
      </div>
      <p class="hero-note fade-rise-d4">{IC['globe']} {L['note']}</p>
    </div>
    <div class="wrap hero3-stats fade-rise-d4">{hero_cards(L['stats'], L.get('gtitle', 'Google Reviews'))}</div>
  </section>
  <section class="sec sec-stone" id="services">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">{L['sec_eyebrow']}</p>
        <h2 class="reveal reveal-d1">{L['sec_h2']}</h2>
      </div>
      <div class="svc-grid">{svc}</div>
    </div>
  </section>
  <section class="sec dark-sec" id="contact">
    <div class="wrap contact-grid">
      <div>
        <p class="eyebrow reveal">{L['c_eyebrow']}</p>
        <h2 class="reveal reveal-d1">{L['c_h2']}</h2>
        <div class="socials reveal reveal-d3">
          <a href="https://www.instagram.com/drsemakoc/" target="_blank" rel="noopener" aria-label="Instagram">{IC['instagram']}</a>
          <a href="https://www.facebook.com/doc.dr.SemaKoc" target="_blank" rel="noopener" aria-label="Facebook">{IC['facebook']}</a>
          <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{IC['message-circle']}</a>
        </div>
      </div>
      <div class="contact-cards">
        <div class="ccard reveal">{IC['map-pin']}<b>{L['c_addr']}</b><p>Tekelioğlu Cad. 1947. Sk. No: 29/3<br>Muratpaşa / Antalya</p><a class="maplink" href="{MAPQ}" target="_blank" rel="noopener">{L['c_map']} {IC['arrow-up-right']}</a></div>
        <div class="ccard reveal reveal-d1">{IC['phone']}<b>{L['c_phone']}</b><a href="{TEL}">{PHONE}</a></div>
        <div class="ccard reveal reveal-d2">{IC['mail']}<b>{L['c_mail']}</b><a href="mailto:{MAIL}">{MAIL}</a></div>
        <div class="ccard reveal reveal-d3">{IC['clock-3']}<b>{L['c_hours']}</b><p>{L['c_hours_txt']}</p></div>
      </div>
    </div>
  </section>
</main>
<footer class="site-foot">
  <div class="wrap foot-in">
    <p class="disclaimer">{IC['shield-check']}<span>{L['disclaimer']}</span></p>
    <div class="foot-base">
      <span>© 2026 Doç. Dr. Sema Koç. {L['rights']}</span>
      <a href="#top">{L['back']}</a>
    </div>
  </div>
</footer>
<a class="wa-cta" href="{WA}" target="_blank" rel="noopener" aria-label="{L['wa_label']}">{IC['message-circle']}<span>WhatsApp</span></a>
<script src="{R}assets/main.js"></script>
</body>
</html>'''

LP = {
 'our-services/rhinoplasty/': dict(slug='lp/rinoplasti/',
  h1='Burnunuz nefesinizdir;', em='estetik, bunun üzerine kurulur.',
  sub='Doç. Dr. Sema Koç rinoplastiyi iki soruyla planlar: Nasıl görünmeli, nasıl nefes almalı? Yirmi yılı aşkın deneyim ve piezo teknolojisiyle.',
  chips=[('activity', 'Piezo teknolojisi'), ('clock-3', 'Aynı gün taburcu mümkün'), ('user', 'Kişiye özel planlama')],
  benefits=[('activity', 'Ultrasonik Piezo Teknolojisi', 'Kemik şekillendirme ses dalgalarıyla yapılır; çevre dokular korunur, süreç hassas ilerler.'),
            ('wind', 'Estetik + Fonksiyon Birlikte', 'Deviasyon ve konka sorunları aynı operasyonda ele alınabilir; hem görünüm hem nefes hedeflenir.'),
            ('graduation-cap', 'Akademik Birikim', 'Doçentlik unvanı ve yirmi yılı aşkın cerrahi deneyimle her aşamada hekim takibi.'),
            ('calendar-check', 'Düzenli Kontrol Takibi', 'Operasyon sonrası kontrol muayeneleriyle iyileşme süreci planlı şekilde izlenir.')]),
 'revizyon-burun-estetigi/': dict(slug='lp/revizyon-burun-estetigi/',
  h1='İkinci ameliyat, ilkinden daha çok', em='ustalık ister.',
  sub='Revizyon rinoplasti doku bilgisi ve dürüstlük ister. Neyin mümkün olduğunu muayenede açıkça konuşur, planı birlikte kurarsınız.',
  chips=[('microscope', 'Ayrıntılı ön değerlendirme'), ('activity', 'Kıkırdak planlaması'), ('user', 'Kişiye özel yaklaşım')],
  benefits=[('microscope', 'Kapsamlı Analiz', 'Doku durumu, skar yapısı ve solunum fonksiyonu birlikte değerlendirilir; plan buna göre yapılır.'),
            ('activity', 'Kıkırdak Kaynağı Planlaması', 'Gerekli durumlarda kulak veya kaburga kıkırdağı kullanımı önceden planlanır ve sizinle paylaşılır.'),
            ('graduation-cap', 'Deneyimli Cerrah', 'Revizyon vakaları ileri deneyim ister; süreç doçent düzeyinde akademik birikimle yürütülür.'),
            ('shield-check', 'Gerçekçi Bilgilendirme', 'Neyin mümkün olduğu, neyin olmadığı muayenede açıkça konuşulur; karar birlikte verilir.')]),
 'ultrasonik-piezo-burun-estetigi/': dict(slug='lp/piezo-rinoplasti/',
  h1='Kemiğe çekiç değil,', em='ses dalgası.',
  sub='Ultrasonik piezo, kemiği milimetrik şekillendirir ve yumuşak dokuyu korur. Uygunluğunuz muayenede netleşir.',
  chips=[('audio-lines', 'Ultrasonik şekillendirme'), ('shield-check', 'Yumuşak doku korunur'), ('microscope', 'Hassas planlama')],
  benefits=[('audio-lines', 'Ses Dalgasıyla Cerrahi', 'Kemik, ultrasonik titreşimle kesilir ve şekillendirilir; mekanik darbe kullanılmaz.'),
            ('shield-check', 'Doku Dostu Yaklaşım', 'Yumuşak dokuya temas sınırlıdır; ödem ve morarma seyri takip sürecinde düzenli izlenir.'),
            ('scan-face', 'İnce Detay Kontrolü', 'Burun sırtı ve kemik hattında milimetrik düzeltmeler hedeflenir.'),
            ('calendar-check', 'Planlı İyileşme', 'Kontrol randevularıyla süreç adım adım takip edilir.')]),
 'burun-ucu-estetigi-tipplasti/': dict(slug='lp/burun-ucu-estetigi/',
  h1='Bütün burnu değil,', em='sadece ucunu düzeltmek.',
  sub='Mesele yalnızca burun ucuysa, tipplasti kemiğe dokunmayan kısa bir seçenektir. Doğru aday olup olmadığınız muayenede netleşir.',
  chips=[('scan-face', 'Kemiğe müdahale yok'), ('clock-3', 'Daha kısa operasyon'), ('heart-pulse', 'Genellikle hızlı toparlanma')],
  benefits=[('scan-face', 'Sınırlı Kapsam', 'Yalnızca uç kıkırdakları düzenlenir; burun sırtına ve kemiğe dokunulmaz.'),
            ('clock-3', 'Kısa Süreç', 'Operasyon klasik rinoplastiden kısa sürer; iyileşme genellikle daha rahattır.'),
            ('user', 'Doğru Aday Analizi', 'Tipplasti mi, rinoplasti mi? Muayenede dürüstçe söylenir; gereksiz kapsam önerilmez.'),
            ('calendar-check', 'Takip Güvencesi', 'Kontrol muayeneleriyle sonuç düzenli izlenir.')]),
 'septoplasti/': dict(slug='lp/septoplasti/',
  h1='Tek taraflı nefes almaya', em='alışmak zorunda değilsiniz.',
  sub='Sürekli tıkanıklığın görünmez nedeni çoğu zaman septum eğriliğidir. Tanı, kısa bir endoskopik muayeneyle konur.',
  chips=[('wind', 'Solunum odaklı cerrahi'), ('shield-check', 'Tampon yerine splint'), ('clock-3', 'Kısa sürede günlük yaşam')],
  benefits=[('wind', 'Nefese Odaklı', 'Amaç estetik değil işlevdir: solunum yolunun açılması hedeflenir.'),
            ('shield-check', 'Güncel Teknik', 'Klasik tampon yerine genellikle silikon splint veya eriyebilen materyaller kullanılır.'),
            ('activity', 'Konka ile Birlikte', 'Gerekliyse konka küçültme aynı seansta planlanabilir.'),
            ('calendar-check', 'Hızlı Dönüş', 'Hastaların çoğu kısa sürede günlük yaşamına döner; süreç kontrollerle izlenir.')]),
 'our-services/snooring-sleep-apnea/': dict(slug='lp/horlama-uyku-apnesi/',
  h1='Horlama bir ses değil,', em='vücudunuzdan bir uyarıdır.',
  sub='Tanı uyku testiyle netleşir; tedavi tıkanıklığın gerçek kaynağına göre planlanır. Bütün seçenekler tek klinikte.',
  chips=[('moon-star', 'Uyku testi ile tanı'), ('activity', 'Cerrahi + cerrahi dışı seçenekler'), ('user', 'Kişiye göre plan')],
  benefits=[('moon-star', 'Doğru Tanı', 'Polisomnografi (uyku testi) ile apnenin varlığı ve şiddeti netleştirilir.'),
            ('wind', 'Tıkanıklığın Kaynağı', 'Burun, damak ve dil kökü ayrı ayrı değerlendirilir; tedavi kaynağa göre planlanır.'),
            ('activity', 'Geniş Seçenek Yelpazesi', 'Yaşam tarzı düzenlemesinden PAP cihazına ve cerrahiye kadar seçenekler birlikte konuşulur.'),
            ('heart-pulse', 'Sağlık Öncelikli', 'Tedavi edilmeyen apnenin kalp-damar riskleri hakkında açık bilgilendirme yapılır.')]),
 'our-services/ear-hearing-treatments/': dict(slug='lp/kulak-isitme/',
  h1='İyi duymak, iyi yaşamaktır;', em='işitmenizi ertelemeyin.',
  sub='Doç. Dr. Sema Koç hem KBB uzmanı hem uzman odyologtur: testi yorumlayan ve tedaviyi planlayan aynı hekim olur.',
  chips=[('ear', 'Mikroskopik muayene'), ('audio-lines', 'Odyometri + timpanometri'), ('graduation-cap', 'Uzman odyolog değerlendirmesi')],
  benefits=[('graduation-cap', 'Çift Uzmanlık', 'Doç. Dr. Sema Koç hem KBB uzmanı hem uzman odyologtur; işitme testleri hekim gözüyle yorumlanır.'),
            ('ear', 'Kapsamlı Kulak Cerrahisi', 'Kulak zarı onarımı (timpanoplasti) ve orta kulak cerrahisi kliniğimizde planlanır.'),
            ('audio-lines', 'Tam Test Altyapısı', 'Odyometri ve timpanometri ile kaybın tipi ve derecesi netleştirilir.'),
            ('user', 'Nedene Göre Tedavi', 'Kulak kiri birikiminden otoskleroza kadar her tablo kendi yöntemiyle ele alınır.')]),
 'our-services/head-neck-cancer/': dict(slug='lp/bas-boyun-cerrahisi/',
  h1='Sesiniz üç haftadır kısıksa,', em='vücudunuz size bir şey söylüyor.',
  sub='Erken tanı, tedavi seçeneklerini genişletir. Endoskopik muayeneden tedavi planına kadar süreç tek elden yönetilir.',
  chips=[('ribbon', 'Erken tanı odağı'), ('microscope', 'Robotik cerrahi eğitimi'), ('heart-pulse', 'Multidisipliner yaklaşım')],
  benefits=[('ribbon', 'Erken Tanı Vurgusu', 'Uzayan belirtiler endoskopik muayene ve gerekli görüntülemeyle vakit kaybetmeden değerlendirilir.'),
            ('microscope', 'Robotik Cerrahi Eğitimi', 'Da Vinci Transoral Robotik Cerrahi eğitimi (2012), uygun vakalarda değerlendirmeye katkı sağlar.'),
            ('heart-pulse', 'Multidisipliner Plan', 'Tedavi; cerrahi, radyoterapi ve onkoloji ekipleriyle birlikte planlanır.'),
            ('user', 'Hasta Yanında', 'Tanıdan takibe her aşamada aynı hekimle ilerlersiniz.')]),
 'our-services/antalya-vertigo-tedavisi/': dict(slug='lp/vertigo/',
  h1='Dünya dönmüyor;', em='iç kulağınız yanlış sinyal veriyor olabilir.',
  sub='En sık neden kristal kaymasıdır ve doğru manevrayla çoğu hasta kısa sürede rahatlar. Tanı, denge ve işitme testleriyle konur.',
  chips=[('orbit', 'Epley ve Semont manevraları'), ('audio-lines', 'İşitme + denge testleri'), ('user', 'Nedene yönelik tedavi')],
  benefits=[('orbit', 'Manevra Tedavisi', 'BPPV tanısında Epley ve Semont manevraları muayenehane koşullarında uygulanır.'),
            ('audio-lines', 'Denge + İşitme Birlikte', 'Uzman odyolog birikimiyle işitme ve denge testleri birlikte yorumlanır.'),
            ('heart-pulse', 'Rehabilitasyon Desteği', 'Gerekli hastalarda vestibüler rehabilitasyon programı planlanır.'),
            ('shield-check', 'Ayırıcı Tanı', 'Meniere, vestibüler nörit ve migren ilişkili vertigo ayrımı titizlikle yapılır.')]),
}

LP_TAGS = {
 'our-services/rhinoplasty/': ['burun'],
 'revizyon-burun-estetigi/': ['burun'],
 'ultrasonik-piezo-burun-estetigi/': ['burun'],
 'burun-ucu-estetigi-tipplasti/': ['burun'],
 'septoplasti/': ['burun', 'horlama'],
 'our-services/snooring-sleep-apnea/': ['horlama', 'geniz'],
 'our-services/ear-hearing-treatments/': ['kulak'],
 'our-services/head-neck-cancer/': ['basboyun'],
 'our-services/antalya-vertigo-tedavisi/': ['vertigo'],
}
NOSE_LP = {'our-services/rhinoplasty/', 'revizyon-burun-estetigi/', 'ultrasonik-piezo-burun-estetigi/', 'burun-ucu-estetigi-tipplasti/', 'septoplasti/'}

def lp_page(t):
    lp = LP[t['slug']]
    R = '../../'
    chips = '\n'.join(f'<span class="chip-inline liquid-glass">{IC[i]} {lbl}</span>' for i, lbl in lp['chips'])
    bens = '\n'.join(
        f'<article class="svc reveal{" reveal-d" + str(i % 2) if i % 2 else ""}"><div class="badge">{IC[ic]}</div><p class="card-t">{h}</p><p>{txt}</p></article>'
        for i, (ic, h, txt) in enumerate(lp['benefits']))
    faq_html = '\n'.join(
        f'<details class="reveal"><summary>{q} {IC["x"]}</summary><div class="faq-a">{a}</div></details>'
        for q, a in t['faq'])
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t['faq']]}, ensure_ascii=False)
    stars5 = ''.join(IC['star'] for _ in range(5))
    head_html = head(R, f"{t['nav']} | Doç. Dr. Sema Koç, Antalya", lp['sub'])
    return f'''{head_html}
<header class="site-head solid">
  <div class="wrap head-in">
    <a class="wordmark" href="#top"><strong>Doç. Dr. Sema Koç</strong><span>KBB ve Baş-Boyun Cerrahisi</span></a>
    <div style="display:flex; align-items:center; gap:1rem;">
      <a href="{TEL}" class="lp-phone">{IC['phone']} <span>{PHONE}</span></a>
      <a class="head-cta" href="#randevu">{IC['calendar-check']}<span>Randevu Al</span></a>
    </div>
  </div>
</header>
<main id="top">
  <section class="hero3 lp-hero">
    <video class="kbvid" autoplay muted loop playsinline preload="metadata" poster="https://drsemakoc.com/hero/hero_poster_desktop.jpg" aria-hidden="true">
      <source src="https://drsemakoc.com/hero/hero_mobile.mp4" media="(max-width: 768px)" type="video/mp4">
      <source src="https://drsemakoc.com/hero/hero_desktop.mp4" type="video/mp4">
    </video>
    <div class="ov" aria-hidden="true"></div>
    <div class="wrap hero3-in hero3-center">
      <span class="lp-badge liquid-glass fade-rise">{IC['award']} Doç. Dr. Sema Koç · 20+ Yıl Deneyim</span>
      <h1 class="fade-rise-d1">{lp['h1']} <em>{lp['em']}</em></h1>
      <p class="lead fade-rise-d2">{lp['sub']}</p>
      <div class="lp-chips fade-rise-d2">{chips}</div>
      <div class="hero-ctas fade-rise-d3">
        <a class="btn btn-gold" href="#randevu">Randevu Talebi {IC['arrow-right']}</a>
        <a class="btn btn-glass liquid-glass" href="{TEL}">{IC['phone']} Hemen Arayın</a>
      </div>
      <p class="hero-note fade-rise-d4"><span class="stars">{stars5}</span> 4,8 · 529 Google yorumu</p>
    </div>
  </section>

  {reviews_sec(LP_TAGS[t["slug"]], n=10)}

  <section class="sec">
    <div class="wrap about-grid">
      <div class="about-copy">
        <p class="eyebrow reveal">Hekiminiz</p>
        <h2 class="reveal reveal-d1">Doç. Dr. Sema Koç</h2>
        <p class="big reveal reveal-d2">Kulak Burun Boğaz ve Baş-Boyun Cerrahisi Uzmanı, Uzman Odyolog. Yirmi yılı aşkın hekimlik deneyimini Antalya'daki kliniğinde sürdürmektedir.</p>
        <ul class="focus-list reveal reveal-d3">
          <li>{IC['check']} Gazi Üniversitesi Tıp Fakültesi, 2001</li>
          <li>{IC['check']} Da Vinci Transoral Robotik Cerrahi Eğitimi, 2012</li>
          <li>{IC['check']} Doçentlik, Kulak Burun Boğaz, 2013</li>
          <li>{IC['check']} Odyoloji Yüksek Lisansı · Uzman Odyolog, 2014</li>
        </ul>
      </div>
      <img class="about-photo reveal reveal-d2" src="{R}assets/img/portre-2.jpg" alt="Doç. Dr. Sema Koç" loading="lazy">
    </div>
  </section>

  {gallery_sec(R)}

  {ba_sec(R) if t['slug'] in NOSE_LP else ''}

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">Neden Bu Klinik?</p>
        <h2 class="reveal reveal-d1">{t['nav']} sürecinde sizi ne bekliyor?</h2>
      </div>
      <div class="svc-grid lp-ben">{bens}</div>
    </div>
  </section>

  {steps_sec().replace('sec-stone', '')}

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head">
        <p class="eyebrow reveal">Sık Sorulan Sorular</p>
        <h2 class="reveal reveal-d1">Merak ettikleriniz</h2>
      </div>
      <div class="faq">{faq_html}</div>
    </div>
  </section>

  <section class="sec dark-sec" id="randevu">
    <div class="wrap lp-form-wrap">
      <p class="eyebrow reveal">Randevu Talebi</p>
      <h2 class="reveal reveal-d1">İlk adımı atın: muayene ile başlayalım</h2>
      <p class="reveal reveal-d2" style="color: var(--text-inv-soft); max-width: 34em;">Bilgilerinizi bırakın, WhatsApp üzerinden randevunuzu birlikte planlayalım. Görüşmeler Türkçe, İngilizce, Rusça ve Ukraynaca yapılabilmektedir.</p>
      <div class="lp-form reveal reveal-d2">{wa_form('Randevu Talebi', t['nav'])}</div>
      <p class="reveal reveal-d3" style="margin-top: var(--space-4);"><a class="btn btn-ghost" href="{TEL}">{IC['phone']} {PHONE}</a></p>
    </div>
  </section>
</main>
<footer class="site-foot">
  <div class="wrap foot-in" style="gap: var(--space-4);">
    <p class="disclaimer">{IC['shield-check']}<span>Bu sayfa bilgilendirme amaçlıdır; hekim muayenesinin yerini tutmaz. Tanı ve tedavi için lütfen hekiminize başvurunuz. Yorumlar, Google Haritalar üzerinde kamuya açık değerlendirmelerdir.</span></p>
    <div class="foot-base">
      <span>© 2026 Doç. Dr. Sema Koç · {ADDR}</span>
      <a href="{TEL}">{PHONE}</a>
    </div>
  </div>
</footer>
<a class="wa-cta" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp ile iletişime geçin">{IC['message-circle']}<span>WhatsApp</span></a>
<div class="call-bar">
  <a class="btn btn-gold" href="{TEL}">{IC['phone']} Hemen Ara</a>
  <a class="btn btn-glass liquid-glass" href="#randevu">Randevu Al</a>
</div>
<script type="application/ld+json">{faq_ld}</script>
<script src="{R}assets/main.js"></script>
</body>
</html>'''


# ---------------- YAZ ----------------
def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(content)

if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(f'{OUT}/assets/fonts', exist_ok=True)
os.makedirs(f'{OUT}/assets/img', exist_ok=True)

shutil.copy(f'{BASE}/style.css', f'{OUT}/assets/style.css')
shutil.copy(f'{BASE}/main.js', f'{OUT}/assets/main.js')
for f in os.listdir(f'{SCRATCH}/site/assets'):
    shutil.copy(f'{SCRATCH}/site/assets/{f}', f'{OUT}/assets/fonts/{f}')
for f in os.listdir(f'{SCRATCH}/opt_img'):
    shutil.copy(f'{SCRATCH}/opt_img/{f}', f'{OUT}/assets/img/{f}')

write('index.html', home_page())
write('about-us/index.html', about_page())
write('sunulan-hizmetler/index.html', services_page())
write('blog/index.html', blog_page())
write('bas-donmesi-nedenleri-belirtileri-ve-tedavisi/index.html', post_page())
write('contacts/index.html', contact_page())
for k in L10N:
    write(k + '/index.html', lang_page(k))
for t in T:
    write(LP[t['slug']]['slug'] + 'index.html', lp_page(t))
for t in T:
    write(t['slug'] + 'index.html', treatment_page(t))

n = sum(len(fs) for _, _, fs in os.walk(OUT))
print(f'✓ {n} dosya üretildi → {OUT}')
