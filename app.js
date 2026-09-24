/**
 * Transmic Space — Master Application Logic
 * Interactive Catalog, Dynamic Filter Tabs, Search & Video Modals
 */

document.addEventListener('DOMContentLoaded', () => {
  initCatalog();
});

let currentFilter = 'all';
let searchQuery = '';

function getCatalog() {
  return window.TRANSMIC_CATALOG || { video_releases: [], publishing_repertoire: [] };
}

function initCatalog() {
  renderReleases();
}

function setFilter(filter) {
  currentFilter = filter;
  
  // Update UI active tab
  document.querySelectorAll('.filter-tab').forEach(tab => {
    if (tab.getAttribute('data-filter') === filter) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
  });

  renderReleases();
}

function handleSearch() {
  const input = document.getElementById('searchInput');
  searchQuery = input.value.trim().toLowerCase();
  renderReleases();
}

function renderReleases() {
  const container = document.getElementById('releasesGrid');
  const catalog = getCatalog();
  
  if (!container) return;
  container.innerHTML = '';

  // If Repertoire view is selected
  if (currentFilter === 'Publishing Repertoire') {
    renderRepertoireView(container, catalog.publishing_repertoire || []);
    return;
  }

  // Filter video releases
  const videos = catalog.video_releases || [];
  const filtered = videos.filter(v => {
    const matchesFilter = (currentFilter === 'all') || (v.category === currentFilter);
    const matchesSearch = !searchQuery || 
      v.title.toLowerCase().includes(searchQuery) ||
      (v.full_title && v.full_title.toLowerCase().includes(searchQuery)) ||
      (v.featured_artists && v.featured_artists.toLowerCase().includes(searchQuery)) ||
      (v.type && v.type.toLowerCase().includes(searchQuery));
    return matchesFilter && matchesSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem; color: var(--text-dim);">
        <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">No productions found matching "${searchQuery}"</p>
        <button class="btn" style="background: rgba(255,255,255,0.06);" onclick="resetSearch()">Clear Search</button>
      </div>
    `;
    return;
  }

  filtered.forEach(item => {
    const card = document.createElement('article');
    card.className = 'release-card';
    
    // Thumbnail resolution path
    const thumbPath = item.thumbnail_file 
      ? `./03_ASSETS/03_IMAGES/Thumbnails/${item.thumbnail_file}` 
      : `https://img.youtube.com/vi/${item.id}/maxresdefault.jpg`;

    // DSP button html if available
    let dspButtons = '';
    if (item.dsp_links) {
      if (item.dsp_links.spotify) {
        dspButtons += `<a href="${item.dsp_links.spotify}" target="_blank" rel="noopener" class="card-btn" title="Spotify">🎧 Spotify</a>`;
      }
      if (item.dsp_links.apple_music) {
        dspButtons += `<a href="${item.dsp_links.apple_music}" target="_blank" rel="noopener" class="card-btn" title="Apple Music">🍎 Apple</a>`;
      }
    }

    // If Taar Kata Ektara, provide direct link to dedicated page
    let dedicatedBtn = '';
    if (item.id === '_PXjXY4ZAB8') {
      dedicatedBtn = `<a href="./taar-kata-ektara/" class="card-btn" style="border-color: rgba(139,92,246,0.5); color: #c4b5fd;">Page ↗</a>`;
    }

    card.innerHTML = `
      <div class="card-thumb-wrap" onclick="openVideoModal('${item.id}', '${escapeHtml(item.title)}')">
        <img src="${thumbPath}" alt="${escapeHtml(item.title)}" class="card-thumb" loading="lazy" onerror="this.src='https://img.youtube.com/vi/${item.id}/hqdefault.jpg'">
        <div class="play-overlay">
          <div class="play-circle">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
              <path d="M8 5v14l11-7z"/>
            </svg>
          </div>
        </div>
        <span class="card-badge">${item.type}</span>
      </div>
      
      <div class="card-body">
        <span class="card-date">${formatDate(item.release_date)}</span>
        <h3 class="card-title">${item.title}</h3>
        <p class="card-artists">${item.featured_artists ? `Ft. ${item.featured_artists}` : 'Transmic Space'}</p>
        
        <div class="card-actions">
          <button class="card-btn card-btn-primary" onclick="openVideoModal('${item.id}', '${escapeHtml(item.title)}')">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
              <path d="M8 5v14l11-7z"/>
            </svg>
            Watch
          </button>
          <a href="${item.youtube_url}" target="_blank" rel="noopener" class="card-btn" title="Open in YouTube">
            YouTube ↗
          </a>
          ${dedicatedBtn}
          ${dspButtons}
        </div>
      </div>
    `;

    container.appendChild(card);
  });
}

function resetSearch() {
  document.getElementById('searchInput').value = '';
  searchQuery = '';
  renderReleases();
}

function toggleGallery() {
  const drawer = document.getElementById('gallery-drawer');
  const btn = document.getElementById('btn-toggle-gallery');
  const isOpen = drawer.classList.contains('open');

  if (isOpen) {
    drawer.classList.remove('open');
    btn.classList.remove('active');
  } else {
    drawer.classList.add('open');
    btn.classList.add('active');
  }
}

function openVideoModal(videoId, title) {
  const modal = document.getElementById('videoModal');
  const embed = document.getElementById('modalEmbed');
  const meta = document.getElementById('modalMeta');

  embed.innerHTML = `
    <iframe 
      src="https://www.youtube.com/embed/${videoId}?autoplay=1" 
      title="${title}" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  `;

  meta.innerHTML = `
    <h3 style="color:#fff; font-size:1.1rem; margin-bottom:0.25rem;">${title}</h3>
    <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank" rel="noopener" style="color:var(--accent-cyan); font-size:0.8rem; text-decoration:none;">Open in YouTube Application ↗</a>
  `;

  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal(event) {
  if (event.target.id === 'videoModal') {
    closeModalForce();
  }
}

function closeModalForce() {
  const modal = document.getElementById('videoModal');
  const embed = document.getElementById('modalEmbed');
  modal.classList.remove('active');
  embed.innerHTML = '';
  document.body.style.overflow = 'auto';
}

function openLightbox(src) {
  const modal = document.getElementById('imageModal');
  const target = document.getElementById('imageModalTarget');
  target.src = src;
  modal.classList.add('active');
}

function closeImageModal() {
  const modal = document.getElementById('imageModal');
  modal.classList.remove('active');
}

function formatDate(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
