const form = document.getElementById('runnerForm');
const input = document.getElementById('urlInput');
const frame = document.getElementById('webFrame');
const backBtn = document.getElementById('backBtn');
const forwardBtn = document.getElementById('forwardBtn');
const reloadBtn = document.getElementById('reloadBtn');
const presetSelect = document.getElementById('presetSelect');
const loadPresetBtn = document.getElementById('loadPresetBtn');
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');
const templateSelect = document.getElementById('templateSelect');
const loadTemplateBtn = document.getElementById('loadTemplateBtn');

const historyStack = [];
let historyIndex = -1;
const TASKS_KEY = 'runnerTasksV1';

const TASK_TEMPLATES = {
  recon: ['Scope review', 'Subdomain discovery', 'Endpoint mapping', 'Vulnerability validation'],
  triage: ['Reproduce issue', 'Collect evidence', 'Estimate impact', 'Prepare remediation note'],
  report: ['Draft title', 'Write steps to reproduce', 'Attach PoC/screenshots', 'Submit report'],
  webhunt: ['Open program policy', 'Collect target assets', 'Run passive recon tools', 'Validate finding and severity'],
  mobile: ['Review Android scope', 'Test auth/session', 'Check storage/secrets', 'Prepare exploitability notes'],
  performance: ['Measure baseline', 'Check heavy endpoints', 'Capture latency/errors', 'Prioritize optimizations'],
  manualtest: ['Map application in Burp/Caido', 'Capture sessions with PwnFox', 'Check authz with Autorize', 'Validate findings and write report']
};

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

function getTasks() {
  try {
    const parsed = JSON.parse(localStorage.getItem(TASKS_KEY) || '[]');
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

function saveTasks(tasks) {
  localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
}

function renderTasks() {
  const tasks = getTasks();
  taskList.innerHTML = '';

  tasks.forEach((task, index) => {
    const item = document.createElement('li');
    item.className = task.done ? 'done' : '';

    const label = document.createElement('button');
    label.type = 'button';
    label.className = 'task-toggle';
    label.textContent = `${task.done ? '✅' : '⬜'} ${task.text}`;
    label.addEventListener('click', () => {
      const nextTasks = getTasks();
      nextTasks[index].done = !nextTasks[index].done;
      saveTasks(nextTasks);
      renderTasks();
    });

    const remove = document.createElement('button');
    remove.type = 'button';
    remove.className = 'task-remove';
    remove.textContent = 'Remove';
    remove.addEventListener('click', () => {
      const nextTasks = getTasks().filter((_, i) => i !== index);
      saveTasks(nextTasks);
      renderTasks();
    });

    item.append(label, remove);
    taskList.appendChild(item);
  });
}

function loadTemplateTasks() {
  const key = templateSelect.value;
  if (!key || !TASK_TEMPLATES[key]) return;

  const tasks = getTasks();
  TASK_TEMPLATES[key].forEach((text) => tasks.push({ text, done: false }));
  saveTasks(tasks);
  renderTasks();
}

function addTask() {
  const text = taskInput.value.trim();
  if (!text) return;

  const tasks = getTasks();
  tasks.push({ text, done: false });
  saveTasks(tasks);
  taskInput.value = '';
  renderTasks();
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

loadPresetBtn.addEventListener('click', () => {
  if (!presetSelect.value) return;
  loadUrl(presetSelect.value, true);
});

presetSelect.addEventListener('change', () => {
  if (!presetSelect.value) return;
  loadUrl(presetSelect.value, true);
});

addTaskBtn.addEventListener('click', addTask);
loadTemplateBtn.addEventListener('click', loadTemplateTasks);
taskInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    event.preventDefault();
    addTask();
  }
});

renderTasks();
loadUrl('https://example.com', true);
