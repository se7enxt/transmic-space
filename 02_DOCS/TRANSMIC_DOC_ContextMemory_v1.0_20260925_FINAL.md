# Transmic Space: Living Context Memory & Orchestrator Charter
**Autonomous Context Tracking, Evolution Ledger & Production Management Protocol**  
**Document Code:** `TRANSMIC_DOC_ContextMemory_v1.0_20260925_FINAL.md`  
**Status:** `FINAL` | **Date:** 2026-09-25  
**Author:** Transmic Space Orchestrator Manager  

---

## 1. Executive Charter & Purpose

This charter formally establishes the **Transmic Space Orchestrator Manager** — an autonomous context-preservation and operational management engine dedicated exclusively to **Transmic Space**.

### Core Mandate
1. **Persistent Context Continuity:** Maintain an unbroken mental model, historical context, and architectural awareness of all Transmic Space projects, musical releases, film productions, assets, and strategic decisions across sessions.
2. **Evolutionary State Tracking:** Systematically record all updates, milestones, draft iterations, and directional shifts into an active, machine-readable `context_state.json` and version-controlled documentation.
3. **Multi-Channel Communication Readiness:** Provide immediate local staging for asynchronous communication via WhatsApp (`DAEMON-WA`), ensuring decisions made on mobile or desktop are synchronized in real-time.
4. **Rigorous Catalog & Compliance Governance:** Safeguard statutory rights (IPRS IPI `01350235979`, 50% publishing share), adhere to workspace naming conventions, and protect canonical historical release dates.

---

## 2. Entity Identity & Brand Foundations

