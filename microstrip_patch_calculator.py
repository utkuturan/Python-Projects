import math

def calculate_microstrip_patch(freq_hz, er, h_m):
    c = 3e8
    Z0 = 50.0 # Hedef Empedans (Ohm)

    # 1. YAMA GENİŞLİĞİ (WIDTH)
    W = (c / (2 * freq_hz)) * math.sqrt(2 / (er + 1))
    
    # 2. EFEKTİF DİELEKTRİK SABİTİ (Epsilon eff)
    e_eff = ((er + 1) / 2) + ((er - 1) / 2) * ((1 + 12 * (h_m / W)) ** -0.5)
    
    # 3. UZUNLUK UZAMASI (Delta L)
    numerator = (e_eff + 0.3) * (W / h_m + 0.264)
    denominator = (e_eff - 0.258) * (W / h_m + 0.8)
    delta_L = h_m * 0.412 * (numerator / denominator)
    
    # 4. YAMA UZUNLUĞU (LENGTH)
    L_eff = c / (2 * freq_hz * math.sqrt(e_eff))
    L = L_eff - 2 * delta_L
    
    # ---------------------------------------------------------
    # EKSİK OLAN KISIMLAR (BESLEME HESABI)
    # ---------------------------------------------------------
    
    # 5. 50 OHM HAT GENİŞLİĞİ (W_feed) - Wheeler/Hammerstad Formülü
    A = (Z0 / 60) * math.sqrt((er + 1) / 2) + ((er - 1) / (er + 1)) * (0.23 + 0.11 / er)
    B = 377 * math.pi / (2 * Z0 * math.sqrt(er))
    
    w_h_ratio = (2 / math.pi) * (B - 1 - math.log(2 * B - 1) + ((er - 1) / (2 * er)) * (math.log(B - 1) + 0.39 - 0.61 / er))
    W_feed = w_h_ratio * h_m
    
    # 6. INSET FEED DERİNLİĞİ (Fi veya y0)
    # Anten kenar empedansı (R_in) hesabı (Yaklaşık)
    R_in_edge = 90 * (er**2 / (er - 1)) * (L / W)**2 
    
    # 50 Ohm noktasına ne kadar girmeliyiz? (Cos^2 kuralı)
    y0 = (L / math.pi) * math.acos(math.sqrt(Z0 / R_in_edge))
    
    # 7. INSET GAP (G) - Genellikle W_feed'in yarısı veya h kadar alınır
    G_gap = W_feed / 2

    return {
        "W_patch": W * 1000,
        "L_patch": L * 1000,
        "W_feed": W_feed * 1000,
        "Fi_depth": y0 * 1000,
        "G_gap": G_gap * 1000,
        "W_gnd": (W * 1000) + 20, 
        "L_gnd": (L * 1000) + 20
    }

# --- PARAMETRELER (FR-4 @ 2.4 GHz) ---
frequency = 2.4e9
epsilon_r = 4.3
height = 0.0016 # 1.6 mm

results = calculate_microstrip_patch(frequency, epsilon_r, height)

print(f"--- 2.4 GHz FR-4 CST Parametreleri ---")
print(f"W_patch  (Yama Genişliği): {results['W_patch']:.2f} mm")
print(f"L_patch  (Yama Uzunluğu):  {results['L_patch']:.2f} mm")
print(f"--- BESLEME (FEED) ---")
print(f"W_feed   (Yol Genişliği):  {results['W_feed']:.2f} mm")
print(f"Fi_depth (Yarık Derinliği):{results['Fi_depth']:.2f} mm")
print(f"G_gap    (Yarık Genişliği):{results['G_gap']:.2f} mm")
