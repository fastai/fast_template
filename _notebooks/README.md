# Automatically Convert Jupyter Notebooks To Blog Posts

`fast_template` will **automatically convert [Jupyter](https://jupyter.org/) Notebooks saved into this directory as blog posts!**.  In addition to automatic conversion, there are some additional benefits that `rast_template` provides:

- Preserves the interactivity of charts and graphs from visualization libraries like [Altair](https://altair-viz.github.io/).  
- Allows you to use features of [nbdev](https://nbdev.fast.ai/) to customize blog posts, such as:
    - Hiding cells by placing the comment `#hide` at the top of any cell.  (To hide only the input to a cell use the hide input [jupyter extension](https://github.com/ipython-contrib/jupyter_contrib_nbextensions))

    - Add jekyll warnings, important or note banners with appropriate block quotes by calling [add_jekyll_notes](https://nbdev.fast.ai/export2html/#add_jekyll_notes).

    - Displaying formatted documentation for classes, functions, and enums by calling [show_doc](https://nbdev.fast.ai/showdoc/#show_doc).

    - Define the Title, Summary and other metadata for your blog post via a special markdown cell at the beginning of your notebook.  See the [Usage](#Usage) setion below for more details.

    - There are many more applicable features of nbdev, which is under active development.  Check the [nbdev docs](https://nbdev.fast.ai/), particulary the [export2html](https://nbdev.fast.ai/export2html/) section, for a complete list of features that may be useful.
- Notebooks are exported to HTML in a lightweight manner to allow you to customize CSS and styling.  CSS can optionally be modified in [/assets/main.scss](/assets/main.scss).

## Setup

Follow [these instructions](https://www.fast.ai/2020/01/16/fast_template/), which walks you through setting up `fast_template` on [GitHub](https://github.com/fastai/fast_template/generate).

## Usage
 
1. Create a Jupyter Notebook with the contents of your blog post.
2. Create a markdown cell at the beginning of your notebook with the following contents: 

    ```
    # Title
    > Awesome summary
    - toc: False
    - metadata_key1: metadata_value1
    - metadata_key2: metadata_value2 
    ```
    - Replace `Title`, with your desired title, and `Awesome summary` with your desired summary. 
    - `fast_template` will automatically generate a table of contents for you based on [markdown headers](https://guides.github.com/features/mastering-markdown/)!  You can toggle this feature on or off by setting `toc:` to either `True` or `False`.
    - **Additional metadata is optional** and allows you to set additional [front matter](https://jekyllrb.com/docs/front-matter/).



3. Save your notebook with the naming convention `YYYY-MM-DD-*.ipynb` into the `/_notebooks` folder of this repo.  For example `_/notebooks/2020-01-28-My-First-Post.ipynb`.  This [naming convention is required by Jekyll](https://jekyllrb.com/docs/posts/) to render your blog post.
    - If you fail to name your file correctly, `fast_template` will automatically attempt to fix the problem by prepending the last modified date of your notebook to your generated blog post in `_posts`, however, it is recommended that you name your files properly yourself for more transperency.

4. [Commit and push](https://help.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line) your notebook to GitHub.  **Important: At least one of your commit messages prior to pushing your notebook(s) must contain the word `/sync` in order to trigger automatic notebook conversion.**  Furthermore, automatic conversion only occurs when a **push is made to the master branch**.  
    - The requirement of the `/sync` keyword is designed to alleviate instances of the unwanted local conflicts that require you to constanly pull to refresh the local copy of your repo. When a notebook is converted to a blog post, a new file is committed automatically. See [How Does it Work?](#How-Does-it-Work) for more details and with instructions on customizing this behavior.


## How Does it Work?

The Jupyter to blog post conversion process is powered by [nbdev](https://github.com/fastai/nbdev), which has [utilities to convert notebooks to webpages](https://nbdev.fast.ai/export2html/), including integrations with [GitHub Pages](https://pages.github.com/), such as [jekyll notes](https://nbdev.fast.ai/export2html/#add_jekyll_notes).  

A [GitHub Action](https://github.com/features/actions) calls `nbdev` when changes to files are detected in the `/_notebooks` directory of your repo and converts Jupyter notebook files into blog posts.  These blog posts are placed into the `/_posts` directory (via a commit and push) which used by GitHub Pages to render your blog posts.  This GitHub Action an be customized by modifying the [/.github/workflows/nb2post.yaml](/.github/workflows/nb2post.yaml) in your repo.

TODO: talk about yaml