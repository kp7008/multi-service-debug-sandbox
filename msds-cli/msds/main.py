import click

@click.group()
def cli():
    pass

@cli.group()
def sandbox():
    pass

@sandbox.command()
def up():
    click.echo("🚀 Sandbox running")

@sandbox.command()
def down():
    click.echo("🛑 Sandbox stopped")

if __name__ == '__main__':
    cli()