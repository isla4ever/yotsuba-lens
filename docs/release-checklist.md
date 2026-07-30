# Chrome Web Store Release Checklist

This checklist keeps Design Lens store submissions reproducible and preserves
the permission boundary between the standard and Collector builds. GitHub tags
and GitHub Releases are not part of this process.

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
npm run package:store
cd dist && shasum -a 256 -c SHA256SUMS
```

`package:store` rejects version drift, renamed variants, host-permission
changes, and any permission set outside the explicit standard/Collector
allowlists.

## 3. Merge Through A Protected Branch

Open a pull request and require these CI jobs before merge:

- `Types, tests, and builds`
- `Browser performance and recovery`
- `Chrome Web Store package`

For `main`, require pull requests, successful checks, resolved conversations,
and protection from force pushes and deletion. Enable these rules only after the
new workflow has completed once so GitHub can resolve the required check names.

## 4. Create The First Store Item Manually

Chrome Web Store requires the first listing to be created in the Developer
Dashboard. The API cannot create the initial item.

- Register the publisher account, enable two-step verification, pay the one-time
  developer registration fee, and verify the contact email.
- Choose **Add new item** and upload only
  `dist/design-lens-0.3.0-standard-chrome.zip`.
- Complete Store Listing, Privacy, Distribution, and Test Instructions using
  `docs/chrome-web-store-listing.md`.
- Submit for review with automatic publishing disabled. The approved submission
  remains staged for up to 30 days.

Never upload the Collector ZIP. It adds `debugger` for explicitly authorized
development capture and is not the public store product.

## 5. Enable Store Automation After The First Item

After the first item exists, copy its extension ID and the publisher ID from the
Developer Dashboard. Link a Google Cloud service account to the publisher and
configure these GitHub Actions secrets:

- `CHROME_EXTENSION_ID`
- `CHROME_PUBLISHER_ID`
- `CHROME_SERVICE_ACCOUNT_CLIENT_EMAIL`
- `CHROME_SERVICE_ACCOUNT_PRIVATE_KEY`

Run the **Chrome Web Store** workflow with `dry_run` enabled first. After the
credential check succeeds, run it again with `dry_run` disabled. The workflow
reruns all quality gates, uploads only the standard ZIP, submits it for review,
and uses `STAGED_PUBLISH` so approval does not make it public automatically.

## 6. Recovery

If a candidate fails before submission, correct it and rebuild the same local
candidate. If a package has already been uploaded, increment the manifest
version before uploading a replacement. If review has started, cancel the
submission in the Developer Dashboard before replacing it. Never create a
GitHub Release as part of the store recovery path.
