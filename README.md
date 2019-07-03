# LeadGen(sales-leads)
Automatically searches company names from a source CSV file and returns name, role, linkedin contact information

## Prequisities

  + Anaconda 3.7
  + Python 3.7
  + Pip

fork https://github.com/fbawa/sales-leads repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd sales-leads
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

From inside the virtual environment, install package dependencies:

```sh
pip install selenium
pip install requests
pip install beautifulsoup4
```
## Usage

1. Open sales-leads repository in Visual Basic Studio

2. Create or navigate to the source.csv file in the data folder and enter target company names

3. Run the recommendation script:

```py
python sales.py
```
4. View contact information data in contacts.csv in the data folder