| Attribute | Authoritative Value |
| :--- | :--- |
| **Entity Name** | **Transmic Space** |
| **Brand Tagline** | *A Lab for Magic* |
| **Primary Disciplines** | Folk Fusion • Contemporary Bengali Songwriting • Independent Cinema • Urban-Folk Synthesis • Performance Events |
| **CISAC / IPI Entity Number** | `01350235979` |
| **Statutory Role** | Original Publisher & Production Banner |
| **Statutory Publishing Share** | **50.00% Mechanical & Performance Royalties** |
| **Official YouTube Channel** | [`@TransmicSpace`](https://www.youtube.com/@TransmicSpace) |
| **Founding Creative Partner** | Abhik Chatterjee (`#ABHIKISM`, IPI `01350235881`, IPRS `9856510`) |
| **Primary Collaborative Vocalist** | Sreemoyee Bhattacharya |

---

## 3. Catalog & Production Benchmarks

### 3.1 Flagship Masterpiece: Taar Kata Ektara (তার কাটা একতারা)
- **Artists:** Sreemoyee Bhattacharya & #abhikism (Abhik Chatterjee)
- **Canonical Release Genesis:** `2019-08-16` (Soundrop ID `569815`)
- **YouTube Video Premiere:** `2019-10-01` ([Watch on YouTube](https://www.youtube.com/watch?v=_PXjXY4ZAB8))
- **ISRC:** `QZGWW1944761` | **Soundrop UPC:** `1941520272340`
- **IPRS Work Identifier:** `WKS-007` | **Work Registration No:** `35410376`
- **Royalties Split:** 50.00% Abhik Chatterjee (Composer/Author) / 50.00% Transmic Space (Original Publisher)

### 3.2 Master Audiovisual Repertoire (16 YouTube Productions)
1. **Pagol Hawa ~ Naa Jaane Kyun** (`tOJcUVOKzfE` | 2026-06-22) — Music Video ft. Riya & Sreemoyee
2. **Boho Folk Tales ~ Episodes 1–5** (`nZL5KIlc7rM`, `EQhgSkWmum4`, `FWwL16Os61Q`, `6uM-ZUzf_54`, `K3VUQdUo6DE` | 2022-10-29–30) — 5-Episode Web Series ft. Titash Bhramar Sen, Tanika Basu, Srabasti Ghosh, Ranieeta Dash, Satakshi Nandy, Ankita Chakraborty, Prantik Banerjee
3. **Jaao Aaro Jaao (যাও আরো যাও)** (`ySilXtOY1lM` | 2021-10-12) — Lyric Video
4. **Hey Bhoboghurey (হে ভবঘুরে)** (`5Wjfk2G5iXc` | 2020-04-14) — Lyric Video
5. **Kichhhudin Mone Mone (কিছুদিন মনে মনে)** (`vteykfpmaMc` | 2020-04-04) — Folk Music Video
6. **Taar Kata Ektara (তার কাটা একতারা)** (`_PXjXY4ZAB8` | 2019-10-01) — Flagship Music Video
7. **All Characters Are Fictitious** (`aT7Z1MqGE6Y` | 2018-04-17) & Trailer 2 (`IslsgtzJmnw` | 2017-09-26) — Feature Film ft. Rii Sen, Saayoni Ghosh, Indrasish Roy
8. **SpaceB (Full Documentary)** (`mW3CnlK_Mx4` | 2017-06-15) — Documentary on Baul Masters & Folk Fusion
9. **#NoWomensDay \| Jodi Akaasher Gaaye** (`ctac2ejFfI4` | 2017-03-08) — Tribute Music Video
10. **#TrashDoveTransmic** (`GNOr4k69TBw` | 2017-02-22) — Creative Short
11. **Dil Ka DP (दिल का DP)** (`VlxeUZIkMU8` | 2017-02-14) — Music Video ft. Bhumika Dubey, Muktak Kanjilal, #abhikism

### 3.3 Publishing Catalog (41 IPRS Registered Works)
A registered repertoire of 41 musical works including *Taar Kata Ektara*, *Boho Folk Tales* thematic compositions, and contemporary fusion songs registered with the Indian Performing Right Society.

---

## 4. Context Persistence & Evolution Engine Architecture

```text
PROJECTS/TRANSMIC_SPACE/
├── 00_CONTEXT/
│   └── context_state.json                # Master living state machine & evolution ledger
├── 01_DATABASE/
│   ├── transmic_space_catalog.json       # Master catalog database (16 videos, 41 works)
│   ├── transmic_youtube_releases.csv     # Official YouTube releases ledger
│   └── transmic_repertoire_works.csv     # IPRS publishing repertoire
├── 02_DOCS/
│   ├── TRANSMIC_DOC_ContextMemory_v1.0_20260925_FINAL.md     # This Charter & Context Doc
│   ├── TRANSMIC_DOC_MasterCatalogDossier_v1.1_20260924_FINAL.md
│   ├── TRANSMIC_DOC_TaarKataEktaraRelease_v1.0_20260924_FINAL.md
│   └── TRANSMIC_DOC_RepertoireCatalog_v1.0_20260924_FINAL.md
├── 03_ASSETS/                            # Branding, posters, typography, thumbnails
├── 04_SCRIPTS/
│   └── transmic_orchestrator.py         # Context CLI: status, sync, log-event, audit
├── 05_COMMUNICATIONS/
│   └── wa_staging.json                   # WhatsApp staging queue (DAEMON-WA bridge)
├── 04_LINKTREE/                          # Mirror of Linktree web application
├── index.html                            # Master responsive catalog hub (GitHub Pages)
├── style.css                             # Glassmorphism cyber-indie design system
├── app.js                                # Dynamic catalog & media modal logic
└── catalog_data.js                       # Inlined catalog data
```

### 4.1 CLI Orchestrator Operations
The orchestrator CLI is located at `04_SCRIPTS/transmic_orchestrator.py` and provides four primary operations:
- `python3 04_SCRIPTS/transmic_orchestrator.py status`: Renders an executive terminal brief with current phase, catalog stats, WhatsApp status, and the 5 most recent evolution milestones.
- `python3 04_SCRIPTS/transmic_orchestrator.py sync`: Auto-scans all folders, counts files, verifies database records, and updates `last_updated` in `context_state.json`.
- `python3 04_SCRIPTS/transmic_orchestrator.py log-event --category <CAT> --summary "<SUMMARY>"`: Appends an event to the evolution ledger.
- `python3 04_SCRIPTS/transmic_orchestrator.py audit`: Runs compliance audits on Transmic files.

---

## 5. WhatsApp Communication Channel Readiness

The orchestrator manager is architected to immediately connect with `DAEMON-WA` (`whatsapp-orchestrator`) targeting the **`Notes`** chat in Chrome Tab 8:
- **Status:** `STANDBY_PENDING_ACTIVATION`
- **Staging Queue:** `05_COMMUNICATIONS/wa_staging.json`
- **Protocol Conformity:**
  - `QA-093` / `QA-122`: Strict exclusivity to the dedicated `Notes` chat; zero external leak.
  - `QA-106`: Structured Directorial Consultation Rubric for quick single-digit replies (`1`, `2`, `3`).
  - `QA-124`: Support for document-modal and high-resolution asset dispatch.

---

## 6. Immutable Operational Invariants

1. **Zero Root Dumping Rule:** No loose files, assets, or scripts in the root or Downloads. Every asset belongs to a numbered subfolder.
2. **Semantic Versioning & Audit Compliance:** Standard format `{PROJECT}_{DOCTYPE}_{Descriptor}_v{Major}.{Minor}_{YYYYMMDD}_{STATUS}.{ext}`. Every document is registered in `_SYSTEM/version_log.csv` and `_SYSTEM/CHANGELOG.md`.
3. **Master Artwork Invariant:** Original master artwork files (`master_artwork.jpg`) remain permanently anchored within the central `#ABHIKISM` archive. Transmic Space hosts derivative posters, thumbnails, and web graphics in `03_ASSETS`.
4. **Canonical Genesis Release Date Rule:** Genesis release dates (e.g., `2019-08-16` for *Taar Kata Ektara*) must never be overwritten by reissue, remaster, or compilation dates.
5. **QuickTime Native Playback Standard:** All video deliverables must use H.264 video (`yuv420p`), AAC stereo audio (`48kHz`), and `-movflags +faststart`.
