import math

# Sabitler
c = 3e8  # Işık hızı (m/s)
fr = 2.4e9  # Hedef Frekans (Hz)

# FR-4 Malzeme Özellikleri
er = 4.3  # Dielektrik sabiti
h = 0.0016  # Yükseklik (metre) -> 1.6mm

# 1. Genişlik (Width) Hesabı
W = (c / (2 * fr)) * math.sqrt(2 / (er + 1))

# 2. Efektif Dielektrik Sabiti (Epsilon eff)
e_eff = ((er + 1) / 2) + ((er - 1) / 2) * (1 + 12 * (h / W)) ** -0.5

# 3. Delta L (Uzunluk Uzaması)
delta_L = h * 0.412 * ((e_eff + 0.3) * (W / h + 0.264)) / ((e_eff - 0.258) * (W / h + 0.8))

# 4. Efektif Uzunluk (L_eff)
L_eff = c / (2 * fr * math.sqrt(e_eff))

# 5. Gerçek Uzunluk (Length)
L = L_eff - 2 * delta_L

print(f"--- 2.4 GHz FR-4 Yama Anten Boyutları ---")
print(f"Genişlik (W): {W * 1000:.2f} mm")
print(f"Uzunluk (L):  {L * 1000:.2f} mm")
print(f"Ground Plane (Wg, Lg): {W*1000 + 20:.2f} mm, {L*1000 + 20:.2f} mm (Yaklaşık)")
