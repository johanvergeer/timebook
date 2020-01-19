import click
from click import Command, Group


@click.group()
def timebook() -> Group:
    pass


@click.command()
def alter() -> Command:
    """ Inserts a note associated with the currently active period in the timesheet.

    usage: `t alter NOTES...`

    aliases: `write`
    """
    pass


@click.command()
def backend() -> Command:
    """Run an interactive database session on the timebook database. Requires the sqlite3 command.

    usage: `t backend`

    aliases: `shell`
    """
    pass


@click.command()
def display() -> Command:
    """Display a given timesheet. If no timesheet is specified, show the current timesheet.

    usage: `t display [TIMESHEET]`

    aliases: `show`
    """
    pass


@click.command(name="format")
def format_() -> Command:
    """Export the current sheet as a comma-separated value format spreadsheet.
    If the final entry is active, it is ignored.

    If a specific timesheet is given, display the same information for that timesheet instead.

    usage: `t format [--start DATE] [--end DATE] [TIMESHEET]`

    aliases: `csv`, `export`
    """
    pass


@click.command(name="in")
def in_() -> Command:
    """  Start the timer for the current timesheet. Must be called before out.
    Notes may be specified for this period. This is exactly equivalent to `t in; t alter NOTES`

    usage: `t in [--switch TIMESHEET] [NOTES...]`

    aliases: `start`
    """
    pass


@click.command()
def kill() -> Command:
    """Delete a timesheet. If no timesheet is specified, delete the current
    timesheet and switch to the default timesheet.

    usage: ``t kill [TIMESHEET]``

    aliases: `delete`
    """
    pass


@click.command(name="list")
def list_() -> Command:
    """List the available timesheets.

    usage: `t list`

    aliases: `ls`
    """
    pass


@click.command()
def now() -> Command:
    """Print the current sheet, whether it's active, and if so, how long it
    has been active and what notes are associated with the current period.

    If a specific timesheet is given, display the same information for that timesheet instead.

    usage: `t now [--simple] [TIMESHEET]`

    aliases: `info`
    """
    pass


@click.command()
def out() -> Command:
    """Stop the timer for the current timesheet. Must be called after in.

    usage: `t out [--verbose] [TIMESHEET]`

    aliases: `stop`
    """
    pass


@click.command()
def running() -> Command:
    """Print all active sheets and any messages associated with them.

    usage: `t running`

    aliases: `active`
    """
    pass


@click.command()
def switch() -> Command:
    """Switch to a new timesheet. this causes all future operation (except switch)
    to operate on that timesheet. The default timesheet is called "default".

    usage: `t switch TIMESHEET`
    """
    pass


timebook.add_command(alter)
timebook.add_command(backend)
timebook.add_command(display)
timebook.add_command(format_)
timebook.add_command(in_)
timebook.add_command(kill)
timebook.add_command(list_)
timebook.add_command(now)
timebook.add_command(out)
timebook.add_command(running)
timebook.add_command(switch)
