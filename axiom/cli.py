import click
from axiom import __version__

@click.group()
@click.version_option(__version__)
def cli():
    """Axiom deployment platform."""

@cli.command()
def deploy():
    """Deploy to production."""
    click.echo("Deploying...")

@cli.command()
def status():
    """Show deployment status."""
    click.echo("Status: OK")
