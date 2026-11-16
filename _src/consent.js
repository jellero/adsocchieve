/* Consenso cookie e Google Analytics 4 (Consent Mode v2).
   Analytics parte solo dopo "Accetta"; la scelta resta nel browser e si cambia da "Preferenze cookie". */
(() => {
  'use strict';
  const GA_ID = 'G-WPJJCPTR36';
  const KEY = 'adsocchieve-consent-v1';
  const lang = (document.documentElement.lang || 'it').slice(0, 2);
  const T = {
    it: {
      text: 'Usiamo cookie tecnici per far funzionare il sito e, solo se accetti, Google Analytics per misurare in forma aggregata le visite.',
      more: 'Informativa cookie', href: '/cookies', accept: 'Accetta', reject: 'Rifiuta', label: 'Preferenze cookie'
    },
    en: {
      text: 'We use technical cookies to run the website and, only if you accept, Google Analytics to measure visits in aggregate form.',
      more: 'Cookie policy', href: '/en/cookies', accept: 'Accept', reject: 'Reject', label: 'Cookie preferences'
    },
    de: {
      text: 'Wir verwenden technische Cookies für den Betrieb der Website und, nur wenn Sie zustimmen, Google Analytics, um Besuche in zusammengefasster Form zu messen.',
      more: 'Cookie-Hinweise', href: '/de/cookies', accept: 'Akzeptieren', reject: 'Ablehnen', label: 'Cookie-Einstellungen'
    }
  };
  const L = T[lang] || T.it;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied', wait_for_update: 500
  });

  const read = () => { try { return localStorage.getItem(KEY); } catch (_) { return null; } };
  const write = value => { try { localStorage.setItem(KEY, value); } catch (_) { /* scelta valida solo per la pagina */ } };

  let loaded = false;
  const loadAnalytics = () => {
    window.gtag('consent', 'update', { analytics_storage: 'granted' });
    if (loaded) return;
    loaded = true;
    const s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
  };

  const clearAnalyticsCookies = () => {
    document.cookie.split(';').map(c => c.trim().split('=')[0]).filter(n => /^_ga/.test(n)).forEach(name => {
      const host = location.hostname.replace(/^www\./, '');
      [host, '.' + host, location.hostname].forEach(domain => {
        document.cookie = name + '=; Max-Age=0; path=/; domain=' + domain;
      });
      document.cookie = name + '=; Max-Age=0; path=/';
    });
  };

  let banner = null;
  const close = () => { if (banner) { banner.remove(); banner = null; } };
  const choose = value => {
    write(value);
    close();
    if (value === 'granted') loadAnalytics();
    else { window.gtag('consent', 'update', { analytics_storage: 'denied' }); clearAnalyticsCookies(); }
  };

  const open = () => {
    if (banner) return;
    banner = document.createElement('div');
    banner.className = 'consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', L.label);
    banner.innerHTML = '<p></p><div class="consent-actions"><button type="button" class="btn consent-reject"></button><button type="button" class="btn btn-dark consent-accept"></button></div>';
    const p = banner.querySelector('p');
    p.textContent = L.text + ' ';
    const a = document.createElement('a');
    a.href = L.href; a.textContent = L.more;
    p.appendChild(a);
    banner.querySelector('.consent-reject').textContent = L.reject;
    banner.querySelector('.consent-accept').textContent = L.accept;
    banner.querySelector('.consent-reject').addEventListener('click', () => choose('denied'));
    banner.querySelector('.consent-accept').addEventListener('click', () => choose('granted'));
    document.body.appendChild(banner);
  };

  document.addEventListener('click', event => {
    const trigger = event.target.closest('[data-cookie-settings]');
    if (!trigger) return;
    event.preventDefault();
    open();
  });

  const start = () => {
    const saved = read();
    if (saved === 'granted') loadAnalytics();
    else if (saved !== 'denied') open();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
