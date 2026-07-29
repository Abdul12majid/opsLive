// ── Mock Data ─────────────────────────────────────────────────────────────────

const JOBS = [
  {
    id: 2367,
    title: 'P7 Melissa Powell AHS ITEM 2 Microwave NORMAL 67302099',
    customer: 'Melissa Powell',
    customerId: 3868,
    phone: '(702) 806-6431',
    email: 'mzpowell26@hotmail.com',
    secondary: 'MELISSA POWELL',
    phone2: '(702) 761-0867',
    rating: 'None',
    address: '7015 Crimson Shadow St, NORTH LAS VEGAS, NV 89086, USA',
    scheduled: '07/24/26 - 12:01 AM',
    effective: '11/12/2025',
    woReceived: '07/22/2026 @ 07:40 AM',
    dispatch: '67302099',
    assignedTo: 'Jamie',
    appliance: 'MICROWAVE',
    brand: 'Samsung',
    model: 'None',
    problem: 'Not advancing through cycles. Not draining. Other Door locks unexpectedly.',
    status: 'new',
    source: 'AHS',
    tags: ['NEW','Diag','Source Parts','Review Parts','Order Part','Parts Ordered','To-be Authorized','Online Authorized','Voice Authorized','Invoice','Admin','Completed','Cancelled'],
    adminNote: '',
    diagNotes: '',
    paid: true,
    amount: 0,
  },
  {
    id: 2366,
    title: 'P7 Melissa Powell AHS ITEM 1 Washer NORMAL 67302099',
    customer: 'Melissa Powell',
    customerId: 3868,
    phone: '(702) 806-6431',
    email: 'mzpowell26@hotmail.com',
    secondary: 'MELISSA POWELL',
    phone2: '(702) 761-0867',
    rating: 'None',
    address: '7015 Crimson Shadow St, NORTH LAS VEGAS, NV 89086, USA',
    scheduled: '07/24/26 - 12:01 AM',
    effective: '11/12/2025',
    woReceived: '07/22/2026 @ 07:40 AM',
    dispatch: '67302099',
    assignedTo: 'Jamie',
    appliance: 'WASHER',
    brand: 'Samsung',
    model: 'WF45R6100AW',
    problem: 'Not spinning. Loud noise during wash cycle.',
    status: 'new',
    source: 'AHS',
    tags: ['NEW','Diag'],
    adminNote: '',
    diagNotes: '',
    paid: false,
    amount: 125,
  },
];

// ── Sidebar HTML ──────────────────────────────────────────────────────────────
function buildSidebar(activePage) {
  const nav = [
    { label:'Dashboard', page:'base.html',            icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>` },
    { label:'Customers', page:'customer_list.html',   icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>` },
    { label:'Jobs',      page:'job_info.html',        icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-4 0v2"/><path d="M8 7V5a2 2 0 0 0-4 0v2"/><line x1="8" y1="12" x2="16" y2="12"/><line x1="8" y1="16" x2="12" y2="16"/></svg>`, badge:5 },
    { label:'Schedule',  page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>` },
    { label:'Mgmt',      page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93A10 10 0 1 0 4.93 19.07"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>` },
    { label:'Analytics', page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>` },
    { label:'Admin',     page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>` },
    { label:'Parts',     page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M6.34 17.66l-1.41 1.41M2 12h2M20 12h2M17.66 17.66l1.41 1.41M4.93 4.93l1.41 1.41"/></svg>`, badge:3 },
    { label:'Messages',  page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>`, badge:12 },
    { label:'Mobile',    page:'#',                    icon:`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="7" y="2" width="10" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>` },
  ];

  const items = nav.map(n => `
    <li class="nav-item">
      <a href="${n.page}" class="nav-link ${activePage === n.page ? 'active' : ''}">
        <span class="nav-icon">${n.icon}</span>
        <span class="nav-label">${n.label}</span>
        ${n.badge ? `<span class="nav-badge">${n.badge}</span>` : ''}
      </a>
    </li>`).join('');

  return `
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-brand">
        <div class="brand-icon">OL</div>
        <span class="brand-name">OpsLive</span>
      </div>
      <nav class="sidebar-nav">
        <ul>${items}</ul>
      </nav>
      <div class="sidebar-footer">
        <div class="sidebar-user">
          <div class="avatar">OM</div>
          <div class="user-info">
            <div class="user-name">Admin User</div>
            <div class="user-role">Operations Manager</div>
          </div>
        </div>
      </div>
    </aside>`;
}

// ── Topbar HTML ───────────────────────────────────────────────────────────────
function buildTopbar(title, subtitle, actions = '') {
  return `
    <header class="topbar">
      <button class="icon-btn" id="menu-toggle" onclick="toggleMobileSidebar()" style="display:none">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      <div class="topbar-title">${title}${subtitle ? `<span>${subtitle}</span>` : ''}</div>
      <div class="topbar-actions">
        <div class="topbar-search">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" placeholder="Quick search...">
        </div>
        ${actions}
        <button class="icon-btn" title="Notifications">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span class="notif-dot"></span>
        </button>
        <button class="icon-btn" title="Refresh">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>
        </button>
        <button class="theme-toggle" id="theme-toggle" onclick="toggleTheme()" title="Toggle dark / light mode">
          <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
          <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
        <div class="topbar-avatar" title="Account">OM</div>
      </div>
    </header>`;
}

// ── Theme Toggle ─────────────────────────────────────────────────────────────
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try { localStorage.setItem('theme', next); } catch (e) {}
}
(function initTheme() {
  let saved = 'light';
  try { saved = localStorage.getItem('theme') || 'light'; } catch (e) {}
  document.documentElement.setAttribute('data-theme', saved);
})();

// ── Toast ─────────────────────────────────────────────────────────────────────
function showToast(message, type = 'success') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    container.id = 'toast-container';
    document.body.appendChild(container);
  }
  const icons = {
    success: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>`,
    error:   `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`,
    info:    `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0ea5e9" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`,
  };
  const t = document.createElement('div');
  t.className = `toast ${type}`;
  t.innerHTML = `${icons[type] || icons.info}<span>${message}</span>`;
  container.appendChild(t);
  setTimeout(() => t.remove(), 3500);
}

// ── Mobile sidebar toggle ─────────────────────────────────────────────────────
function toggleMobileSidebar() {
  document.getElementById('sidebar')?.classList.toggle('mobile-open');
}

// ── Responsive menu button ────────────────────────────────────────────────────
function initResponsive() {
  const btn = document.getElementById('menu-toggle');
  if (btn) btn.style.display = window.innerWidth <= 768 ? 'flex' : 'none';
  window.addEventListener('resize', () => {
    if (btn) btn.style.display = window.innerWidth <= 768 ? 'flex' : 'none';
  });
}

document.addEventListener('DOMContentLoaded', initResponsive);
