import textwrap

import click

from seventh import __version__, wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(
    language: str = "en",  # The language edition of wikipedia
) -> None:  # Just formats the output and returns None
    """The ultramodern Python project."""
    page = wikipedia.random_page(language=language)  # language=language needed here
    # title = data["title"]
    # extract = data["extract"]
    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))


if __name__ == "__main__":
    main()
