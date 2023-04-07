chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.local.set({
    isScanningOn: true // initially on
  }, function() {
    console.log('Scanning is ON');
  });
});

chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    chrome.storage.local.get('isScanningOn', function(data) {
      if (data.isScanningOn) {
        if (
          details.url.includes('outlook.com/api/v2.0/me/messages') &&
          details.url.includes('$select=Subject') &&
          (details.method === 'POST' || details.method === 'PATCH')
        ) {
          chrome.scripting.executeScript({
            target: {tabId: details.tabId},
            files: ['content_scripts.js']
          });
        }
      }
    });
    return {cancel: false};
  },
  {urls: ['<all_urls>']},
  ['blocking']
);