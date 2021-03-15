import i18next from 'https://deno.land/x/i18next/index.js';
// import Backend from 'https://deno.land/x/i18next_fs_backend/index.js';
import BackendAdapter from 'https://cdn.jsdelivr.net/gh/i18next/i18next-multiload-backend-adapter/src/index.js'
import Fetch from 'https://cdn.jsdelivr.net/gh/dotcore64/i18next-fetch-backend/src/index.js'

i18next
.use(BackendAdapter)
.init({
backend: {
    backend: Fetch,
    backendOption:{
      loadPath: '../i18n/de.json',
      allowMultiLoading:  true,
      multiSeparator: '+',
    }
  },
lng: 'de',
/*resources: {
},*/
fallbackLng: 'de',
preload: ['de'],
}), function(err, t) {
// initialized and ready to go!
};
for (let i = 0; i < document.querySelectorAll('[data-i18n]').length; i++) { 
    document.querySelectorAll('[data-i18n]')[i].innerHTML = i18next.t(document.querySelectorAll('[data-i18n]')[i].getAttribute("data-i18n"));
}
