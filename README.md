# gpg-test

Mobile Web Runner (single-page app) for opening websites in a mobile-friendly iframe shell.

## Run locally

Open `index.html` directly in a browser, or serve locally:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Deploy on GitHub Pages (public link)

1. Create a new GitHub repository.
2. Push this project:

```bash
git add .
git commit -m "Mobile web runner"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git push -u origin main
```

3. In GitHub: `Settings` → `Pages`.
4. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/(root)**
5. Click **Save**.
6. Your live URL will be:

```text
https://<YOUR_USERNAME>.github.io/<REPO_NAME>/
```

## Features

- URL input with auto `https://` normalization
- Back / Forward / Reload controls
- Responsive layout optimized for phones
- Simple iframe-based browsing experience

> Note: Some websites block iframe embedding via CSP/X-Frame-Options.

## Trusted Defensive Security Toolkit (Authorized Use Only)

> Use security tools only on assets you own or where you have explicit written permission.

### Asset Discovery (Defensive)
- **Amass**: external asset mapping and subdomain discovery.
- **Subfinder**: passive subdomain enumeration.
- **Katana**: web crawling to inventory visible routes.
- **gau / waybackurls**: historical URL collection for exposure review.

### Validation & Triage
- **Nuclei**: template-based vulnerability checks.
- **Dalfox**: XSS-focused testing in approved scope.
- **Burp Suite / OWASP ZAP**: manual verification of findings.

### Code & Configuration Review
- **Semgrep**: static analysis and secure-code checks.
- **Gitleaks**: secret detection in repositories.
- **Trivy**: container and dependency vulnerability scanning.

### Monitoring & Reporting
- Keep logs for every scan run (tool name, target, timestamp).
- Track remediation status (open, in-progress, fixed, verified).
- Share concise reports with impact and mitigation steps.

### Guardrails
- No auto-exploitation, malware, C2, credential theft, or persistence tooling.
- Respect legal scope, rate limits, and responsible disclosure.


## Private Access + Task Resume

- App auto-generates a private key on first run and saves it in browser `localStorage` (`mobile_runner_access_key_v1`).
- Share link as: `https://<your-domain>/?k=<your-generated-key>`
- To view your key once on owner device: open DevTools Console and run `localStorage.getItem('mobile_runner_access_key_v1')`.
- App saves navigation history in `localStorage` and resumes last task after reopen/reload.
- Works offline for already loaded app files when browser cache is available.
