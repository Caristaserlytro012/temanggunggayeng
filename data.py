"""
data.py  —  SEMUA ISI WEB ADA DI SINI (edit file ini saja).

Setelah mengedit, jalankan:  python build.py
Hasilnya file index.html yang siap dibuka / di-deploy ke Vercel.

Kolom "maps":
  - kalau diawali "http"  -> dipakai langsung sebagai link
  - kalau diawali "/g/"   -> otomatis jadi link Google
Kolom yang dikosongkan ("") akan tampil "Cek di lokasi".
"""

# ---------------------------------------------------------------
# WISATA — 27 link dari Carista (urutan sama dengan daftar di tugas)
# ---------------------------------------------------------------
WISATA_LINK = [
    "https://share.google/U8sgXWANsIm5E81ho", "https://share.google/adZtv97qYOl9XU17x",
    "https://share.google/fQHSlZYXMdv8H4m3K", "https://share.google/ofnZQWIWFj481gCwh",
    "https://share.google/WAkmFVm4Iezirc8SY", "https://share.google/ljPQaD1vsduiAAXYn",
    "https://share.google/2zNVUSzws5naRPdCG", "https://share.google/DfWOpeP3rkMorOc5R",
    "https://share.google/ANeqt13Xj4Sok5WuR", "https://share.google/o2On4ZFgU5qDAFCSi",
    "https://share.google/pwBZgyDUO7uHoOkaM", "https://share.google/UGLjuKk6DvooqXTXj",
    "https://share.google/G6xlLlD8bUeusVwT8", "https://share.google/QWLZc2sVFBk0vrn4x",
    "https://share.google/cW2Z8gqLbxFvxDRwh", "https://share.google/ALJ3l0Wg621Gzl9XC",
    "https://share.google/z9L5Y6KUCNt4xzdsb", "https://share.google/GR7TpnSppT1I9fkxu",
    "https://share.google/RW6rdkTpfOrTsAo4T", "https://share.google/hrdT2LG0oKhbMYGBP",
    "https://share.google/j2R7WO0QBDUL0ggIE", "https://share.google/tFeagjczmcKimjGOA",
    "https://share.google/AV4vRTJk6LQ37qfGl", "https://share.google/PzqThDGgNu2KNyFTC",
    "https://share.google/KLTUZ0WMCZge8RY61", "https://share.google/TKZE9iasfKoCfwepW",
    "https://share.google/DI7T9rnNeBXoYuFvQ",
]

# ISI INFO WISATA DI SINI. Format per nomor link (mulai dari 1):
#   nomor: ("Nama", "Lokasi", "Deskripsi", "HTM", "Jam buka"),
# Contoh:
#   1: ("Nama Wisata", "Kecamatan ...", "Tempat wisata alam yang ...", "Rp10.000", "08.00 - 17.00"),
WISATA_INFO = {
    1: ("Wisata Alam Posong", "", "", "", ""),
    2: ("Embung Kledung", "", "", "", ""),
    3: ("Umbul Jumprit", "", "", "", ""),
    4: ("Pikatan Water Park", "", "", "", ""),
    5: ("Pasar Papringan Ngadiprono", "", "", "", ""),
    6: ("Situs Liyangan", "", "", "", ""),
    7: ("Kledung Park", "", "", "", ""),
    8: ("Wana Wisata Walitis", "", "", "", ""),
    9: ("Alam Sewu", "", "", "", ""),
    10: ("Candi Pringapus", "", "", "", ""),
    11: ("Curug Surodipo", "", "", "", ""),
    12: ("Air Terjun Curug Lawe Benowo Kalisidi", "", "", "", ""),
    13: ("Kledung Pass", "", "", "", ""),
    14: ("Sunrise Camp Gunung Prau", "", "", "", ""),
    15: ("Alun-Alun Kota Temanggung", "", "", "", ""),
    16: ("Jembatan Sigandul Temanggung", "", "", "", ""),
    17: ("Curug Onje", "", "", "", ""),
    18: ("Wisata Alam Sigrowong", "", "", "", ""),
    19: ("Monumen Meteorit Wonotirto", "", "", "", ""),
    20: ("Curug Lawe", "", "", "", ""),
    21: ("Wahana Wisata Alam Jumprit Temanggung (WAPITT)", "", "", "", ""),
    22: ("Puncak Botorono", "", "", "", ""),
    23: ("Sigandul View", "", "", "", ""),
    24: ("Embung Bansari", "", "", "", ""),
    25: ("Curug Titang", "", "", "", ""),
    26: ("Taman Kali Progo", "", "", "", ""),
    27: ("Taman Kartini Temanggung", "", "", "", ""),
}

DESKRIPSI_DEFAULT = ("Tempat wisata di Temanggung. Buka Google Maps untuk melihat "
                     "foto, ulasan, dan lokasinya.")

WISATA = []
for i, link in enumerate(WISATA_LINK, start=1):
    d = list(WISATA_INFO.get(i, ())) + [""] * 5
    WISATA.append({
        "kat": "Wisata",
        "nama": d[0] or f"Wisata {i}",
        "lokasi": d[1],
        "desc": d[2] or DESKRIPSI_DEFAULT,
        "htm": d[3],
        "jam": d[4],
        "maps": link,
    })

