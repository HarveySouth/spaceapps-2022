import spacepy
import spacepy.toolbox

def download_data():
    """Use spacepy to update all data sources
    
    By default this will add data to ~/.spacepy/data
    
    See https://spacepy.github.io/configuration.html
    """
    spacepy.toolbox.update(all=True)

