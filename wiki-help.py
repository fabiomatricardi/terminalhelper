import sys
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def get_base_path() -> Path:
    """Return directory containing the script or executable."""
    if getattr(sys, "frozen", False):
        # PyInstaller --onefile: points to the actual .exe location
        return Path(sys.executable).parent
    else:
        # Running as script: points to the .py file location
        return Path(__file__).parent

def load_documents(doc_dir: Path) -> list[tuple[Path, str]]:
    """Scan folder for .md/.txt files and extract first line as title."""
    docs = []
    if not doc_dir.exists():
        console.print(f"[bold yellow]⚠️ 'documentation' folder not found at:[/bold yellow] {doc_dir}")
        console.print("[dim]Create it next to the executable and add .md or .txt files.[/dim]")
        return docs

    files = sorted(doc_dir.glob("*.md")) + sorted(doc_dir.glob("*.txt"))
    
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                title = first_line if first_line else file_path.stem
                docs.append((file_path, title))
        except Exception as e:
            console.print(f"[yellow]⚠️ Skipping {file_path.name}: {e}[/yellow]")

    docs.sort(key=lambda x: x[1].lower())
    return docs

def main() -> None:
    doc_dir = get_base_path() / "documentation"
    docs = load_documents(doc_dir)

    if not docs:
        console.print("\n[bold red]📄 No documents found. Exiting.[/bold red]")
        sys.exit(1)

    while True:
        console.print(Panel("[bold cyan]📖 Documentation Helper[/bold cyan]", expand=False))
        console.print("\n[bold]Available documents:[/bold]")
        
        for i, (_, title) in enumerate(docs, start=1):
            console.print(f"  [green]{i}.[/green] {title}")
        console.print(f"  [red]0.[/red] Exit\n")

        choice = console.input("👉 Select a number: ").strip()

        if choice == "0":
            console.print("[bold yellow]👋 Goodbye![/bold yellow]")
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(docs):
                file_path, title = docs[idx]
                content = file_path.read_text(encoding="utf-8")
                
                # Remove duplicate title line if it matches the menu label
                lines = content.splitlines()
                if lines and lines[0].strip() == title:
                    lines.pop(0)
                    content = "\n".join(lines)

                console.print(f"\n[bold underline]{title}[/bold underline]\n")
                console.print(Markdown(content) if file_path.suffix == ".md" else content)
                console.print("\n" + "─" * 50 + "\n")
            else:
                console.print("[bold red]❌ Number out of range. Try again.[/bold red]")
        except ValueError:
            console.print("[bold red]❌ Please enter a valid number.[/bold red]")

if __name__ == "__main__":
    main()