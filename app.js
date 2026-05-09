const form = document.getElementById('runnerForm');
const input = document.getElementById('urlInput');
const frame = document.getElementById('webFrame');
const backBtn = document.getElementById('backBtn');
const forwardBtn = document.getElementById('forwardBtn');
const reloadBtn = document.getElementById('reloadBtn');

const historyStack = [];
let historyIndex = -1;

function normalizeUrl(value) {
  const trimmed = value.trim();
  if (!trimmed) return '';
  return /^https?:\/\//i.test(trimmed) ? trimmed : `https://${trimmed}`;
}

function loadUrl(rawUrl, push = true) {
  const normalized = normalizeUrl(rawUrl);
  if (!normalized) return;

  frame.src = normalized;
  input.value = normalized;

  if (push) {
    historyStack.splice(historyIndex + 1);
    historyStack.push(normalized);
    historyIndex = historyStack.length - 1;
  }
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  loadUrl(input.value, true);
});

backBtn.addEventListener('click', () => {
  if (historyIndex > 0) {
    historyIndex -= 1;
    loadUrl(historyStack[historyIndex], false);
  }
});

forwardBtn.addEventListener('click', () => {
  if (historyIndex < historyStack.length - 1) {
    historyIndex += 1;
    loadUrl(historyStack[historyIndex], false);
  }
});

reloadBtn.addEventListener('click', () => {
  if (historyIndex >= 0) {
    loadUrl(historyStack[historyIndex], false);
  }
});

loadUrl('https://example.com', true);
