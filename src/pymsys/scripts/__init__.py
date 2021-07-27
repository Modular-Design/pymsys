import click
import uvicorn
from ..server import Server
from ..nodes import ExampleNode

app = Server(ExampleNode)


def launch(module="pymsys.scripts:app", host="127.0.0.1", port=9000):
    uvicorn.run(module, host=host, port=port, log_level="info", reload=True)


@click.group(chain=True, invoke_without_command=True)
@click.pass_context
def pymsys(ctx):
    if ctx.invoked_subcommand is None:
        launch()


@pymsys.command("serve")
@click.option('-m', '--module', default="msys.scripts.msys:server", help='The module to host.')
@click.option('-h', '--host', default="127.0.0.1", help='The host address.', type=str)
@click.option('-p', '--port', default=8000, help='The port address.', type=int)
def serve(module, host, port):
    """launches costom server"""
    launch(module, host, port)


if __name__ == '__main__':
    pymsys()
