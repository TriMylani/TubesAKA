import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi rekursif untuk menghitung BMI
def calculate_bmi_recursive(weight, height, index=0, results=None):
    if results is None:
        results = []
    if index >= len(weight):
        return results
    bmi = weight[index] / ((height[index] / 100) ** 2)
    results.append(bmi)
    return calculate_bmi_recursive(weight, height, index + 1, results)

# Fungsi iteratif untuk menghitung BMI
def calculate_bmi_iterative(weight, height):
    results = []
    for i in range(len(weight)):
        bmi = weight[i] / ((height[i] / 100) ** 2)
        results.append(bmi)
    return results

# Fungsi untuk menentukan kategori BMI
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 <= bmi < 29.9:
        return "Berat badan berlebih"
    else:
        return "Obesitas"

# Grafik untuk menyimpan data
names = []
weights = []
heights = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(names, recursive_times, label='Recursive', marker='o', linestyle='-')
    plt.plot(names, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative')
    plt.xlabel('Input (Person)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)  # Jangan blok program saat grafik ditampilkan
    plt.pause(0.1)  # Memberikan waktu bagi grafik untuk ditampilkan

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Person", "Weight (kg)", "Height (cm)", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(names), len(weights), len(heights), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([names[i], weights[i], heights[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        name = input("Masukkan nama (atau ketik 'selesai' untuk keluar): ")
        if name.lower() == 'selesai':
            print("Program selesai. Terima kasih!")
            break

        weight = float(input("Masukkan berat badan (kg): "))
        height = float(input("Masukkan tinggi badan (cm): "))

        names.append(name)
        weights.append(weight)
        heights.append(height)

        # Hitung BMI
        bmi = weight / ((height / 100) ** 2)
        category = get_bmi_category(bmi)
        print(f"Hi {name}, BMI Anda adalah {bmi:.2f}. Kategori: {category}.")

        # Ukur waktu eksekusi algoritma rekursif
        start_time = time.time()
        calculate_bmi_recursive([weight], [height])
        recursive_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma iteratif
        start_time = time.time()
        calculate_bmi_iterative([weight], [height])
        iterative_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan nilai yang valid!")
