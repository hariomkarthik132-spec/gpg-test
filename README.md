# gpg-test

Mobile Web Runner (single-page app) for opening websites in a mobile-friendly iframe shell.

## Run locally

```bash
./start.sh 8080
```

Open one of these:
- `http://127.0.0.1:8080`
- `http://localhost:8080`


## Notebook (Jupyter/Colab) me run kaise kare

Agar terminal command work nahi kar rahi, notebook cell me ye chalao:

```python
!python3 notebook_server.py 8080
```

Phir browser me kholo:
- `http://127.0.0.1:8080`

Agar 8080 busy ho to:
```python
!python3 notebook_server.py 9090
```

## If you see "127.0.0.1 refused to connect"

1. Start server first:
```bash
./start.sh 8080
```
2. Check port is listening:
```bash
ss -ltnp | rg 8080
```
3. If busy port, run another:
```bash
./start.sh 9090
```
Then open `http://127.0.0.1:9090`.

## Link sharing (important)

- I cannot send links to your Gmail directly from this environment.
- After running locally, use this direct link in your browser: `http://127.0.0.1:8080`
- If you deploy on GitHub Pages, your shareable link will be: `https://<your-username>.github.io/<repo-name>/`

## Features

- URL input with auto `https://` normalization
- Back / Forward / Reload controls
- Bug bounty presets: HackerOne, Bugcrowd, Intigriti, YesWeHack
- Web proxies/manual testing presets: Burp Suite, Caido, PwnFox, Wireshark
- Recon/asset discovery presets: Subfinder, Amass, Aquatone, httpx, MassDNS, gau, waybackurls
- Vulnerability scanning/fuzzing presets: Nuclei, Param Miner, XSStrike, gf, Autorize
- Security recon presets: Shodan, Censys, VirusTotal, Wappalyzer, Exploit-DB, MITRE CVE
- Security framework presets: Sn1per, Axiom, Arjun, ProjectDiscovery, OWASP MSTG, Web3 security docs
- Automation presets: AutoGPT, CrewAI, PentestGPT
- AI tool presets: ChatGPT, Claude, Gemini, Perplexity, Copilot, Poe, Hugging Face
- Task chain tracker with local persistence
- One-click automation templates: Recon, Triage, Report, Web Hunt, Android Security, Performance, Manual Web Testing
- Responsive layout optimized for phones

> Note: Some websites block iframe embedding via CSP/X-Frame-Options.

## Security note

This app opens links in-browser only. It does **not** auto-install or auto-delete local tools on your device.

## Roadmap

- One-tap "open in new tab" fallback when iframe is blocked
- Import/export task chains as JSON
- Add optional priority labels (P0/P1/P2) for bounty tasks
- Add program notes and report templates per task
