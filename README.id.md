<div align="center">

# 🛡️ Agent-Checkpoint

**Pencadangan file pra-edit tanpa kehilangan data, klasifikasi SemVer, dan buku catatan audit ganda untuk AI coding & riset otonom.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)]()
[![Cross Agent](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Windsurf%20%7C%20Copilot-orange.svg)]()
[![SemVer](https://img.shields.io/badge/Versioning-SemVer%202.0-blueviolet.svg)]()

---

**Pilihan Bahasa:**  
[🇬🇧 English](./README.md) • [🇮🇩 Bahasa Indonesia (Aktif)](./README.id.md)

---

</div>

## ⚡ Masalah: AI Menimpa File Secara Destruktif

AI coding agent otonom (Cursor, Claude Code, Google Antigravity, Windsurf, GitHub Copilot, Aider) semakin mempercepat pengembangan software dan riset ilmiah. Namun, hampir semua AI memiliki perilaku bawaan yang berbahaya: **mereka menimpa file secara langsung tanpa menyimpan riwayat sebelumnya**.

* ❌ **Regresi Diam-diam:** AI merefaktor kode dan secara tidak sengaja menghilangkan penanganan kasus kritis (*edge cases*) atau formula penting.
* ❌ **Nol Jejak Audit:** Anda kembali ke proyek tanpa mengetahui *mengapa* perubahan logika atau parameter tertentu dilakukan oleh AI.
* ❌ **Halusinasi Permanen:** Kesalahan interpretasi perintah membuat AI menghapus draf naskah atau kode kerja berjam-jam.
* ❌ **Riwayat Git Kotor:** Developer terpaksa membuat puluhan *micro-commit* Git hanya agar punya jaring pengaman untuk *undo*.

---

## 💡 Solusi: Protokol Agent-Checkpoint

**Agent-Checkpoint** adalah protokol ultra-ringan tanpa dependensi (*zero-dependency*) yang dipasang dalam hitungan detik. Protokol ini memberlakukan aturan mutlak pada AI: **dilarang menyentuh file yang ada tanpa menyalin versi lamanya terlebih dahulu**, sekaligus mencatat jurnal audit yang menjelaskan *alasan* perubahan tersebut.

---

## 🌟 Keuntungan Utama

### 1. 🛡️ Keamanan Mutlak (Nol Data Hilang)
Sebelum mengedit file, AI secara otomatis menyalin versi utuh sebelumnya ke folder tersembunyi `.snapshots/`. Kode dan dokumen Anda tidak akan pernah tertimpa tanpa jejak.

### 2. 📝 Jurnal Audit Otomatis (Audit Trail)
AI secara otomatis memperbarui file `REVISION_LOG.md` yang mencatat **alasan teknis dan arsitektural** di balik setiap perubahan. Sangat berguna untuk:
* Ringkasan *code review* dan evaluasi tim.
* Menelusuri kembali apa yang diubah AI semalam tanpa harus menebak-nebak.
* Rekam jejak kepatuhan (*compliance*) dan transparansi proyek ilmiah.

### 3. 🎯 Tanpa Dependensi & 100% Privat
* **Tanpa instalasi:** Tidak butuh `npm`, `pip`, Docker, atau server latar belakang.
* **100% Lokal & Offline:** Semua snapshot dan log tersimpan di harddisk lokal Anda sendiri. Nol data dikirim ke luar.

### 4. 🔀 Pelacakan Mundur & Rollback Cepat
Anda dapat meminta AI kapan saja: *"Bandingkan `auth_service.py` dengan versi sebelum direfaktor"* atau *"Kembalikan `auth_service.py` ke versi `v1.0.0`"*. AI akan memuat snapshot lama dan menyajikan perbandingan atau pemulihan seketika.

---

## 🏗️ Arsitektur: Sistem Buku Besar Ganda (Dual-Ledger)

```mermaid
flowchart TD
    subgraph Trigger ["1. Pemicu Perubahan File"]
        A["User Meminta Edit / Refactor"] --> B{"File Sudah Ada?"}
        B -->|"Belum (File Baru)"| C["Registrasi sebagai v1.0.0 (Initial)"]
        B -->|"Sudah Ada"| D["Klasifikasi Dampak SemVer\n(MAJOR / MINOR / PATCH)"]
    end

    subgraph CoreEngine ["2. Eksekusi Snapshot & Edit"]
        D --> E["Salin File Aktif ke:\n.snapshots/<nama>_v<OLD_VERSION>.<ext>"]
        E --> F["Terapkan Perubahan ke File Utama"]
    end

    subgraph DualLedger ["3. Sinkronisasi Buku Besar Ganda"]
        F --> G[".snapshots/manifest.json\n(Indeks Mesin Cepat untuk AI: < 5ms)"]
        F --> H["REVISION_LOG.md\n(Buku Catatan Audit untuk Manusia)"]
    end

    subgraph Retrieval ["4. Trackback & Rollback"]
        I["User: 'Bandingkan dengan versi lama'"] --> G
        G --> J["Muat Snapshot Lama vs File Aktif"]
        J --> K["Sajikan Tabel Perbandingan / Analisis"]
    end

    style G fill:#1b4332,color:#fff,stroke:#fff
    style H fill:#2d6a4f,color:#fff,stroke:#fff
```

---

## 🔰 Panduan Pemula (Pemasangan 30 Detik)

Pemasangan tidak memerlukan konfigurasi rumit maupun perintah terminal. Cukup gunakan metode *drop-in file*.

### Cara 1: Menggunakan File Explorer (Paling Mudah)
1. Buka folder [`adapters/`](./adapters) di repositori ini.
2. Pilih 1 file yang sesuai dengan aplikasi AI Anda:
   * **Cursor IDE:** Salin file [`.cursorrules`](./adapters/.cursorrules)
   * **Claude Code:** Salin file [`CLAUDE.md`](./adapters/CLAUDE.md)
   * **Google Antigravity / Gemini CLI:** Salin aturan dari [`AGENTS.md`](./adapters/AGENTS.md)
   * **Windsurf (Cascade):** Salin file [`.windsurfrules`](./adapters/.windsurfrules)
   * **GitHub Copilot:** Salin file [`copilot-instructions.md`](./adapters/copilot-instructions.md) ke folder `.github/`
3. Tempel (*paste*) file tersebut ke folder root proyek Anda.
4. **Selesai!** AI di aplikasi Anda sudah otomatis terlindungi.

---

### Cara 2: Menggunakan Terminal (Perintah 1-Baris)
Jalankan perintah ini di dalam root proyek Anda:

* **Cursor IDE:**
  ```bash
  curl -o .cursorrules https://raw.githubusercontent.com/username/agent-checkpoint/main/adapters/.cursorrules
  ```
* **Claude Code:**
  ```bash
  curl -o CLAUDE.md https://raw.githubusercontent.com/username/agent-checkpoint/main/adapters/CLAUDE.md
  ```
* **Windsurf:**
  ```bash
  curl -o .windsurfrules https://raw.githubusercontent.com/username/agent-checkpoint/main/adapters/.windsurfrules
  ```

---

## 🎮 Penggunaan Sehari-hari (Zero Learning Curve)

Setelah adapter terpasang, **Anda tidak perlu menghafal perintah baru**. Berinteraksilah dengan AI seperti biasa:

### 1. Meminta AI Mengedit Kode
Beri prompt seperti biasa:
> *"Tolong refactor fungsi autentikasi login di auth_service.py agar mendukung JWT token refresh dan rate limiting."*

**Secara otomatis di balik layar, AI akan:**
1. Mencadangkan file lama Anda ke `.snapshots/auth_service_v1.0.0.py`.
2. Menerapkan perubahan pada `auth_service.py` (naik versi menjadi `v1.1.0`).
3. Mencatat alasan teknis ke `REVISION_LOG.md` dan `.snapshots/manifest.json`.

---

### 2. Memeriksa Perubahan (*Trackback*)
Lihat perbedaan tanpa perlu membuka git diff secara manual:
> *"Bandingkan auth_service.py dengan versi sebelum direvisi. Apa saja logic keamanan dan error handling yang berubah?"*

AI akan langsung membaca snapshot lama dan menyajikan perbandingan *Before vs After*.

---

### 3. Membatalkan Perubahan (*Rollback*)
Jika hasil kodingan AI tidak sesuai harapan:
> *"Batalkan perubahan pada auth_service.py dan kembalikan ke versi v1.0.0."*

AI akan mengembalikan file dari `.snapshots/` dengan aman.

---

## 📂 Struktur Folder Proyek

Setelah aktif, proyek Anda akan memiliki struktur rapi berikut:

```text
my-project/
├── .snapshots/                          # Folder snapshot riwayat (dikelola otomatis)
│   ├── manifest.json                    # Indeks cepat untuk AI (< 5ms)
│   ├── auth_service_v1.0.0.py           # Snapshot cadangan sebelum diedit
│   └── api_routes_v1.0.0.ts
├── REVISION_LOG.md                      # Log riwayat lengkap untuk dibaca manusia/tim
├── auth_service.py                      # File aktif versi terbaru (v1.1.0)
└── api_routes.ts                        # File aktif versi terbaru
```

---

## ⚠️ Batasan yang Diketahui (Known Limitations)

Demi transparansi rekayasa perangkat lunak, versi `v1.0` memiliki batasan berikut:

| Batasan | Konteks Teknis | Saran Mitigasi |
| :--- | :--- | :--- |
| **1. Kepatuhan Model Kecil** | Protokol berbasis instruksi sistem. Model tier-1 (Claude 3.5/3.7, GPT-4o, Gemini 2.0 Pro) memiliki kepatuhan **~100%**. Model kecil lokal (7B/8B) sesekali bisa lupa membuat snapshot jika sesi chat sangat panjang. | Gunakan model cerdas untuk tugas refactoring utama. |
| **2. Penumpukan Snapshot** | Jika file diedit ratusan kali, folder `.snapshots/` akan terus bertambah. Fitur pembersihan otomatis (*auto-pruning*) belum disertakan di v1.0. | File teks memakan storage sangat sedikit (~10 MB/bln), tetapi disarankan menghapus versi patch lama secara berkala. |
| **3. Operasi Delete / Rename** | Versi 1.0 berfokus pada edit isi (*modify*). Menghapus file lewat terminal (`rm`) belum dicegat secara otomatis. | Lakukan konfirmasi manual sebelum menyuruh AI menghapus file secara permanen. |
| **4. Refactoring Multi-File Sekaligus** | Mengubah 10 file dalam 1 prompt akan menghasilkan 10 entri log terpisah daripada 1 entri grup (*changeset*). | Lakukan refactor bertahap per modul. |

---

## 🌐 Dukungan File Universal & Batasan Penyimpanan Cerdas

Agent-Checkpoint **mendukung semua bahasa pemrograman dan jenis file teks (*universal & agnostic*)**. Aturan dasarnya sangat sederhana:  
> **"Jika suatu file dapat dibuka dan diedit di editor teks atau editor kode, Agent-Checkpoint melindunginya."**

### ✅ File Apa Saja yang Otomatis Di-snapshot? (Mendukung 100+ Format)

* **Bahasa Pemrograman & Sistem:** Python (`.py`), TypeScript (`.ts`, `.tsx`), JavaScript (`.js`, `.jsx`), Go (`.go`), Rust (`.rs`), C/C++ (`.c`, `.cpp`, `.h`, `.hpp`), C# (`.cs`), Java (`.java`), PHP (`.php`), Ruby (`.rb`), Swift (`.swift`), Kotlin (`.kt`), Dart (`.dart`), Scala (`.scala`), Shell (`.sh`, `.bash`, `.zsh`), PowerShell (`.ps1`, `.bat`), Lua (`.lua`), R (`.r`), Julia (`.jl`).
* **Web & Antarmuka Frontend:** HTML (`.html`), CSS (`.css`), SCSS/SASS (`.scss`), Vue (`.vue`), Svelte (`.svelte`), XML (`.xml`), SVG (`.svg`).
* **Data Science & Riset Modern:** Jupyter Notebooks (`.ipynb`), Typst (`.typ`), LaTeX (`.tex`, `.bib`, `.sty`), Markdown (`.md`, `.mdx`), RestructuredText (`.rst`), AsciiDoc (`.adoc`), Plain text (`.txt`).
* **Diagrams & Visual Berbasis Kode:** Mermaid (`.mmd`, `.mermaid`), PlantUML (`.puml`), Graphviz (`.dot`), Draw.io XML (`.drawio`), Excalidraw JSON (`.excalidraw`).
* **Skema API, Kontrak & Protokol:** Protobuf (`.proto`), GraphQL (`.graphql`, `.gql`), Prisma (`.prisma`), OpenAPI / Swagger (`.yaml`, `.json`), Apache Thrift (`.thrift`), FlatBuffers (`.fbs`).
* **Game Development & Shaders:** GLSL (`.glsl`, `.frag`, `.vert`), HLSL (`.hlsl`), WGSL (`.wgsl`), Godot GDScript (`.gd`, `.tscn`), Unreal Engine text configs (`.ini`).
* **Hardware & Sistem Tertanam (Embedded):** Verilog (`.v`, `.vh`), SystemVerilog (`.sv`), VHDL (`.vhd`), Assembly (`.asm`, `.s`), Arduino (`.ino`), CMake (`CMakeLists.txt`, `.cmake`).
* **DevOps, IaC & Kebijakan Keamanan:** Open Policy Agent Rego (`.rego`), CUE (`.cue`), Terraform (`.tf`), Kubernetes manifests, Dockerfile, Makefile, JSON, YAML, TOML, SQL (`.sql`).

---

### 🛡️ Batasan Penyimpanan Cerdas (Garansi Nol Beban Disk)

Untuk memperluas dukungan format tanpa membuat harddisk Anda sesak, protokol menerapkan **Aturan Bertingkat (*Tiered Ingestion Rules*)**:

#### 1. 📏 Ambang Batas 1 MB untuk Data Tabular (*Smart 1 MB Cap*)
* File data kecil, mock data uji, dan data seed (`.csv`, `.tsv`, `.jsonl`, `.ndjson`) **hanya di-snapshot jika ukurannya $\le 1\text{ MB}$**.
* Jika ukuran file melebihi $1\text{ MB}$ (contoh: dataset training 100 MB), AI **secara otomatis tidak menduplikasi filenya**, melainkan hanya mencatat metadata-nya (nama file dan waktu perubahan) di `REVISION_LOG.md` tanpa memakan ruang harddisk.

#### 2. 🚫 Pengecualian Ketat File Biner
Protokol secara ketat menolak pencadangan file biner berat dan direktori dependensi:

| Kategori Berkas | Kebijakan Snapshot | Contoh Berkas (Tidak Pernah Diarsip) |
| :--- | :--- | :--- |
| **Model AI & Machine Learning** | 🚫 **Dikecualikan** | Bobot model & checkpoint (`.pt`, `.pth`, `.onnx`, `.safetensors`, `.bin`, `.ckpt`) |
| **Dataset Berukuran Besar** | 🚫 **Dikecualikan** | Data tabular berat ($> 1\text{ MB}$, `.parquet`, `.h5`, `.arrow`, `.feather`, `.csv` raksasa) |
| **Biner Terkompilasi & Media** | 🚫 **Dikecualikan** | File biner (`.exe`, `.dll`, `.so`), arsip (`.zip`, `.tar.gz`), video/audio |
| **Folder Cache & Dependensi** | 🚫 **Dikecualikan** | `node_modules/`, `venv/`, `.venv/`, `__pycache__/`, `target/`, `dist/`, `build/`, `.git/` |

**Estimasi Ruang Penyimpanan:**  
Karena berkas kode sumber teks berukuran sangat kecil (rata-rata 5 KB s.d. 50 KB), bahkan **500 kali modifikasi berkas dalam sebulan** hanya memakan sekitar **~7.5 MB hingga 15 MB** ruang harddisk. Praktis tidak membebani disk modern sama sekali.

---

## 📄 Lisensi & Komunitas

Didistribusikan di bawah [Lisensi MIT](./LICENSE) — bebas digunakan untuk proyek pribadi, riset akademik, maupun komersial.

Kontribusi, *pull request*, dan saran fitur baru sangat kami sambut! ⭐ Silakan beri *Star* jika repositori ini membantu melindungi pekerjaan Anda.
