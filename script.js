// script.js — interaksi kecil di browser: filter, cari, efek muncul, tombol ke atas.
// (Browser tidak bisa menjalankan Python, jadi bagian interaktif memakai JavaScript.)

const kartu = document.querySelectorAll('.kartu');
const tombol = document.querySelectorAll('#filter button');
const cari = document.getElementById('cari');
const kosong = document.getElementById('kosong');
const atas = document.getElementById('atas');
let aktif = 'Semua';

// Efek kartu muncul pelan-pelan saat di-scroll
const pengamat = new IntersectionObserver(daftar => {
  daftar.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('tampil');
      pengamat.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
kartu.forEach(k => pengamat.observe(k));

// Tampilkan kartu sesuai kategori dan kata kunci
function saring() {
  const q = cari.value.trim().toLowerCase();
  let jumlah = 0;
  kartu.forEach(k => {
    const cocok = (aktif === 'Semua' || k.dataset.kat === aktif) && k.dataset.cari.includes(q);
    k.hidden = !cocok;
    if (cocok) jumlah++;
  });
  kosong.hidden = jumlah > 0;
}

function pilih(kategori) {
  aktif = kategori;
  tombol.forEach(b => b.classList.toggle('aktif', b.dataset.filter === kategori));
  saring();
}

tombol.forEach(b => b.addEventListener('click', () => pilih(b.dataset.filter)));
cari.addEventListener('input', saring);

// Menu atas (Wisata / Budaya / Kuliner) langsung memilih kategori
document.querySelectorAll('[data-pilih]').forEach(a =>
  a.addEventListener('click', () => pilih(a.dataset.pilih)));

// Tombol kembali ke atas
addEventListener('scroll', () => atas.classList.toggle('muncul', scrollY > 600));
atas.addEventListener('click', () => scrollTo({ top: 0 }));
