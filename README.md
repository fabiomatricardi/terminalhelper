# 📖 Wiki-Help CLI

A lightweight, terminal-based documentation viewer that **dynamically generates an interactive menu** from external `.md` and `.txt` files. Built with Python and `Rich`, it renders beautifully formatted cheat sheets, API references, and guides directly in your terminal.

Designed for easy distribution via PyInstaller while keeping the `documentation/` folder **external and instantly updatable** without recompiling.

---

## ✨ Features

- 🔍 **Auto-Discovery**: Scans a `documentation/` directory and builds the menu dynamically on startup.
- 🎨 **Rich Terminal UI**: Colorful panels, markdown rendering, and interactive input prompts.
- 📦 **External Data Folder**: Keep documentation separate from the executable. Add, edit, or remove files anytime.
- 🐍 **PyInstaller Ready**: Compiles to a single `.exe` while correctly resolving external paths.
- 📝 **Flexible Format**: Supports `.md` (rendered as Markdown) and `.txt` (plain text). First line = menu title.
- ⚡ **Zero Escape Headaches**: All docs live in external files, completely avoiding Python string escaping warnings/errors.

---

## 📁 Project Structure

```
wiki-help/
├── wiki-help.py              # Main application script
├── requirements.txt          # Python dependencies
└── documentation/            # External folder for your docs (keep this outside the .exe)
    ├── 01-ipython.md
    ├── 02-llamaserver.md
    └── 03-github-cheatsheet.txt
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
# or
pip install rich
```

### 2. Run the App
```bash
python wiki-help.py
```

### 3. Add Documentation
Place `.md` or `.txt` files in the `documentation/` folder. Restart the app to see them appear in the menu.

---

## 🧠 How It Works

The app follows a **data-driven architecture**: instead of hardcoding strings inside Python, it treats the `documentation/` folder as its source of truth. This eliminates escape-sequence bugs, simplifies maintenance, and enables live updates.

### 🔑 Key Functions Explained

| Function | Purpose | Key Details |
|----------|---------|-------------|
| `get_base_path()` | Resolves the correct working directory | Uses `sys.executable.parent` when compiled (`--onefile`) so it points to the actual `.exe` location, not PyInstaller's temp extraction folder. Falls back to `Path(__file__).parent` during development. |
| `load_documents(doc_dir)` | Scans & parses documentation files | Finds all `.md`/`.txt` files, reads the first line as the menu title, handles read errors gracefully, and sorts results alphabetically for a predictable menu order. |
| `main()` | Interactive CLI loop | Displays the dynamic menu, validates user input, reads the selected file, strips the duplicate title line, and renders content using `rich.markdown.Markdown` (for `.md`) or plain text (for `.txt`). |

### 🔄 Execution Flow
1. App starts → calls `get_base_path()` → locates `documentation/` relative to the executable/script.
2. `load_documents()` scans the folder, extracts titles, and returns a sorted list of `(path, title)` tuples.
3. `main()` enters a `while True` loop, prints a Rich panel menu, and waits for input.
4. On valid selection, it reads the file, removes the first-line title (to avoid duplication), and renders it.
5. Loop continues until `0` is entered or the window is closed.

---

## 📦 Building a Standalone Executable (PyInstaller)

Since the `documentation/` folder is **external by design**, you do **NOT** need `--add-data`.

```bash
pip install pyinstaller
pyinstaller --onefile --console --name "WikiHelp" wiki-help.py
```

### 📤 Deployment Structure
Distribute the compiled executable alongside the documentation folder:
```
WikiHelp_App/
├── WikiHelp.exe          ← Standalone executable
└── documentation/        ← ← Users can update this anytime
    ├── ipython.md
    └── ...
```
✅ Changes to `documentation/` are reflected immediately on the next run. No rebuild required.

---

## 📝 Documentation Format Guidelines

Each file in `documentation/` should follow this simple rule:

```text
This First Line Becomes The Menu Label

# Actual Content Starts Here
Your markdown or plain text goes here...
- Lists work fine
- **Bold** and *italic* render beautifully in .md files
- Tables, code blocks, and links are fully supported
```

### Supported Extensions
| Extension | Rendering | Notes |
|-----------|-----------|-------|
| `.md` | 🎨 Rich Markdown | Full table, list, code, and link support |
| `.txt` | 📄 Plain Text | Preserves formatting exactly as written |

> 💡 **Tip**: Prefix filenames with numbers (`01-`, `02-`, etc.) if you want alphabetical sorting to match your intended order.

---

## 🛠️ Customization & Extensions

- **Change UI Colors**: Modify Rich markup tags like `[green]`, `[bold cyan]`, etc.
- **Add Search/Filter**: Extend `load_documents()` to support fuzzy matching or keyword search.
- **CLI Arguments**: Add `argparse` to accept `--docs-dir "custom/path"` for portable deployments.
- **Auto-Refresh**: Use `watchdog` to restart the menu when files in `documentation/` change.

---

## 📄 License

MIT License. Feel free to use, modify, and distribute. See `LICENSE` for details.

---

> 🙌 Built with ❤️ using Python & [Rich](https://github.com/Textualize/rich).  
> Report bugs or suggest features in the [Issues](../../issues) tab.


### 📦 Bonus: `requirements.txt`
Create this in your repo root:
```txt
rich>=13.0.0
```
