import json
import cv2
import qrcode

# Mapping QR codes ke password admin
ADMIN_QR_PASSWORD = {
    '1962427124102841': 'Samson123',
    '1962424311223344': 'Wilfredo006',
    '1962425724110227': 'Bram123',
    '1962429724102887': 'Levina19',
    '1962422624124678': 'Firafasya123',
    # tambahkan lagi di sini
}

def scan_qr():
    """
    Fungsi untuk memindai QR code menggunakan kamera.
    Mengembalikan data QR code sebagai string jika berhasil, atau None jika gagal.
    """
    detector = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Tidak dapat membuka kamera.")
        return None

    print("Silakan scan QR code. Tekan 'q' untuk keluar.")

    qr_data = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Tidak dapat membaca frame dari kamera.")
            break

        # Deteksi dan dekode QR code
        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None and data:
            qr_data = data.strip()
            print(f"QR Code terdeteksi: {qr_data}")

            # Pastikan bbox valid dan konversi ke integer
            bbox = bbox.astype(int)
            for i in range(len(bbox)):
                pt1 = tuple(bbox[i][0])
                pt2 = tuple(bbox[(i + 1) % len(bbox)][0])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            # Tampilkan frame dengan kotak
            cv2.imshow("Scan QR Code", frame)
            cv2.waitKey(1000)
            break

        cv2.imshow("Scan QR Code", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return qr_data

def akun():
    """
    Fungsi utama untuk login sebagai admin atau pembeli.
    """
    produk = ambil_dari_json()
    while True:
        role = input("Apakah anda 'admin' atau 'pembeli'? (ketik 'exit' untuk keluar): ").strip().lower()
        if role == "admin":
            qr_number = scan_qr()
            if qr_number is None:
                print("Gagal memindai QR code.")
                continue
            if qr_number in ADMIN_QR_PASSWORD:
                password = input("Masukkan password admin: ").strip()
                if password == ADMIN_QR_PASSWORD[qr_number]:
                    print("Login berhasil")
                    produk = tambah_produk()
                else:
                    print("Password salah")
            else:
                print("QR Code admin tidak dikenali.")
        elif role == "pembeli":
            vending_machine(produk)
        elif role == "exit":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def simpan_ke_json(produk):
    """
    Menyimpan data produk ke file JSON.
    """
    with open("produk.json", "w") as file:
        json.dump(produk, file, indent=4)

def ambil_dari_json():
    """
    Mengambil data produk dari file JSON.
    Jika file tidak ada atau rusak, kembalikan dictionary kosong.
    """
    try:
        with open("produk.json", "r") as file:
            produk = json.load(file)
            produk = {int(k): v for k, v in produk.items()}
            return produk
    except (FileNotFoundError, json.JSONDecodeError):
        print("File produk.json tidak ditemukan atau rusak. Membuat file baru...")
        simpan_ke_json({})
        return {}

def tambah_produk():
    """
    Menambahkan produk baru ke vending machine.
    """
    produk = ambil_dari_json()
    print("Input produk ke vending machine. Ketik '0' untuk selesai.")
    while True:
        nama = input('Masukkan nama produk: ').strip()
        if nama == '0':
            break
        try:
            harga = int(input(f'Masukkan harga dari {nama}: Rp '))
            stok = int(input(f"Masukkan banyak barang dari {nama}: "))
            kode = len(produk) + 1
            produk[kode] = {"nama": nama, "harga": harga, "stok": stok}
            print(f"Produk {nama} dengan harga Rp {harga} dan stok {stok} berhasil ditambahkan")
        except ValueError:
            print('Error. Harga dan stok harus berupa angka.')
    simpan_ke_json(produk)
    return produk

def tampilan_produk(produk):
    """
    Menampilkan daftar produk.
    """
    print("\nDaftar Produk:")
    for kode, item in produk.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']} (Stok: {item['stok']})")

def generate_qr_code_terminal(content):
    """
    Membuat QR Code untuk konten tertentu dan menampilkannya di terminal.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=2,  # Ukuran border QR Code
    )
    qr.add_data(content)
    qr.make(fit=True)

    # Menampilkan QR Code di terminal
    print("\nQR Code untuk pembayaran:")
    qr.print_ascii(invert=True)

def vending_machine(produk):
    """
    Fungsi vending machine untuk pembeli.
    """
    if not produk:
        print("Vending Machine kosong, silahkan hubungi Admin.")
        return
    while True:
        tampilan_produk(produk)
        try:
            pilih = int(input("\nMasukkan kode produk yang ingin dibeli (0 untuk keluar): "))
            if pilih == 0:
                print("Terima Kasih telah menggunakan Vending Machine.")
                break
            if pilih not in produk:
                print("Produk tidak ditemukan. Silakan coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Silakan input kode yang benar.")
            continue

        produk_pilihan = produk[pilih]
        if produk_pilihan["stok"] <= 0:
            print(f"Maaf, stok {produk_pilihan['nama']} habis.")
            continue

        print(f"Anda memilih {produk_pilihan['nama']} dengan harga Rp{produk_pilihan['harga']}")

        # Generate QR Code untuk transaksi
        qr_content = f"Produk: {produk_pilihan['nama']}\nHarga: Rp{produk_pilihan['harga']}"
        generate_qr_code_terminal(qr_content)

        # Update stok setelah transaksi selesai
        produk_pilihan["stok"] -= 1
        simpan_ke_json(produk)
        print("Silakan gunakan QR Code di atas untuk membayar.")

if __name__ == "__main__":
    akun()
