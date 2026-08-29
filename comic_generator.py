#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KIZILELMA MU'NUN UYANIŞI - Görsel Üreticisi
Stability AI API ile 144 panel görsel oluşturma
"""

import os
import json
import requests
import base64
import time
from pathlib import Path
from typing import Dict, List, Optional

# Konfigürasyon
API_KEY = "sk-LV93j042XmKNMhjl7ADaCG2pSU77yXrm4OnRWf4eyDIsQbe7"
API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
OUTPUT_DIR = r"C:\Users\Semih\.gemini\antigravity\scratch\kizilelma_comic\images"

# Karakterler
CHARACTERS = {
    "uras_yetiskin": "young man with messy long dark hair with a braid, green eyes, light stubble, dark grey hoodie, orange carrot-fit pants, anime manga style",
    "uras_cocuk": "5-year-old boy with messy dark hair, green eyes, worn-out village clothes, anime manga style",
    "deren": "20-year-old girl with long dark brown hair, brown eyes, black sleeveless top, blue jeans, anime manga style",
    "maya": "20-year-old girl with long fiery red hair, green eyes, dark blue and silver mystical robe with ancient runes, anime manga style",
    "alisan": "22-year-old guy with short dark hair, clean-shaven, athletic build, black t-shirt, blue jeans, anime manga style",
    "yagiz": "22-year-old guy with slicked-back blonde hair, blue eyes, arrogant smirk, black leather jacket, white t-shirt, blue jeans, anime manga style"
}

# Mekanlar
LOCATIONS = {
    "koy_yagmur": "Turkish eastern village house, heavy rain, stormy night, dramatic rainy weather, mountains",
    "hastane": "sterile white hospital room, medical equipment, heart monitor, clinical environment, ICU",
    "yemekhane": "university cafeteria, crowded, fluorescent lights, tables and chairs, busy",
    "kutuphane": "old university library interior, 5th floor window, books, shelves, night time",
    "yurt_odasi": "messy dorm room, night time, bed, minimal furniture, dim lighting",
    "otobus": "tour bus interior, crowded with students, seats, windows showing mountain road",
    "uludag_tesis": "ski resort, snowy mountain peaks, cable cars, cafe, winter landscape, Uludag mountain",
    "bozkir": "vast dark steppe, dry grass, wind, misty atmosphere, ethereal, Turkish landscape"
}

class ComicImageGenerator:
    def __init__(self, api_key: str, output_dir: str):
        self.api_key = api_key
        self.output_dir = output_dir
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        
        # Klasörü oluştur
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        
    def generate_image(self, prompt: str, filename: str) -> bool:
        """Stability AI ile görsel oluştur"""
        filepath = os.path.join(self.output_dir, filename)
        
        # Zaten varsa atla
        if os.path.exists(filepath):
            print(f"⏭️  ATLANDI (zaten var): {filename}")
            return True
        
        try:
            body = {
                "steps": 30,
                "width": 512,
                "height": 512,
                "seed": 0,
                "cfg_scale": 7.0,
                "samples": 1,
                "text_prompts": [
                    {
                        "text": prompt,
                        "weight": 1.0
                    }
                ]
            }
            
            print(f"⏳ Oluşturuluyor: {filename}")
            print(f"   Prompt: {prompt[:80]}...")
            
            response = self.session.post(
                API_URL,
                headers=self.headers,
                json=body,
                timeout=120
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("artifacts"):
                    img_data = base64.b64decode(data["artifacts"][0]["base64"])
                    
                    with open(filepath, "wb") as f:
                        f.write(img_data)
                    
                    print(f"✅ Kaydedildi: {filename}")
                    return True
                else:
                    print(f"❌ Artifact yok: {filename}")
                    return False
            else:
                print(f"❌ API Hatası ({response.status_code}): {filename}")
                print(f"   Yanıt: {response.text[:200]}")
                return False
                
        except Exception as e:
            print(f"❌ Hata: {e}")
            return False
    
    def create_panel_prompt(self, page_num: int, panel_num: int, panel_data: Dict) -> str:
        """Panel için prompt oluştur"""
        
        # Sayfa spesifik promptlar
        page_prompts = {
            1: {
                1: f"Turkish eastern village house at night, heavy rain, stormy clouds, dramatic rainy weather, mountains, 8k, anime manga style, dark atmosphere",
                2: f"Interior of village house, father with shotgun at door protecting family, mother holding child, desperate expressions, candlelight, anime manga style",
                3: f"Wooden door shattering violently, masked armed men entering, dynamic action, firelight, smoke, anime manga style, dramatic",
                4: f"Father falling backward after being shot, shotgun dropping, gunfire in background, pain expression, dramatic, anime manga style",
                5: f"Mother shielding child with body, bullets penetrating, sacrifice moment, blood, darkening, anime manga style, tragic",
                6: f"Small boy lying on floor surrounded by blood, silent and still, dark tragic scene, anime manga style, dramatic lighting"
            },
            2: {
                1: f"Sterile white hospital room, child in bed with bandages, heart rate monitor, dim blue clinical lighting, anime manga style",
                2: f"Doctor and nurses gathered around hospital bed, desperate expressions, white environment, medical drama, anime manga style",
                3: f"Close-up of flatlining heart rate monitor, green line on black screen, dramatic shadows, anime manga style",
                4: f"Medical staff with bowed heads, emotional moment, tragedy, somber atmosphere, hospital room, anime manga style",
                5: f"Soul leaving boy's body, ethereal transition, fading lines, dark mist, spiritual effect, anime manga style",
                6: f"Swirling dark mist, void, unknown, fading consciousness, blank white and grey void, anime manga style"
            },
            3: {
                1: f"Vast dark steppe landscape, dry grass, wind, misty eerie mood, Turkish landscape, anime manga style",
                2: f"Small boy standing in center of steppe, black smoke rising from chest wound, fearless expression, anime manga style",
                3: f"Ground shaking, earth trembling, dust clouds, violent wind, ominous atmosphere, steppe, anime manga style",
                4: f"Close-up of boy's focused determined eyes, dark aura surrounding, mystical energy, green eyes glowing, anime manga style",
                5: f"Terrifying pitch-black Alpha Wolf (Bozkurt) running towards camera, aggressive attacking pose, glowing red eyes, anime manga style, 8k",
                6: f"Extreme close-up of red glowing eyes of monstrous wolf meeting green eyes of boy, intense standoff, supernatural, anime manga style"
            },
            8: {
                1: f"Kalabalık üniversite yemekhane, saate kilitlenmiş genç kız, fluorescent lights, masalar, anime manga style",
                2: f"Genç adamın zihninde karanlık orman ve yaratık canlanıyor, mystical vision, anime manga style",
                3: f"Üniversite yemekhane'de arkadaş Alişan, atletik yapı, siyah tişört, uyarı verirken, anime manga style",
                4: f"Güzel kız Deren masaya yaklaşıyor, kahve saç, kahve gözler, siyah kolsuz üst, mavi kot, anime manga style",
                5: f"Deren tam tepesinde, gülümsüyor, flirt ediyor, anime manga style",
                6: f"Genç adamın gözleri büyüyor, şaşkınlık ifadesi, anime manga style"
            },
            20: {
                4: f"Mysterious girl with long fiery red hair, green eyes, dark blue and silver mystical robe with ancient runes, mystical aura, anime manga style, 8k"
            }
        }
        
        # Sayfa ve panel-spesifik prompt varsa kullan
        if page_num in page_prompts and panel_num in page_prompts[page_num]:
            return page_prompts[page_num][panel_num]
        
        # Varsayılan prompt oluştur
        base_prompt = "anime manga style, dramatic, cinematic lighting, 8k"
        
        # Karakterleri ekle
        if panel_data.get("characters"):
            chars = [CHARACTERS.get(c, c) for c in panel_data["characters"] if c in CHARACTERS]
            if chars:
                base_prompt += ", " + ", ".join(chars)
        
        # Mekanı ekle
        if panel_data.get("location"):
            base_prompt += f", {panel_data['location']}"
        
        # Açıklama ekle
        if panel_data.get("description"):
            base_prompt += f", {panel_data['description']}"
        
        return base_prompt
    
    def generate_all_panels(self):
        """Tüm panelleri oluştur"""
        print("=" * 70)
        print("🔴 KIZILELMA MU'NUN UYANIŞI - GÖRSEL ÜRETIMI BAŞLANIYOR")
        print("=" * 70)
        print(f"📁 Çıktı klasörü: {self.output_dir}\n")
        
        # Senaryo verisini yükle
        scenario_file = r"C:\Users\Semih\.gemini\antigravity\scratch\kizilelma_comic\data\bolum1_senaryo.json"
        
        try:
            with open(scenario_file, 'r', encoding='utf-8') as f:
                scenario_data = json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Senaryo dosyası bulunamadı: {scenario_file}")
            print("📝 Örnek paneller oluşturuluyor...\n")
            
            # Örnek paneller
            pages = {
                1: {
                    "title": "KANLI GEÇMİŞ",
                    "panels": [
                        {"panel": i, "characters": [], "location": "koy_yagmur", "description": f"Panel {i}"}
                        for i in range(1, 7)
                    ]
                },
                2: {
                    "title": "ÖLÜMÜN EŞİĞİ",
                    "panels": [
                        {"panel": i, "characters": [], "location": "hastane", "description": f"Panel {i}"}
                        for i in range(1, 7)
                    ]
                },
                3: {
                    "title": "KARANLIK BOZKIR",
                    "panels": [
                        {"panel": i, "characters": [], "location": "bozkir", "description": f"Panel {i}"}
                        for i in range(1, 7)
                    ]
                }
            }
            scenario_data = {"pages": [{"page": page, **data} for page, data in pages.items()]}
        
        generated = 0
        failed = 0
        
        # Sayfaları işle
        for page_data in scenario_data.get("pages", []):
            page_num = page_data.get("page", 0)
            page_title = page_data.get("title", "")
            
            print(f"\n📖 SAYFA {page_num}: {page_title}")
            print("-" * 70)
            
            # Panelleri işle
            for panel_data in page_data.get("panels_data", []):
                panel_num = panel_data.get("panel", 0)
                
                # Dosya adı
                if page_data.get("is_splash"):
                    filename = f"page{page_num}_splash.jpg"
                else:
                    filename = f"page{page_num}_panel{panel_num}.jpg"
                
                # Prompt oluştur
                prompt = self.create_panel_prompt(page_num, panel_num, panel_data)
                
                # Görsel oluştur
                if self.generate_image(prompt, filename):
                    generated += 1
                else:
                    failed += 1
                
                # Rate limiting - Stability AI için gerekli
                time.sleep(2)
        
        print("\n" + "=" * 70)
        print(f"✅ TAMAMLANDI!")
        print(f"   ✓ Oluşturulan: {generated}")
        print(f"   ✗ Başarısız: {failed}")
        print(f"   📁 Konumu: {self.output_dir}")
        print("=" * 70)

def main():
    """Ana fonksiyon"""
    
    if not API_KEY or API_KEY == "sk-":
        print("❌ HATA: API anahtarı geçersiz!")
        return
    
    generator = ComicImageGenerator(API_KEY, OUTPUT_DIR)
    generator.generate_all_panels()

if __name__ == "__main__":
    main()
