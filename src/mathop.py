from logging import raiseExceptions
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument("a", type=float, nargs=-1)
def add(a):
    """Needs at least two arguments. Adds them all together."""
    if len(a)<2:
        click.echo("Expected at least 2 inputs.")
        return
    click.echo(sum(a))

@click.command()
@click.argument("a", type=float)
@click.argument("b", type=float, nargs=-1)
def sub(a,b):
    """Needs at least two arguments. Every argument after the first is subtracted from the first."""
    if len(b)<1:
        click.echo("Expected at least 2 inputs.")
        return
    click.echo(a-sum(b))

@click.command()
@click.argument("a", type=float, nargs=-1)
def mult(a):
    """Needs at least two arguments. Multiplies them all together."""
    if len(a)<2:
        click.echo("Expected at least 2 inputs.")
        return
    prod=1
    for i in a:
        prod*=i
    click.echo(prod)

@click.command()
@click.argument("a", type=float)
@click.argument("b", type=float, nargs=-1)
def div(a,b):
    """Needs at least two arguments. Divides every argument after the first from the first."""
    if len(b)<1:
        click.echo("Expected at least 2 inputs.")
        return
    quo=1
    for i in b:
        if i==0:
            click.echo("Can't divide by zero")
            return
        quo/=i
    click.echo(quo*a)

@click.command()
@click.argument('a', type=float, nargs=2)
def mod(a):
    """First argument modulo the second."""
    click.echo(a[0]%a[1])

@click.command()
@click.argument('a', type=float, nargs=2)
def exp(a):
    """First argument raised to the power of the second."""
    click.echo(a[0]**a[1])


cli.add_command(add)
cli.add_command(sub)
cli.add_command(mult)
cli.add_command(div)
cli.add_command(mod)
cli.add_command(exp)
