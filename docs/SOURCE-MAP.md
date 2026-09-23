# Source map

Primary source: `C:\Users\dylan\Downloads\Arcadia EDD Absolute Value 867 Sponsorship Packet 26-27.pdf` (the finished 2026–2027 packet, supplied 2026-09-20), 17 pages, cover season 2026–2027. All 17 rendered pages were inspected alongside text extraction. The verbatim extraction in `sources/packet-extracted.txt` is archival evidence and includes decorative duplicates; it is never rendered on the site. Regenerate it from the published copy with `python -m pymupdf gettext -mode layout`.

Against the packet this replaces, the finished packet changes the printed website from the retired Weebly address to `www.867arcadiaedd.com`, renames contents entry 04 to “meet the team”, and renumbers the closing sections (our partners 16, sponsorship tier benefits 17, contact us 18). Body copy, figures, costs, tiers, supporter list, and photographs are unchanged; five portraits and decorative panels were re-exported without any change to what they show. Contents entry “15. ww” points at a page the PDF does not contain.

Secondary sources inspected:

- [Wix Home and its About Us section](https://dylanlin2009.wixstudio.com/867-absolute-value)
- [Wix Over the Years](https://dylanlin2009.wixstudio.com/867-absolute-value/home-1)
- [Wix Projects Portfolio](https://dylanlin2009.wixstudio.com/867-absolute-value/projects)
- [Wix Sponsors](https://dylanlin2009.wixstudio.com/867-absolute-value/home-2)
- [Team 254](https://www.team254.com/) for conventional navigation and program/archive organization only. No Team 254 copy, facts, photographs, or branding are used.

Wix's About Us navigation points to the home page/section, not a separate About URL. Source text and media lists are saved in `docs/sources/` for review. Raw HTML is ignored by Git.

| Major section / route | Primary source | Content file / treatment |
| --- | --- | --- |
| Home introduction and philosophy | Packet pp. 3–4 | `content/team.json`; complete short excerpts |
| Homepage About Us, below the three quick links | Packet p. 3 | `content/team.json`: first two `about` paragraphs, shared with Our Team |
| Homepage programs | Packet p. 10; user program-name clarification | `team.json`; combined JPL Invention Challenge / Wonderworks title |
| Homepage featured robot | Wix Over the Years, January–April 2026 | `projects.json`; Biocore / Limelight alignment |
| Our Team | Packet pp. 3–4, 8 | `team.json`; 10 returning members correction |
| 867 by the numbers, on Our Team | Packet p. 12 | `stats.json`; published figures only, returning members from p. 12 rather than the different p. 8 figure |
| Team Leads | Packet pp. 5–7; supplied brief | `leaders.json`; 2026–2027 roster, Tiger Hou correction, only supplied personal bio |
| Team departments | Packet pp. 5–7 | `departments.json`; department copy is not invented personal biography |
| FRC overview | Packet p. 10 | `team.json`; complete paragraphs |
| Engineering detail pages | Packet p. 11 | `projects.json`; undated where no year is given |
| JPL overview | Packet p. 10 | `team.json`; source description distinguished from new Wonderworks material |
| Bucket Brigade / Still Water | Wix Over the Years; packet p. 13; user date correction | `projects.json`; December 2025, complete challenge/design/result copy, blank team names excluded |
| JPL archived projects | Packet p. 13 | `projects.json`; published named years and results |
| Outreach | Packet p. 14 | `outreach.json`; 2019/2020 historical work separated from planned initiatives |
| Schedule & Join | User's meeting, tryout, and competition-window confirmations; Wix street address | `events.json`; Pacific time; no invented application rules or exact dates |
| Past events | Wix Over the Years; user December 2025 correction | `events.json`; month-level dates retained as month-level dates |
| Over the Years | Wix Over the Years; packet p. 13 award priority | `history.json`; season entries linked to available detail pages |
| Gallery | Genuine images extracted from packet pp. 3, 5–7, 17; Wix 2026 rendering | `gallery.json`; neutral visible descriptions, no template captions |
| Funding and equipment | Packet pp. 3, 9, 15 | `sponsors.json`; approximate costs labeled as packet budget estimates |
| Sponsorship tiers | Packet p. 16, visually checked | `sponsors.json`; all incremental benefits and explicit inheritance retained |
| Previous supporters | Packet p. 15 | `sponsors.json`; no current sponsorship claim |
| Current sponsors | User instruction to keep blank | `sponsors.json`; empty state |
| Contact | User brief; packet p. 17; Wix footer | `team.json`; exact email and Instagram handle |
| Download | Finished packet supplied 2026-09-20 | Unedited copy at `dist/downloads/absolute-value-867-sponsorship.pdf`; stated size updated to 13.4 MB |

## Asset provenance

Images are optimized WebP copies, never generated representations of the team. Source PDF image IDs are recorded by `scripts/prepare-assets.py`.

| Assets | Source |
| --- | --- |
| `logo`, `favicon`, `pixel-star`, `packet-cover` | Packet pp. 1 / 17; extracted matching logo, not redrawn |
| `workshop` | Packet p. 3 |
| `mechanical-workshop`, `controls-workshop`, Dylan / Iris / Cyrus portraits | Packet p. 5 |
| Amanda portrait, `team-collaboration`, `robot-assembly`, `robot-testing`, `hands-on` | Packet p. 6 |
| Tiger / Kay portraits, `cad-work` | Packet p. 7 |
| `team-photo` | Packet p. 17; date not supplied |
| `frc-render` | Wix Home, `473aab_0741bf2f03ff4058b73ef7ed6d77e442~mv2.png`, original filename `FRC 2026 v1.png` |

Unused downloaded screenshot-based images remain research material and are not presented as identified project photographs. CSS graph lines are simple functional geometry. The packet cover is a download thumbnail; body copy remains selectable HTML text.

## Pixel and pastel styling update

The original packet's stars (p. 1), wrench (p. 5), blue gear (p. 9), trophy (p. 10), people and handshake (p. 15), envelope (p. 17), and flowers (p. 7) supply decorative icons. The stacked pixel 867 graphic is a clean crop from the cover. These are extracted original assets, not generated artwork. `docs/brand-assets.json` records the PDF image identifiers and source pages; `scripts/prepare-brand-assets.py` reproduces the extraction.

DotGothic16 is self-hosted from Google Fonts for short labels and the homepage's 867 only. Its SIL Open Font License is included at `dist/assets/fonts/DotGothic16-OFL.txt`. Main headings, navigation, and body copy retain the readable sans-serif. Styles for these accents are in `dist/assets/packet-theme.css`. The Spring and Fall program bars are removed, and their labels are exactly SPRING and FALL, per user instruction.

## Editorial changes

Only obvious spelling, punctuation, capitalization, artificial letter spacing, hyphenation, and repeated text layers were normalized. Examples: “robot.Our” → “robot. Our”; “camerastogether” → “cameras together”; “resevoir” → “reservoir”; “main accomplish” → “main accomplishment”; “Developement” → “Development.” Repeated passages are deduplicated. Short project summaries and functional headings describe documented content; the detailed prose preserves source wording. Original incomplete text and suggested fixes are recorded in `CONTENT-REVIEW.md` instead of being silently completed.

## Homepage JPL win feature
- December 2025 first-place student-team result and 6.45-second run: NASA, https://www.nasa.gov/centers-and-facilities/jpl/invention-challenge-brings-student-engineers-to-nasa-jpl/
- Photo matching the user attachment: https://www.nasa.gov/wp-content/uploads/2025/12/e1-ic.jpg, saved as dist/assets/still-water-jpl-2025.jpg; credited NASA/JPL-Caltech. Full image proportions preserved.


## Updated downloadable sponsorship packet
- Source: Arcadia EDD Absolute Value 867 Sponsorship Packet 26-27.pdf, supplied by the user on September 22, 2026.
- PDF page 16 (printed page 17): Wood $100+, Brick $300+, Steel $600+, Carbon Fiber $1,000+. Existing tier benefits and inheritance retained.
- Download replaced byte-for-byte at dist/downloads/absolute-value-867-sponsorship.pdf; cover thumbnail refreshed from page 1. 17 pages, 5,070,323 bytes.

