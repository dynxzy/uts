def pilih_barang(daftar_barang, kapasitas):
    """Memilih barang secara greedy berdasarkan prioritas."""
    # Langkah 1: urutkan prioritas menurun, berat menaik sebagai penentu seri
    terurut = sorted(daftar_barang, key=lambda b: (-b["prioritas"], b["berat"]))

    terpilih = []
    sisa = kapasitas

    # Langkah 2: ambil barang selama masih muat
    for barang in terurut:
        if barang["berat"] <= sisa:
            terpilih.append(barang)
            sisa -= barang["berat"]

    return terurut, terpilih, sisa


def cetak_tabel(judul, data):
    print(judul)
    print(f"{'No':<4}{'Nama Barang':<16}{'Berat (kg)':<12}{'Prioritas':<10}")
    print("-" * 42)
    for i, b in enumerate(data, start=1):
        print(f"{i:<4}{b['nama']:<16}{b['berat']:<12}{b['prioritas']:<10}")
    print()


if __name__ == "__main__":
    kapasitas = 15  # kg

    barang = [
        {"nama": "Laptop",      "berat": 6, "prioritas": 5},
        {"nama": "Obat-obatan", "berat": 2, "prioritas": 10},
        {"nama": "Payung",      "berat": 1, "prioritas": 2},
        {"nama": "Makanan",     "berat": 4, "prioritas": 8},
        {"nama": "Buku",        "berat": 2, "prioritas": 3},
        {"nama": "Air minum",   "berat": 5, "prioritas": 9},
        {"nama": "Senter",      "berat": 1, "prioritas": 6},
        {"nama": "Pakaian",     "berat": 3, "prioritas": 7},
    ]

    print(f"Kapasitas tas: {kapasitas} kg\n")
    cetak_tabel("Daftar barang awal:", barang)

    terurut, terpilih, sisa = pilih_barang(barang, kapasitas)

    cetak_tabel("Setelah diurutkan berdasarkan prioritas:", terurut)

    print("Proses seleksi:")
    sisa_proses = kapasitas
    for b in terurut:
        if b["berat"] <= sisa_proses:
            sisa_proses -= b["berat"]
            print(f"  [AMBIL]  {b['nama']:<12} berat {b['berat']} kg -> sisa kapasitas {sisa_proses} kg")
        else:
            print(f"  [LEWAT]  {b['nama']:<12} berat {b['berat']} kg > sisa kapasitas {sisa_proses} kg")
    print()

    cetak_tabel("Barang terpilih:", terpilih)

    total_berat = sum(b["berat"] for b in terpilih)
    total_prioritas = sum(b["prioritas"] for b in terpilih)
    print(f"Total berat       : {total_berat} kg dari {kapasitas} kg")
    print(f"Sisa kapasitas    : {sisa} kg")
    print(f"Total prioritas   : {total_prioritas}")