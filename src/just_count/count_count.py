from just_count.square import square
import click

@click.command()
@click.argument("number",type=int)


def main(number): 
    print(f"The square of {number} is {square(number)}")
