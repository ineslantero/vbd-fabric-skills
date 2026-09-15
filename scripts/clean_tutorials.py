"""Clean up the SharePoint-converted tutorial markdown files."""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\inesoraa\OneDrive - Microsoft\Documents\Microsoft Scout\Fabric VBD Hack\vbd-fabric-skills\skills\vbd-lab-foundation\references")

def clean(text: str) -> str:
    text = re.sub(r"\\([.\-_()!'\":;,?/])", r"\1", text)
    text = re.sub(r'<a\s+id="[^"]*"></a>', "", text)
    text = re.sub(r"__([^_\n]+?) __", r"__\1__", text)
    text = re.sub(r"\*\*([^*\n]+?) \*\*", r"**\1**", text)
    text = re.sub(r"__ ([^_\n]+?)__", r"__\1__", text)
    text = re.sub(r"\*\* ([^*\n]+?)\*\*", r"**\1**", text)
    text = re.sub(r"!\[screenshot: image\]\(\)", "", text)
    text = re.sub(r"!\[screenshot:[^\]]*\]\(\)", "", text)

    def toc_repl(m):
        heading = m.group(1).strip()
        heading = re.sub(r"\s+\d+\s*$", "", heading)
        return f"- {heading}"
    text = re.sub(r"\[([^\]]+?)\]\(#_Toc\d+\)", toc_repl, text)

    text = text.replace("\u00a0", " ").replace("\u200b", "")

    # Paragraph reflow: walk through, group runs of prose lines (possibly with
    # blank lines) into paragraphs. A paragraph ends when we hit a structural
    # line (heading / list / code fence / table row / blockquote) OR when a
    # prose line ends with a sentence terminator followed by a blank line.
    STRUCTURAL = re.compile(r"^(#{1,6}\s|-\s|\*\s|\d+\.\s|>\s?|\||`{3}|!\[|---\s*$|\*\*\*\s*$)")
    TERMINATOR = re.compile(r"[.!?:;)\"']$")

    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        # Structural or empty -> emit and continue
        if stripped == "" or STRUCTURAL.match(stripped):
            out.append(raw)
            i += 1
            continue
        # Start a paragraph. Accumulate subsequent prose lines (skipping blank
        # lines) until we hit a structural line OR the accumulated prose ends
        # in a terminator AND the next non-blank line is structural.
        para = [stripped]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if nxt == "":
                # Peek ahead
                k = j + 1
                while k < len(lines) and lines[k].strip() == "":
                    k += 1
                if k >= len(lines):
                    break
                peek = lines[k].strip()
                if STRUCTURAL.match(peek):
                    break
                # Prev ends with terminator AND double-blank-delimited paragraph? end here
                if TERMINATOR.search(para[-1]):
                    break
                # else join across the blank line (reflow wrapped paragraph)
                para.append(peek)
                j = k + 1
                continue
            if STRUCTURAL.match(nxt):
                break
            # Consecutive prose line: join if prev didn't end sentence
            if TERMINATOR.search(para[-1]):
                break
            para.append(nxt)
            j += 1
        out.append(" ".join(para))
        out.append("")  # trailing blank line for the paragraph
        i = j

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.rstrip() + "\n"


TITLES = {
    "lakehouse": "Fabric Foundation VBD - Lakehouse Lab Tutorial",
    "warehouse": "Fabric Foundation VBD - Data Warehouse Lab Tutorial",
    "rti": "Fabric Foundation VBD - Real-Time Intelligence Lab Tutorial",
    "datascience": "Fabric Foundation VBD - Data Science Lab Tutorial",
}
SOURCE_DOCX = {
    "lakehouse": "Lakehouse Tutorial.docx",
    "warehouse": "Fabric Data Warehouse Tutorial.docx",
    "rti": "Real-time Intelligence Tutorial.docx",
    "datascience": "Data Science Tutorial.docx",
}

for lab in ["lakehouse", "warehouse", "rti", "datascience"]:
    path = ROOT / lab / f"{lab}-tutorial.md"
    original = path.read_text(encoding="utf-8")

    # Strip any previously-added header block so we don't stack it
    stripped = re.sub(
        r"^# Fabric Foundation VBD.*?(?=^- [A-Z]|\Z)",
        "",
        original,
        count=1,
        flags=re.DOTALL | re.MULTILINE,
    )
    cleaned = clean(stripped)

    # Aggressive trim: find the first TOC bullet or the first real H1 that
    # isn't the pandoc title, whichever comes first. Everything before is junk.
    first_bullet = re.search(r"^- (?:Introduction|Module|Lab|Overview|Getting Started|Exercise)", cleaned, flags=re.MULTILINE)
    first_heading = re.search(r"^# (?:Introduction|Module|Overview|Getting Started|Exercise|Lab)", cleaned, flags=re.MULTILINE)
    candidates = [m.start() for m in (first_bullet, first_heading) if m]
    if candidates:
        cleaned = cleaned[min(candidates):]

    header = (
        f"# {TITLES[lab]}\n\n"
        f"> Converted from `{SOURCE_DOCX[lab]}` (SharePoint IP Release - Fabric Foundation Discovery Labs).\n"
        f"> Screenshots have been stripped; refer to `sources.yaml` in this folder for the Microsoft Learn URLs cited throughout.\n\n"
        f"## Contents\n\n"
    )
    path.write_text(header + cleaned.lstrip(), encoding="utf-8")
    print(f"{lab}: {len(original):,} -> {len(header)+len(cleaned):,} bytes")
