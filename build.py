#!/usr/bin/env python3
"""
Generate the site's HTML pages from src/base.html + src/pages/*.html.

The output is plain, self-contained HTML — no runtime dependency on this
script. It exists so the shared header, footer and <head> stay identical
across every page instead of drifting across 25 hand-edited copies.

    python3 build.py            build every page listed in PAGES
    python3 build.py about-us   build one page

Add a page: drop the <main> content in src/pages/<slug>.html and add an
entry to PAGES below.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent
BASE = ROOT / "src" / "base.html"
PAGES_DIR = ROOT / "src" / "pages"

# slug -> (output filename, <title>, meta description, canonical path, nav item to mark active)
PAGES = {
    "index": (
        "index.html",
        "Home - IntelliGenesis LLC",
        "IntelliGenesis turns AI and cyber innovation into mission-ready capability, "
        "moving faster from concept to operational impact for the defense, intelligence, "
        "and federal communities.",
        "",
        "index",
    ),
    "about-us": (
        "about-us.html",
        "About Us - IntelliGenesis LLC",
        "IntelliGenesis has made its name in the Intelligence Community as a trusted "
        "provider of data science, cyber and AI/ML solutions for the defense, "
        "intelligence and federal communities.",
        "about-us/",
        None,
    ),
}

NAV_KEYS = [
    "index", "ig_labs", "intellicademy", "mission_services",
    "technologies", "careers", "contact_us_form",
]


def build(slug):
    if slug not in PAGES:
        raise SystemExit(f"unknown page '{slug}' — add it to PAGES in build.py")

    out_name, title, description, canonical, active = PAGES[slug]
    content_file = PAGES_DIR / f"{slug}.html"
    if not content_file.exists():
        raise SystemExit(f"missing content file: {content_file}")

    html = BASE.read_text(encoding="utf-8")
    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{DESCRIPTION}}", description)
    html = html.replace("{{CANONICAL}}", canonical)
    html = html.replace("{{CONTENT}}", content_file.read_text(encoding="utf-8").rstrip("\n"))

    for key in NAV_KEYS:
        html = html.replace(
            "{{ACTIVE_%s}}" % key,
            ' class="uk-active"' if key == active else "",
        )

    (ROOT / out_name).write_text(html, encoding="utf-8")
    return out_name, len(html)


if __name__ == "__main__":
    targets = sys.argv[1:] or list(PAGES)
    for slug in targets:
        name, size = build(slug)
        print(f"  built {name:<28} {size:>7,d} bytes")
    print(f"{len(targets)} page(s) built")
