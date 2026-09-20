# DS212 course book

This project uses **Jupyter Book 1 (Sphinx Book Theme)**. The requirements deliberately stay below Jupyter Book 2, which uses a different configuration format.

The book and PyData themes are pinned together to keep the sidebar controls compatible. After changing either version, check the navigation drawer on a phone-sized viewport as well as desktop navigation.

## Build on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\jupyter-book.exe build . --all -W --keep-going
```

Open `_build/html/intro.html`, or serve the generated site locally:

```powershell
.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1 --directory _build/html
```

Then visit <http://127.0.0.1:8000/intro.html>.

## Maintain the appearance and navigation

- `_toc.yml`: reading order, topic groups, and short sidebar labels. Add each exercise under its related lesson. Keep the hierarchy to two levels.
- `_config.yml`: book metadata, theme settings, and extensions.
- `_static/ds212.css`: colors, typography, responsive layout, and dark mode.
- `_static/ds212-mark.svg` and `favicon.svg`: course identity.
- `intro.md`: course homepage and original introduction.
- `course-guide.md`: navigation and study guidance.
- `syllabus.md`: dedicated PDF viewer and download link. The source PDF remains at `files/Syllabus.pdf`; `html_extra_path` also copies it to the output root for the viewer.

Existing notebook lesson content is unchanged. HTML is generated output; make future edits in these source files and rebuild.
