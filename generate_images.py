#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KIZILELMA MU'NUN UYANIŞI - Otomatik Çizgi Roman Görsel Üreticisi
Bölüm 1 için 24 sayfa, her sayfada 6 panel (toplam 144 panel)
Stable Diffusion API ile AI görsel üretimi
"""

import os
import json
import requests
from pathlib import Path
from typing import List, Dict, Tuple
import time

# Konfigürasyon
CONFIG = {
    "api_endpoint": "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
    "api_key": os.getenv("STABILITY_API_KEY", "your-api-key-here"),
    "output_dir": "images",
    "batch_size": 5,
    "quality": "high",
    "style": "anime manga style, dramatic, cinematic lighting, 8k"
}

# Karakter referans tanımları
CHARACTERS = {
    "uras_yetiskin": "young man with messy long dark hair with a braid, green eyes, light stubble, dark grey hoodie, orange carrot-fit pants",
    "uras_cocuk": "5-year-old boy with messy dark hair, green eyes, worn-out village clothes",
    "deren": "20-year-old girl with long dark brown hair, brown eyes, black sleeveless top, blue jeans",
    "maya": "20-year-old girl with long fiery red hair, green eyes, dark blue and silver mystical robe with ancient runes",
    "alisan": "22-year-old guy with short dark hair, clean-shaven, athletic build, black t-shirt, blue jeans",
    "yagiz": "22-year-old guy with slicked-back blonde hair, blue eyes, arrogant smirk, black leather jacket, white t-shirt, blue jeans"
}

# Mekan referans tanımları
LOCATIONS = {
    "koy_yagmur": "Turkish eastern village house at night, heavy rain, stormy clouds, dramatic rainy weather",
    "hastane": "sterile white hospital room, medical equipment, heart monitor, clinical environment",
    "yemekhane": "university cafeteria, crowded, fluorescent lights, tables and chairs",
    "kutuphane": "old university library, 5th floor window, books, shelves",
    "yurt_odasi": "messy dorm room, night time, bed, minimal furniture, dim lighting",
    "otobus": "tour bus interior, crowded with students, seats, windows showing mountain road",
    "uludag_tesis": "ski resort, snowy mountain peaks, cable cars, cafe, winter landscape",
    "bozkir": "vast dark steppe, dry grass, wind, misty atmosphere, ethereal"
}

# Panel senaryo veri tabanı (Bölüm 1)
PANELS_DATA = {
    1: {
        "title": "KANLI GEÇMİŞ",
        "panels": [
            {
                "num": 1,
                "ref_char": None,
                "ref_location": "koy_yagmur",
                "prompt_suffix": "house exterior, sağanak yağmur, silah sesleri anlatılan, gece, ıssız köy",
                "sound": "GÜMMM! GÜMMM!"
            },
            {
                "num": 2,
                "ref_char": ["uras_cocuk"],
                "ref_location": "koy_yagmur",
                "prompt_suffix": "interior, mother holding child, father with shotgun at door, desperate expressions, candlelight",
                "sound": None
            },
            {
                "num": 3,
                "ref_char": None,
                "ref_location": "koy_yagmur",
                "prompt_suffix": "wooden door shattering violently, masked armed men entering, dynamic action, firelight",
                "sound": "GÜMMM!"
            },
            {
                "num": 4,
                "ref_char": None,
                "ref_location": "koy_yagmur",
                "prompt_suffix": "father falling backward, shotgun dropping, gunfire in background, pain expression, dramatic",
                "sound": "PAT! PAT! PAT!"
            },
            {
                "num": 5,
                "ref_char": ["uras_cocuk"],
                "ref_location": "koy_yagmur",
                "prompt_suffix": "mother shielding child with body, bullets penetrating, sacrifice, blood, darkening screen",
                "sound": None
            },
            {
                "num": 6,
                "ref_char": ["uras_cocuk"],
                "ref_location": "koy_yagmur",
                "prompt_suffix": "small boy lying on floor surrounded by blood, silent and still, dark tragic scene",
                "sound": None
            }
        ]
    },
    2: {
        "title": "ÖLÜMÜN EŞİĞİ",
        "panels": [
            {
                "num": 1,
                "ref_char": ["uras_cocuk"],
                "ref_location": "hastane",
                "prompt_suffix": "child in hospital bed with bandages, heart rate monitor beeping, dim blue clinical lighting",
                "sound": "Biiip... Biiip..."
            },
            {
                "num": 2,
                "ref_char": None,
                "ref_location": "hastane",
                "prompt_suffix": "doctor and nurses gathered around bed with desperate expressions, white environment",
                "sound": None
            },
            {
                "num": 3,
                "ref_char": None,
                "ref_location": "hastane",
                "prompt_suffix": "close-up of flatlining heart rate monitor, green line on black screen, dramatic shadows",
                "sound": "BİİİİİİP"
            },
            {
                "num": 4,
                "ref_char": None,
                "ref_location": "hastane",
                "prompt_suffix": "medical staff with bowed heads, emotional moment, tragedy, somber atmosphere",
                "sound": None
            },
            {
                "num": 5,
                "ref_char": ["uras_cocuk"],
                "ref_location": "hastane",
                "prompt_suffix": "soul leaving boy's body, ethereal transition, fading lines, dark mist, spiritual effect",
                "sound": None
            },
            {
                "num": 6,
                "ref_char": None,
                "ref_location": None,
                "prompt_suffix": "swirling dark mist, void, unknown, fading consciousness, blank white and grey void",
                "sound": None
            }
        ]
    },
    3: {
        "title": "KARANLIK BOZKIR VE ALFA KURT",
        "panels": [
            {
                "num": 1,
                "ref_char": None,
                "ref_location": "bozkir",
                "prompt_suffix": "vast steppe landscape, dark atmosphere, wind blowing grass, misty eerie mood",
                "sound": None
            },
            {
                "num": 2,
                "ref_char": ["uras_cocuk"],
                "ref_location": "bozkir",
                "prompt_suffix": "small boy standing in center of steppe, black smoke rising from chest wound, fearless expression",
                "sound": None
            },
            {
                "num": 3,
                "ref_char": None,
                "ref_location": "bozkir",
                "prompt_suffix": "ground shaking, earth trembling, dust clouds, violent wind, ominous atmosphere",
                "sound": "ÇATIRT!"
            },
            {
                "num": 4,
                "ref_char": ["uras_cocuk"],
                "ref_location": "bozkir",
                "prompt_suffix": "close-up of boy's focused determined eyes, dark aura surrounding, mystical energy",
                "sound": None
            },
            {
                "num": 5,
                "ref_char": None,
                "ref_location": "bozkir",
                "prompt_suffix": "terrifying pitch-black Alpha Wolf (Bozkurt) running towards camera, aggressive attacking pose, glowing red eyes",
                "sound": "GÜM GÜM GÜM!"
            },
            {
                "num": 6,
                "ref_char": ["uras_cocuk"],
                "ref_location": "bozkir",
                "prompt_suffix": "extreme close-up of red glowing eyes of monstrous wolf meeting green eyes of boy, intense standoff, supernatural",
                "sound": None
            }
        ]
    }
    # ... Diğer sayfalar benzer şekilde devam edecek
}

class ComicImageGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        
    def generate_image(self, prompt: str, filename: str) -> bool:
        """Stable Diffusion API ile görsel üret"""
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
            
            response = self.session.post(
                CONFIG["api_endpoint"],
                headers=self.headers,
                json=body,
                timeout=60
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("artifacts"):
                    import base64
                    img_data = base64.b64decode(data["artifacts"][0]["base64"])
                    os.makedirs(CONFIG["output_dir"], exist_ok=True)
                    
                    filepath = os.path.join(CONFIG["output_dir"], filename)
                    with open(filepath, "wb") as f:
                        f.write(img_data)
                    
                    print(f"✓ Oluşturuldu: {filename}")
                    return True
            else:
                print(f"✗ Hata ({response.status_code}): {filename}")
                print(f"  Yanıt: {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ API Hatası: {e}")
            return False
    
    def create_panel_prompt(self, page_num: int, panel_data: Dict) -> str:
        """Panel için prompt oluştur"""
        base_prompt = CONFIG["style"]
        
        # Karakterleri ekle
        if panel_data.get("ref_char"):
            chars = [CHARACTERS.get(c, c) for c in panel_data["ref_char"]]
            base_prompt += ", " + ", ".join(chars)
        
        # Mekanı ekle
        if panel_data.get("ref_location"):
            location = LOCATIONS.get(panel_data["ref_location"], "")
            base_prompt += ", " + location
        
        # Panel spesifik açıklamayı ekle
        if panel_data.get("prompt_suffix"):
            base_prompt += ", " + panel_data["prompt_suffix"]
        
        return base_prompt
    
    def generate_chapter_1(self):
        """Bölüm 1 için tüm görselleri oluştur"""
        print("=" * 60)
        print("KIZILELMA MU'NUN UYANIŞI - Bölüm 1 Görsel Üretimi Başlatılıyor")
        print("=" * 60)
        
        generated = 0
        failed = 0
        
        for page_num, page_data in PANELS_DATA.items():
            print(f"\n📖 SAYFA {page_num}: {page_data['title']}")
            print("-" * 40)
            
            for panel in page_data["panels"]:
                panel_num = panel["num"]
                prompt = self.create_panel_prompt(page_num, panel)
                filename = f"page{page_num}_panel{panel_num}.jpg"
                
                print(f"  Panel {panel_num}: ", end="", flush=True)
                
                if self.generate_image(prompt, filename):
                    generated += 1
                else:
                    failed += 1
                
                # API rate limiting
                time.sleep(1)
        
        print("\n" + "=" * 60)
        print(f"✓ Tamamlandı! Oluşturulan: {generated}, Başarısız: {failed}")
        print(f"📁 Görseller 'images/' klasöründe kaydedildi")
        print("=" * 60)

def main():
    """Ana fonksiyon"""
    
    # API anahtarı kontrolü
    api_key = CONFIG["api_key"]
    if api_key == "your-api-key-here":
        print("⚠️  HATA: Stability AI API anahtarı ayarlanmamış!")
        print("\nKullanım:")
        print("  export STABILITY_API_KEY='your-key-here'")
        print("  python generate_images.py")
        return
    
    # Görsel üreticisini başlat
    generator = ComicImageGenerator(api_key)
    
    # Bölüm 1'i oluştur
    generator.generate_chapter_1()
    
    print("\n💡 İpucu: Görselleri index.html'de görmek için:")
    print("   python -m http.server 8000")
    print("   http://localhost:8000")

if __name__ == "__main__":
    main()
