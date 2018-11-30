var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/static/core/css/estilos.css',
        '/static/core/img/Duque.jpg',
        '/static/core/img/Chocolate.jpg',
        '/static/core/img/Luna.jpg',
        '/static/core/img/Maya.jpg',
        '/static/core/img/Bigotes.jpg',
        '/static/core/img/Oso.jpg',
        '/static/core/img/Pexel.jpg',
        '/static/core/img/Wifi.jpg',
        '/static/core/js/jquery-3.1.1.min.js',
        '/intermedio/',
        '/',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});