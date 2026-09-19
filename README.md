# Absolute Value 867 website

A complete static website for the student-led engineering team at Arcadia High School. The working preview is available at **http://127.0.0.1:8670** while the preview process is running. No public launch has occurred.

## Open or restart the preview

Install Node.js if needed, open this folder in a terminal, and run:

```sh
npm run build
npm run preview
```

Then open **http://127.0.0.1:8670**. Stop a server you started in your terminal with Ctrl+C. The site itself has no package dependencies, database, accounts, or administration service.

## Everyday updates

All team content is in the `content` folder. These are ordinary JSON text files. Keep commas and quotation marks intact; `npm run build` will point out invalid JSON. After each content edit, run `npm run build`, then refresh the preview.

| What to change | Where | How |
| --- | --- | --- |
| Team leads | `content/leaders.json` | Update name, role, season, and portrait filename. Add a bio only if supplied. Put the portrait in `dist/assets`; omit `bio` when none is available. |
| A season or historical milestone | `content/history.json` | Add a record under `frcSeasons`, `milestones`, or `awards`. Use the documented year. Named FRC robots automatically get a detail page; unspecified robot names stay unspecified. |
| A robot or engineering project | `content/projects.json` | Add a unique `slug`, name, year (or `null`), category (`FRC`, `JPL`, `Other`), status, summary, and source. Set `featured: true` on the FRC project to feature on the homepage. Optional fields: `challenge`, `approach`, `results`, `future` (paragraph arrays), image, alt, caption, related project slugs. Future work belongs under `future` or a clear planned status. |
| Regular meeting times | `content/events.json` → `meetings` | Update days, time, and note. Keep occasional meetings distinct from regular times. |
| Competitions and tryouts | `content/events.json` | Update `seasonalWindows` for general annual timing. Add confirmed dated events to `upcoming`; move completed ones to `past`. Fields: name, date (ISO date or month), dateLabel, time, timezone, location, kind, status, url, linkLabel. Leave unknown details `null`; do not invent exact dates. |
| Photos and captions | `content/gallery.json` | Add the image basename, descriptive alt text, caption, category, year or `null`, and source. Store optimized `.webp` images in `dist/assets`. Filters update from the categories automatically. |
| Current sponsors | `content/sponsors.json` → `current` | Add objects such as `{ "name": "Confirmed sponsor", "url": "https://official-website.example", "logo": "/assets/sponsor.webp" }`. Omit unknown `url` or `logo` fields. Keep `previous` separate. The home and sponsor pages update together. |
| Sponsorship benefits | `content/sponsors.json` → `tiers` | Edit only approved benefits and inheritance. Costs under `costs` are program estimates, not tier prices. |
| Replace the packet | `dist/downloads/absolute-value-867-sponsorship.pdf` | Replace the PDF using the same filename. Update the cover thumbnail in `dist/assets/packet-cover.png` and the stated page count/file size in `scripts/build.mjs` if changed. |
| Team contact and main prose | `content/team.json` | Update the email, Instagram URL, school information, and approved source copy. |
| Outreach | `content/outreach.json` | Keep completed activities dated; keep planned work separate. |

Keep a copy of the original images outside the public assets folder. Prefer originals at least 1200px wide for wide photographs. Never use a screenshot as a replacement for editable body text. Photographs without confirmed dates should stay undated.

## Site structure

`scripts/build.mjs` generates real HTML for every route into `dist`. Shared layouts are in that builder; shared design and interactions are in `dist/assets/styles.css` and `dist/assets/site.js`. The site works for reading and navigation without JavaScript; JavaScript adds the compact mobile menu, gallery dialog, and filters. Do not edit generated page HTML directly because the next build replaces it.

The navigation covers Our Team, Team Leads, FRC Robots, JPL & Other Projects, Outreach, Schedule & Join, Over the Years, Gallery, Sponsor Us, and Contact, plus individual project pages.

The added packet-inspired visual styling lives in `dist/assets/packet-theme.css`. Original packet artwork is named `pixel-*` in `dist/assets`; its provenance is recorded in `docs/brand-assets.json`. The locally hosted DotGothic16 font is intentionally limited to short labels and the homepage number. Keep body text and main navigation in the regular sans-serif.

## Check changes

```sh
npm run build
npm run check
```

The static checks cover routes, local references, metadata, image alternative text, corrected names, template-content exclusions, sponsorship inheritance, and the PDF. `docs/browser-checks.json` records the browser validation. The optional `scripts/browser-check.py` uses Python Playwright and installed Chrome to check responsive layouts and interactions; those tools are for development, not required to run the site.

Review [the content checklist](docs/CONTENT-REVIEW.md) before publication. [The source map](docs/SOURCE-MAP.md) identifies where major sections and images came from.

## Publication

### Vercel

The root `vercel.json` configures this as a static site: Framework Preset **Other**, Build Command **npm run build**, and Output Directory **dist**. Commit and push this file with the site to the connected GitHub branch so the next deployment uses it. These file-based settings override the corresponding Vercel project settings.

If a deployment reports “No Output Directory named public found,” the build has succeeded but Vercel is looking in the wrong folder. Deploy a commit containing `vercel.json`, or set the project's Output Directory to **dist** in Vercel and redeploy. Keep `dist/assets` and `dist/downloads` tracked; the build generates page HTML alongside those authored assets.

The static `dist` folder can also be packaged for Sites hosting if requested. Only the contents of `dist` are public website output; `.tools`, `tmp`, and source-reference folders are not part of the deployed site. Current sponsor information and corrected packet text can be added before launch. No analytics, donation links, contact forms, or external accounts have been added.
