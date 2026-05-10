# gpg-test

Mobile Web Runner (single-page app) for opening websites in a mobile-friendly iframe shell.

## Run locally

Open `index.html` directly in a browser, or serve locally:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Run now (verified)

```bash
python3 -m http.server 8080
```

Open: `http://127.0.0.1:8080`

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
