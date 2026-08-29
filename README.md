# 🔴 KIZILELMA MU'NUN UYANIŞI
## İnteraktif Türk Çizgi Romanı | Interactive Turkish Comic Series

**Bölüm 1: Mistik Bağ ve Kampüs Günleri**

![Status](https://img.shields.io/badge/Status-In%20Development-blue)
![Pages](https://img.shields.io/badge/Pages-24-red)
![Panels](https://img.shields.io/badge/Panels-144-orange)

---

## 📖 Proje Hakkında

**KIZILELMA MU'NUN UYANIŞI**, bir genç adamın sırlarına sahip uyanışını anlatan dramatik bir Türk çizgi romanıdır. Bölüm 1'de, köy evinden başlayan trajik bir olaydan kurtulacak Uras'ın, üniversite kampüsündeki maceralarına ve mistik güçleriyle tanışmasına tanık oluyoruz.

---

## 🎮 HIZLI BAŞLAT

```bash
# 1. Repository'yi klonla
git clone https://github.com/Sedge16/kizilelma-mucusu.git
cd kizilelma-mucusu

# 2. Web sunucusunu başlat
python -m http.server 8000

# 3. Tarayıcıda aç
# http://localhost:8000
```

---

## 📁 Proje Yapısı

```
kizilelma-mucusu/
├── index.html              # Ana sayfa - Başla buradan!
├── style.css               # Comic-book stili
├── script.js               # İnteraktif oynatıcı
├── generate_images.py      # Görsel oluşturucu (Stable Diffusion)
├── images/                 # Panel görselleri (144 görsel)
└── README.md               # Dokümantasyon
```

---

## 👥 Karakterler

| Karakter | Yaş | Açıklama |
|----------|-----|----------|
| **Uras** | 5→20 | Dağınık koyu saç, yeşil gözler, mistik güçler |
| **Deren** | 20 | Güçlü kişiliğe sahip kız, kahve saç |
| **Maya** | 20 | Telekinetik güçler, mistik cübbe, kızıl saç |
| **Alişan** | 22 | Arkadaş, atletik, loyal |
| **Yağız** | 22 | Antagonist, alaycı, arrogant |

---

## 📚 Bölüm 1 Özeti (24 SAYFA)

**Sayfalar 1-2:** Kanlı köy saldırısı, Uras'ın vurulması  
**Sayfalar 3-7:** Ruhsal alemde Alfa Kurt, mistik bağ, mucize uyanış  
**Sayfalar 8-15:** Üniversitede Deren ile tanışma, 5 kattan inişi, viral video  
**Sayfalar 16-19:** Otobüse binişi, Yağız ile çatışma, termos kazası  
**Sayfalar 20-24:** Kayak tesisine varış, mistik Maya ile karşılaşma, dağda kırmızı gözler  

---

## 🎮 Kontroller

- **→ / SONRAKI SAYFA** - Sonraki sayfaya git
- **← / ÖNCEKİ SAYFA** - Önceki sayfaya git
- **ZOOM** - Sayfayı büyüt/küçült (50% - 200%)

---

## 🚀 Görselleri Oluştur (İsteğe Bağlı)

Eğer kendi görsellerin oluşturulmak istiyorsan:

```bash
# API anahtarını ayarla (Stability AI)
export STABILITY_API_KEY='your-key-here'

# Tüm 144 paneli oluştur (~30-60 dakika)
python generate_images.py
```

**Not:** API anahtarı yoksa placeholder görseller otomatik kullanılır.

---

## 📝 Senaryo Format

Her panel şu öğeleri içerir:
- Karakterler
- Diyalog balonları
- Ses efektleri (GÜMMM!, PAT!, vb)
- Mekân açıklaması
- Panel numarası

---

## 🎨 Özellikler

✅ **Comic-Book Tasarımı** - Klasik panel sınırları ve diyalog balonları  
✅ **Responsive Layout** - Mobil, tablet ve desktop uyumlu  
✅ **İnteraktif Navigasyon** - Sayfa geçişleri ve zoom  
✅ **Anime/Manga Stili** - Dramatik sahneler  
✅ **Türkçe Interface** - Tüm metinler Türkçe  

---

## 🔧 Teknoloji Stack

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Backend:** Python 3.8+ (Görsel oluşturma)
- **AI:** Stable Diffusion XL API
- **Format:** Responsive Web + Future PDF Export

---

## 📊 İstatistikler

| Metrik | Sayı |
|--------|------|
| **Sayfalar** | 24 |
| **Panel/Sayfa** | 6 |
| **Toplam Panel** | 144 |
| **Karakterler** | 6 |
| **Mekanlar** | 8 |
| **Diyalog** | 40+ |
| **Ses Efekti** | 20+ |

---

## 🐛 Sorun Giderme

**Görseller yüklenmedi?**
→ `generate_images.py` ile oluştur veya `images/` klasörünü kontrol et

**API anahtarı geçersiz?**
→ Stability AI'dan yeni anahtar al: https://platform.stability.ai/

**Sayfa yavaş yükleniyor?**
→ Cache'i temizle: Ctrl+Shift+Del

---

## 📞 İletişim

GitHub: [@Sedge16](https://github.com/Sedge16)

---

**Sürüm:** 1.0 Beta | **Güncelleme:** 2026-08-29

*"Soğuk... Her şey çok soğuk..."* - Uras
