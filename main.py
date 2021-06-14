#%%
import click
from core import google, is_link
from sys import exit

@click.command()
@click.option('--search', '-S', help = 'Open Google Search Results For Entered Text')
@click.option('--website', '-W', help = 'Open Website Directly')

def main(search, website):

    if search is not None:
    
       google(search)

    elif website is not None:

        is_link(website)
    
    else:

        if click.confirm('Would you like to search on Google?'):
           
            google(click.prompt('What would you like to search on Google?'))
            
        
        elif click.confirm('Would you like to open a website?'):

            is_link(click.prompt('What website would you like to go to?'))

        else:

            exit()
            


if __name__ == '__main__':
    main()
# %%
