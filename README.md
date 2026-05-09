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
