"""
build.py  —  membuat index.html dari template.html + data.py

Cara pakai (di terminal VS Code):
    python build.py

Lalu buka index.html di browser. Tidak butuh install library apa pun.
"""
from html import escape
from pathlib import Path

import data

FOLDER = Path(__file__).parent
IKON = {"Wisata": "🏞️", "Budaya": "🏛️", "Kuliner": "🍜"}


def link_maps(m: str) -> str:
    """Kalau sudah link lengkap dipakai langsung, kalau kode /g/... jadi link Google."""
    if m.startswith("http"):
        return m
    return "https://www.google.com/search?kgmid=" + m


def buat_kartu(t: dict) -> str:
    label_harga = "Kisaran harga" if t["kat"] == "Kuliner" else "Tiket (HTM)"
    kata_cari = f'{t["nama"]} {t["desc"]} {t["lokasi"]}'.lower()
    return f"""
    <article class="kartu {t['kat'].lower()}" data-kat="{t['kat']}" data-cari="{escape(kata_cari, quote=True)}">
      <div class="kepala"><span>{IKON[t['kat']]}</span><small>{t['kat']}</small></div>
      <div class="isi">
        <h3>{escape(t['nama'])}</h3>
        <p>{escape(t['desc'])}</p>
        <ul>
          <li><b>Lokasi:</b> {escape(t['lokasi'] or 'Lihat di Google Maps')}</li>
          <li><b>{label_harga}:</b> {escape(t['htm'] or 'Cek di lokasi')}</li>
          <li><b>Jam buka:</b> {escape(t['jam'] or 'Cek di lokasi')}</li>
        </ul>
        <a class="peta" href="{escape(link_maps(t['maps']), quote=True)}" target="_blank" rel="noopener">Lihat di Google Maps</a>
      </div>
    </article>"""


def hitung(kategori: str) -> int:
    return sum(1 for t in data.SEMUA if t["kat"] == kategori)


def main() -> None:
    template = (FOLDER / "template.html").read_text(encoding="utf-8")

    stat = "".join(f"<div><b>{hitung(k)}</b>{k}</div>" for k in data.KATEGORI)

    tombol = [f'<button class="aktif" data-filter="Semua">Semua ({len(data.SEMUA)})</button>']
    tombol += [f'<button data-filter="{k}">{k} ({hitung(k)})</button>' for k in data.KATEGORI]

    kartu = "".join(buat_kartu(t) for t in data.SEMUA)

    hasil = (template
             .replace("{{STAT}}", stat)
             .replace("{{FILTER}}", "".join(tombol))
             .replace("{{KARTU}}", kartu))

    (FOLDER / "index.html").write_text(hasil, encoding="utf-8")
    print(f"Selesai! index.html dibuat dengan {len(data.SEMUA)} tempat.")


if __name__ == "__main__":
    main()
