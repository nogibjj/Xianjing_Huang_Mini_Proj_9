## Xianjing_Huang_Individual_Project_1
[![Install](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/install.yml)[![Lint](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/lint.yml)[![Format](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/format.yml)[![Test](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Individual_Project_1/actions/workflows/test.yml)

### Youtube Video Link
[Youtube Link](https://youtu.be/ad-qByfXmTE)

### Directory Tree Structure 
```
Xianjing_Huang_Individual_Project_1/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── imgs/
├── .gitignore
├── lib.py
├── Makefile
├── MSFT-stock.csv
├── proj1_notebook.ipynb
├── README.md
├── report.pdf
├── requirements.txt
├── script.py
├── stock_line_chart.png
├── test_lib.py
└── test_script.py
```

### Requirements
* __`Jupyter Notebook`__ with:
  - Cells that perform __descriptive statistics using Polars or Panda__
  - Tested by using __nbval plugin__ for __pytest__
* __`Makefile`__ with the following:
  - Run all tests __(must test notebook and script and lib)__
  - Formats code with __Python Black__
  - Lints code with __Ruff__
  - Installs code via:  __pip install -r requirements.txt__
*	__`test_script.py`__ to test script
*	__`test_lib.py`__ to test library
*	Pinned __`requirements.txt`__
*	__`GitHub Actions`__ performs all four Makefile commands with __badges__ for each one in the `README.md`

### Preparation 
1. Open codespaces 
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed 
3. If running locally, `git clone` the repository and use `make install`
![1](/imgs/001.png)

### Check format and test errors
1. Format code `make format`
![3](/imgs/003.png)
2. Lint code `make lint`
![4](/imgs/004.png)
3. Test code `make test`
![2](/imgs/002.png)

### Descriptive Statistics
![0](/imgs/000.png)

### Visualization
![5](/stock_line_chart.png)

### Report
Generated summary report (PDF) via CI/CD.
You can find it here [Report](/report.pdf)