import i18next from '/i18next/src/index.js'; // Source: 'https://deno.land/x/i18next@v19.9.2/index.js'
import BackendAdapter from 'https://cdn.jsdelivr.net/gh/i18next/i18next-multiload-backend-adapter/src/index.js'
import Fetch from 'https://cdn.jsdelivr.net/gh/dotcore64/i18next-fetch-backend/src/index.js'

/**
 * Fetches de.json from backend and then translates all HTML-elements which have a data-i18n attribute
 */
i18next
.use(BackendAdapter)
.init({
backend: {
    backend: Fetch,
    backendOption:{
      loadPath: 'content/de.json',
      allowMultiLoading:  true,
      multiSeparator: '+',
    }
  },
lng: 'de',
fallbackLng: 'de',
preload: ['de'],
}).then(function(t) {
    // after initialization is done, translate all HTML-Elements which have a data-i18n attribute
    // data-i18n attribute must have the same value as the corresponding key in the de.json-file
    for (let i = 0; i < document.querySelectorAll('[data-i18n]').length; i++) {
        document.querySelectorAll('[data-i18n]')[i].innerHTML = i18next.t(document.querySelectorAll('[data-i18n]')[i].getAttribute("data-i18n"));
    }
});

