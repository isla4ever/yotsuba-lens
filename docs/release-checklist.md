# Release Checklist

This checklist keeps Design Lens releases reproducible and preserves the
permission boundary between the standard and Collector builds.

## 1. Prepare The Candidate

- Work from a branch based on the latest `main`.
- Use the Node version declared in `.nvmrc`.
- Keep `package.json`, `package-lock.json`, the extension manifest, README
  badges, and `CHANGELOG.md` on the same version.
- Confirm user-visible behavior and known limitations are in `CHANGELOG.md`.
- Do not commit `.output/`, `dist/`, `output/`, captured pages, or credentials.

## 2. Run Local Gates

```bash
npm ci
npm run audit:dependencies
npm run check:all
npx playwright install chromium
npm run check:browser
npm run package:release
cd dist && shasum -a 256 -c SHA256SUMS
```

`package:release` rejects version drift, renamed variants, host-permission
changes, and any permission set outside the explicit standard/Collector
allowlists.

## 3. Merge Through A Protected Branch

Open a pull request and require these CI jobs before merge:

- `Types, tests, and builds`
- `Browser performance and recovery`
- `Reproducible release package`

For `main`, require pull requests, successful checks, resolved conversations,
and protection from force pushes and deletion. Enable these rules only after the
new workflow has completed once so GitHub can resolve the required check names.

## 4. Create The Draft Release

After the release commit is merged into protected `main`:

```bash
git tag -a v0.3.0 -m "Design Lens v0.3.0"
git push origin v0.3.0
```

The tag workflow reruns dependency, code, browser, packaging, and permission
gates. It creates a draft GitHub release with:

- `design-lens-0.3.0-standard-chrome.zip`
- `design-lens-0.3.0-collector-chrome.zip`
- `SHA256SUMS`

Before publishing the draft, verify both checksums, load each unpacked build in
a clean Chrome profile, and confirm only Collector requests `debugger`.

## 5. Submit The Standard Build To Chrome Web Store

- Upload only `dist/design-lens-0.3.0-standard-chrome.zip`.
- Use the listing, permission justifications, reviewer steps, and data-use
  declarations in `docs/chrome-web-store-listing.md`.
- Upload the store icon, two screenshots, and small promotional tile from
  `docs/store-assets/` and verify their dimensions in the dashboard preview.
- Confirm **No remote code**, the public privacy-policy URL, and the Limited Use
  attestations before submission.
- Select deferred publishing so approval does not make the release live before
  the final dashboard review.
- Never upload the Collector build to Chrome Web Store; distribute it only as a
  clearly labeled GitHub release artifact.

## 6. Recovery

Do not move or reuse a published version tag. If a candidate fails before
publication, delete only the draft and create a corrected candidate. If a
published release is defective, document the issue and publish a new patch
version.
