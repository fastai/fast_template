"""Converts Jupyter Notebooks to Jekyll compliant blog posts"""
from datetime import datetime
import re, os, logging
from nbdev import export2html
from nbdev.export2html import Config, Path, _re_digits

# Check for YYYY-MM-DD
_re_blog_date = re.compile(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-)')
# Check for leading dashses or numbers
_re_numdash = re.compile(r'(^[-\d]+)')
warnings = set()

def rename_for_jekyll(nb_path: Path) -> str:
    """
    Return a Path's filename string appended with its modified time in YYYY-MM-DD format.
    """
    assert nb_path.exists(), f'{nb_path} could not be found.'
    
    # Checks if filename is compliant with Jekyll blog posts
    if _re_blog_date.match(nb_path.name): return nb_path.with_suffix('.md').name
    
    else:
        clean_name = _re_numdash.sub('', nb_path.with_suffix('.md').name)

        # Gets the file's last modified time and and append YYYY-MM-DD- to the beginning of the filename
        dtnm = datetime.fromtimestamp(os.path.getmtime(nb_path)).strftime("%Y-%m-%d-") + clean_name
        assert _re_blog_date.match(dtnm), f'{dtnm} is not a valid name, filename must be pre-pended with YYYY-MM-DD-'
        # push this into a set b/c _nb2htmlfname gets called multiple times per conversion
        warnings.add((nb_path, dtnm))
        return dtnm

    
# Modify the naming process such that destination files get named properly for Jekyll _posts
def _nb2htmlfname(nb_path, dest=None): 
    fname = rename_for_jekyll(nb_path)
    if dest is None: dest = Config().doc_path
    return Path(dest)/fname


for original, new in warnings:
    print(f'{original} has been renamed to {new} to be complaint with Jekyll naming conventions.\n')

# TODO: Open a GitHub Issue When there are any warnings
    
## apply monkey patch
export2html._nb2htmlfname = _nb2htmlfname

export2html.notebook2html(fname='_notebooks/*.ipynb', dest='_posts/')
