from mock.mock_service import app
import click
from click_help_colors import HelpColorsGroup, version_option
import webbrowser
import uvicorn
from _printer import print_message
from threading import Timer
from emoji import emojize

__version__ = "1.0.0"
__description__ = "API Mock Service."
__image__ = emojize(fr"""
 █████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔═══██╗████╗ ████║
███████║██║   ██║██╔████╔██║
██╔══██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝         ╚═╝     ╚═╝

                                 {__description__}
                                 version:{__version__}
                                 :sun:  :rainbow: :unicorn:
""")

@click.group(cls=HelpColorsGroup,
             invoke_without_command=True,
             help_headers_color='magenta',
             help_options_color='cyan',
             context_settings={"max_content_width": 120, })
@version_option(version=__version__, prog_name="aomaker", message_color="green")
@click.pass_context
def main(ctx): # ctx为命令上下文
    click.echo(__image__) # 打印
    if ctx.invoked_subcommand is None: # 若不包含子命令，则直接打印help信息
        click.echo(ctx.get_help())

@main.group()
def mock():
    """Aomaker mock server."""
    pass

@mock.command(help="Start the mock server.")
@click.option('--web', is_flag=True, help="Open the API documentation in a browser.")
@click.option('--port', default=9999, help="Specify the port number to run the mock server on. Default is 9999.")
def start(web, port):
    """Start the mock server."""
    from mock.mock_service import app
    docs_url = f"http://127.0.0.1:{port}/api/docs"
    if web:
        Timer(2, open_web, args=[docs_url]).start()
    print_message(f"🚀 启动Mock服务器在端口 {port}")
    print_message(f"📚 API文档地址: {docs_url}")
    uvicorn.run(app, host="127.0.0.1", port=port)

def open_web(url):
    webbrowser.open(url)

if __name__ == '__main__':
    main()