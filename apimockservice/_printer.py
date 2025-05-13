from rich.console import Console
console = Console()

def print_message(message, style="bold blue", prefix="<APIMock>"):
    console.print(f"[{style}]{prefix} {message}[/{style}]")
