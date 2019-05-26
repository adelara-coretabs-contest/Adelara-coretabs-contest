const staticCacheName = 'site-static-v3';
const dynamicCacheName = 'site-dynamic-v3';
const assets = [
  '/',
  '/js/app.js',
  '/css/styles.css',
  '/img/404.png',
  '/img/chef-playing.png',
  '/img/chef.png',
  '/img/cloud-v.png',
  '/img/icon.png',
  '/img/icon-72x72.png',
  '/img/icon-96x96.png',
  '/img/128x128.png',
  '/img/loading.png',
  '/img/success.png',
  'https://fonts.googleapis.com/css?family=Handlee&display=swap',
  'https://fonts.googleapis.com/css?family=Homemade+Apple&display=swap',
];


const limitCacheSize = (name, size) => {
  caches.open(name).then(cache => {
    cache.keys().then(keys => {
      if(keys.length > size){
        cache.delete(keys[0]).then(limitCacheSize(name, size));
      }
    });
  });
};

// install event
self.addEventListener('install', evt => {
  console.log('Ok, sw installed');
  evt.waitUntil(
    caches.open(staticCacheName).then((cache) => {
      console.log('caching shell assets');
      cache.addAll(assets);
    })
  );
});

// activate event
self.addEventListener('activate', evt => {
  console.log('Ok, swactivated');
  evt.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(keys
        .filter(key => key !== staticCacheName && key !== dynamicCacheName)
        .map(key => caches.delete(key))
      );
    })
  );
});

// fetch events
self.addEventListener('fetch', evt => {
  if(evt.request.url.indexOf('firestore.googleapis.com') === -1){
    evt.respondWith(
      caches.match(evt.request).then(cacheRes => {
        return cacheRes || fetch(evt.request).then(fetchRes => {
          return caches.open(dynamicCacheName).then(cache => {
            cache.put(evt.request.url, fetchRes.clone());
            // check cached items size
            limitCacheSize(dynamicCacheName, 15);
            return fetchRes;
          })
        });
      }).catch(() => {
        console.log('Check your network');
        alert('Check your network')
        } 
      )
    );
  }
});