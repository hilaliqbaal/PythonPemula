import numpy as np

print("===== Kode Mencari Regresi Linear Sederhana ====")

print("""
      Rumus umum = 

      Y = a + bX
      Y = nilai prediksi
      X = Nilai input
      a = intercept
      b = gradien
      """)

n = int(input("Masukkan Jumlah Pasangan X dan Y : "))

if n < 2:
    print("Minimal harus ada 2 pasangan data untuk regresi linear.")
    exit()

X = []
Y = []

print("Masukkan data X dan Y satu per satu:")

for i in range(n):
    x = float(input(f"X[{i+1}] = "))
    y = float(input(f"Y[{i+1}] = "))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

mean_X = np.mean(X)
mean_Y = np.mean(Y)

b = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X)**2)
a = mean_Y - b * mean_X

print("\n=== Hasil Regresi Linear ===")
print(f"Nilai a (intercept): {a}")
print(f"Nilai b (slope): {b}")
print(f"Persamaan regresi: Y = {a:.2f} + {b:.2f}X")

X_pred = float(input("\nMasukkan nilai X untuk prediksi Y: "))
Y_pred = a + b * X_pred
print(f"Prediksi Y untuk X = {X_pred} adalah Y = {Y_pred}")
