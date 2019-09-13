import click

from clients.services import ClientService
from clients.models import ClientModel

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help= 'The clients name')
@click.option('-c', '--company',
                type=str,
                prompt=True,
                help= 'The clients name')
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help= 'The clients name')
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help= 'The clients name')
@click.pass_context
def create(ctx, name, company, email, position):
    """creates a new client"""
    client = client(name,company, email, position)
    client.services = ClientService(ctx)


@click.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete a client"""
    pass


all = clients
