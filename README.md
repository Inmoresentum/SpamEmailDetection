# CSE422 Lab Project

## PROJECT TITLE: _SPAM EMAIL DETECTION_

### Notebook:

This repository contains the [ipynb/notebook](src/SpamEmailDetction.ipynb) and the [dataset](src/Dataset/emails.csv)
I submitted for the CSE422 Lab project.

### Project Report:

* The report was written in `LaTeX` and it's in a separate repository.
  Click to [this link](https://github.com/Inmoresentum/CSE422ProjectLatexRepository/) which will redirect you there.
* If you are looking for the `PDF/Project` Report then
  click [here](https://github.com/Inmoresentum/CSE422ProjectLatexRepository/blob/master/out/main.pdf)
  which will redirect you to the `main.pdf` file.

## Setup

1. Python

`python` version **3.10.8** or higher. Download [python](https://www.python.org/downloads/) if you don't have it
already.

To check your version of python, run:

   ```shell
    python --version
   ```

- **Note**: Unix like operating systems (`OS X, Linux and BSD`) `python` comes with the operating system itself.
  So, I recommend using any _**virtual environment**_ instead of using the _**system environment**_ which can break
  things easily.
  You can
  use [miniconda](https://docs.conda.io/en/main/miniconda.html), [virtualenv](https://virtualenv.pypa.io/en/latest/)
  or any other environment of your choice.

Once the virtual environment setup is done, install the required dependencies using `requirements.txt` using the
following command. Open your terminal from the project directory

   ```shell
    pip install -r requirements.txt
   ```

## issues

You've found a bug in the source code, a mistake in somewhere?
You can help
by [submitting an issue on GitHub](https://github.com/Inmoresentum/SpamEmailDetection/issues).
Before you create an issue, make sure to search for the issue archive -- your issue may have already been addressed, 
and there maybe a temporary workaround!

Please try to create bug reports that are:

- _Reproducible._ include steps to reproduce the problem.
- _Specific._ include as much detail as possible: which version, what environment, etc.
- _Unique._ do not duplicate existing opened issues.
- _Scoped to a **single bug**._ one bug per report.