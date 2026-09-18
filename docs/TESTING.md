# Validation

Run `npm run build` and `npm run check` after content changes. The final browser run is recorded in `browser-checks.json`.

The site has 38 HTML pages: the requested main pages, documented project/robot details, and a useful not-found page. The complete route list is in `routes.json`.

The static checks validate every local page/asset reference, a single page heading, titles, language metadata, image alternative-text attributes, source-copy safeguards, tier inheritance and benefit counts, client JavaScript syntax, and the downloadable PDF signature.

Browser checks cover each route at 1440, 768, 390, and 320 CSS pixels. They verify successful loading, no horizontal overflow, and loaded images. Interactive checks cover the mobile menu, nested navigation, keyboard skip link, visible focus, Enter/Escape navigation, gallery filters, image-dialog focus/close behavior, project filters and their empty state, the PDF response, contact destinations, and 200% root text size on the home, join, and sponsorship pages.

Visual review includes the homepage, sponsorship page, leadership page, schedule, and gallery across phone, tablet, and desktop sizes. The restrained palette uses dark indigo on white/light backgrounds; peach, blue, pink and purple are accents. Thin gray graph lines are decorative. Photography is from team sources and optimized as WebP; the largest displayed photo is approximately 152 KB.

The supplied Instagram destination returned HTTP 200 at `https://www.instagram.com/ahs.frc867/` and contained the same handle. Email links match `arcadiaedd.team867@gmail.com`; no test message was sent and mailbox deliverability was not tested.

The local server binds to `127.0.0.1:8670`, and a non-browser readiness request returned HTTP 200. A user-facing browser integration was unavailable in this session, so the preview was handed off as a clickable local URL. Headless Chrome was used for the requested browser testing. No Sites publication or other external write was performed.

Joining, seasonal competition dates, sponsorship, and contact information are reachable within two navigation actions from the homepage, including on mobile: Menu → Schedule & Join or Sponsor Us. Joining and sponsorship also have direct homepage links; email and Instagram are directly available in the footer.

No claim of a full WCAG audit or assistive-technology certification is made. Unresolved source-content issues are in `CONTENT-REVIEW.md`.
