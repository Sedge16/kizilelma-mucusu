// KIZILELMA MU'NUN UYANIŞI - Çizgi Roman Viewer
// Interactive Comic Book System

const TOTAL_PAGES = 24;
let currentPage = 1;
let zoomLevel = 100;

// Tüm sayfaların senaryo verileri
const pagesData = {
  1: {
    title: "SAYFA 1: KANLI GEÇMİŞ",
    panels: [
      {
        number: 1,
        image: "images/page1_panel1.jpg",
        dialogue: [],
        sound: "GÜMMM! GÜMMM!",
        description: "Sağanak yağmur altında Doğu'da ıssız bir köy evi. Pencerelerden vuran silah sesleri."
      },
      {
        number: 2,
        image: "images/page1_panel2.jpg",
        dialogue: [
          { speaker: "BABA", text: "Sakın çıkmayın dışarı!" }
        ],
        sound: "",
        description: "İçeride: Küçük Uras annesinin kucağında titriyor. Babası tüfekle kapıyı tutuyor."
      },
      {
        number: 3,
        image: "images/page1_panel3.jpg",
        dialogue: [],
        sound: "GÜMMM!",
        description: "Kapı kırılıyor. Maskeli adamlar içeri dalıyor."
      },
      {
        number: 4,
        image: "images/page1_panel4.jpg",
        dialogue: [],
        sound: "PAT! PAT! PAT!",
        description: "Yakın Plan: Babanın vurulup yere düşüşü."
      },
      {
        number: 5,
        image: "images/page1_panel5.jpg",
        dialogue: [
          { speaker: "İÇ SES URAS", text: "Soğuk... Her şey çok soğuk..." }
        ],
        sound: "",
        description: "Anne, Uras'ın üzerine siper oluyor. Kurşunlar anneyi delip Uras'ın göğsüne saplanıyor."
      },
      {
        number: 6,
        image: "images/page1_panel6.jpg",
        dialogue: [],
        sound: "",
        description: "Uras'ın kanlar içinde yere serildiği son kare. Sessiz panel."
      }
    ]
  },
  2: {
    title: "SAYFA 2: ÖLÜMÜN EŞİĞİ",
    panels: [
      {
        number: 1,
        image: "images/page2_panel1.jpg",
        dialogue: [],
        sound: "Biiip... Biiip... Biiiiiiip",
        description: "Bembeyaz steril hastane odası. Monitör yavaşça düzleşiyor."
      },
      {
        number: 2,
        image: "images/page2_panel2.jpg",
        dialogue: [
          { speaker: "BAŞHEKIM", text: "Ailesini kaybettiğimiz yetmiyormuş gibi bu çocuk da gidiyor... Vücudundaki mermiler hayati organları darmadağın etmiş. Yaşamaz... Tıbben imkansız!" }
        ],
        sound: "",
        description: "Başhekim umutsuzca konuşuyor."
      },
      {
        number: 3,
        image: "images/page2_panel3.jpg",
        dialogue: [],
        sound: "BİİİİİİP",
        description: "Monitördeki çizgi tamamen düzleşiyor."
      },
      {
        number: 4,
        image: "images/page2_panel4.jpg",
        dialogue: [],
        sound: "",
        description: "Doktorlar başlarını eğiyor, hemşireler gözyaşlarını tutuyor. Sessiz panel."
      },
      {
        number: 5,
        image: "images/page2_panel5.jpg",
        dialogue: [],
        sound: "",
        description: "Uras'ın ruhu bedeninden ayrılıyormuş gibi bir his. Çizgiler bulanıklaşıyor. Geçiş paneli."
      },
      {
        number: 6,
        image: "images/page2_panel6.jpg",
        dialogue: [],
        sound: "",
        description: "Yerini koyu bir sis ve karartan ekran alıyor."
      }
    ]
  }
  // Diğer sayfalar benzer şekilde devam edecek...
};

// Sayfayı render et
function renderPage(pageNum) {
  const page = pagesData[pageNum];
  if (!page) return;

  const comicPage = document.getElementById('comicPage');
  comicPage.innerHTML = `
    <div class="page-title">${page.title}</div>
    <div class="panels-container">
      ${page.panels.map(panel => `
        <div class="panel">
          <div class="panel-number">${panel.number}</div>
          <img src="${panel.image}" alt="Panel ${panel.number}" class="panel-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22250%22 height=%22250%22%3E%3Crect fill=%22%23f0f0f0%22 width=%22250%22 height=%22250%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 font-size=%2216%22 fill=%22%23999%22 text-anchor=%22middle%22 dy=%22.3em%22%3EPanel ${panel.number}%3C/text%3E%3C/svg%3E'">
          
          ${panel.sound ? `<div class="sound-effect">${panel.sound}</div>` : ''}
          
          ${panel.dialogue.map(d => `
            <div class="panel-dialogue">
              <div class="dialogue-speaker">${d.speaker}</div>
              <div class="dialogue-text">${d.text}</div>
            </div>
          `).join('')}
        </div>
      `).join('')}
    </div>
  `;

  // Güncellemeleri güncelle
  document.getElementById('pageCounter').textContent = `SAYFA ${pageNum}`;
  document.getElementById('prevBtn').disabled = pageNum === 1;
  document.getElementById('nextBtn').disabled = pageNum === TOTAL_PAGES;

  // Sayfayı başa kaydır
  window.scrollTo(0, 0);
}

// Navigasyon
document.getElementById('prevBtn').addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    renderPage(currentPage);
  }
});

document.getElementById('nextBtn').addEventListener('click', () => {
  if (currentPage < TOTAL_PAGES) {
    currentPage++;
    renderPage(currentPage);
  }
});

// Zoom kontrolü
document.getElementById('zoomSlider').addEventListener('input', (e) => {
  zoomLevel = e.target.value;
  document.getElementById('zoomValue').textContent = zoomLevel;
  document.getElementById('comicPage').style.transform = `scale(${zoomLevel / 100})`;
  document.getElementById('comicPage').style.transformOrigin = 'top center';
});

// Klavye navigasyonu
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight') {
    document.getElementById('nextBtn').click();
  } else if (e.key === 'ArrowLeft') {
    document.getElementById('prevBtn').click();
  }
});

// İlk sayfayı yükle
renderPage(1);