# ---------------------------------------------------------------
# BUDAYA
# ---------------------------------------------------------------
BUDAYA = [
    {"nama": "Situs Liyangan", "lokasi": "Dusun Liyangan, Purbosari, Ngadirejo",
     "maps": "/g/187cd6zh", "htm": "Rp5.000", "jam": "",
     "desc": "Kompleks peradaban kuno masa Mataram Kuno yang tertimbun abu vulkanik di lereng Gunung Sindoro. Terlihat sisa struktur hunian, jalan, dan candi."},
    {"nama": "Candi Pringapus", "lokasi": "Desa Pringapus, Ngadirejo",
     "maps": "/g/121hftnt", "htm": "Rp5.000", "jam": "08.00 - 15.30 WIB",
     "desc": "Candi Hindu klasik yang dikelilingi keasrian desa, dengan arsitektur dan relief batu yang indah."},
    {"nama": "Umbul Jumprit", "lokasi": "Jl. Kejajar, Jumprit, Ngadirejo",
     "maps": "/g/11c48vxs9l", "htm": "Rp10.000", "jam": "",
     "desc": "Mata air suci di lereng gunung. Airnya rutin dipakai untuk ritual, misalnya perayaan Trisuci Waisak."},
    {"nama": "Tuk Budoyo", "lokasi": "Losari, Tlogomulyo",
     "maps": "/g/11f7nk0w0_", "htm": "", "jam": "",
     "desc": "Mata air keramat di kaki Gunung Sumbing, pusat ritual pencucian atau pengambilan air bagi penari kesenian tradisional. Berstatus cagar budaya."},
    {"nama": "Makam Ki Ageng Makukuhan", "lokasi": "Tawangsari, Kedu",
     "maps": "/g/11ddy0c7zp", "htm": "", "jam": "",
     "desc": "Makam tokoh penyebar agama dan kebudayaan yang dihormati. Sering jadi titik ziarah dan tradisi budaya tahunan."},
    {"nama": "Roemah Lie Tiauw Ing", "lokasi": "Jl. Diponegoro, pusat kota Temanggung",
     "maps": "/g/11h52cjvtm", "htm": "", "jam": "",
     "desc": "Rumah bersejarah bergaya Tionghoa-Jawa klasik yang pernah jadi lokasi syuting film tahun 1980-an."},
    {"nama": "Pasar Papringan Ngadiprono", "lokasi": "Ngadimulyo, Kedu",
     "maps": "/g/11fk4mt05g", "htm": "", "jam": "Hanya Minggu Pon dan Minggu Wage",
     "desc": "Pasar tradisional unik di kebun bambu. Menyajikan kuliner dan kesenian, dan transaksinya memakai kepingan bambu."},
]
for t in BUDAYA:
    t["kat"] = "Budaya"

# ---------------------------------------------------------------
# KULINER
# ---------------------------------------------------------------
KULINER = [
    {"nama": "Warung Makan Jadoel", "lokasi": "Jl. Jenderal Sudirman No.102, Jampirejo",
     "maps": "/g/11c0psyxxs", "htm": "Rp1 - 25.000 per orang", "jam": "Buka 24 jam",
     "desc": "Rating 4,6 (3,2 ribu ulasan). Berdiri sejak abad ke-19, masakan rumahan tanpa MSG yang disajikan para eyang. Andalannya Bantil, Pelas Tongkol, Oseng Lombok Ijo, dan Tempe Bacem raksasa."},
    {"nama": "Bakso Lombok Uleg Pak Di", "lokasi": "Jl. Jampirejo Tengah",
     "maps": "/g/11ckkx2mvf", "htm": "Rp1 - 25.000 per orang", "jam": "11.00 - 21.00 WIB (Jumat mulai 13.00)",
     "desc": "Rating 4,4 (2,2 ribu ulasan). Bakso berkuah bening segar dengan cabai rawit hijau yang diulek langsung di mangkuk, disajikan dengan ketupat dan tahu pong."},
    {"nama": "Rumah Makan Bu Carik (Parakan)", "lokasi": "Jl. Raya Wonosobo No.224, Parakan Kauman",
     "maps": "/g/1pzx7l1b3", "htm": "", "jam": "07.00 - 17.00 WIB",
     "desc": "Rating 4,5 (1,7 ribu ulasan). Terkenal dengan Brongkos Daging Sapi berkuah gurih manis berbumbu kluwek, cocok dengan empal goreng atau iso babat."},
    {"nama": "Kupat Tahu Batoar", "lokasi": "Jl. Gilingsari No.5, Pacarsari, Manding",
     "maps": "/g/11c1nxn3cl", "htm": "Rp1 - 25.000 per orang", "jam": "08.30 - 18.00 WIB",
     "desc": "Rating 4,6 (926 ulasan). Salah satu kedai kupat tahu tertua dan paling autentik, dengan bumbu kacang gurih manis."},
    {"nama": "Pondok Lesehan Kampoeng Sawah", "lokasi": "Jl. Gatot Subroto No.25",
     "maps": "/g/1pzwzqscd", "htm": "", "jam": "",
     "desc": "Rating 4,3 (2,7 ribu ulasan). Makan lesehan di saung tengah sawah dengan menu utama olahan ikan segar. Cocok untuk keluarga."},
    {"nama": "Sigandul View Coffee & Resto", "lokasi": "Jalur Parakan - Wonosobo",
     "maps": "/g/11q9fny24x", "htm": "", "jam": "",
     "desc": "Rating 4,3 (3,5 ribu ulasan). Kafe dengan pemandangan Jembatan Sigandul serta Gunung Sindoro dan Sumbing."},
    {"nama": "Waroeng Iwak Kali", "lokasi": "Kabupaten Temanggung",
     "maps": "/g/11btvgbzzr", "htm": "", "jam": "",
     "desc": "Rating 4,3 (613 ulasan). Terkenal dengan Ikan Uceng goreng, ikan air tawar kecil khas sungai Temanggung yang renyah dan gurih."},
]
for t in KULINER:
    t["kat"] = "Kuliner"

# Gabungan semua tempat, urutan: wisata, budaya, kuliner
SEMUA = WISATA + BUDAYA + KULINER
KATEGORI = ["Wisata", "Budaya", "Kuliner"]
