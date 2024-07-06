# Sistem Penunjang Keputusan Kreditur Berbasis AHP

![GitHub repo size](https://img.shields.io/github/repo-size/rickyrsn/uas_spk_ahp)
![GitHub contributors](https://img.shields.io/github/contributors/rickyrsn/uas_spk_ahp)
![GitHub stars](https://img.shields.io/github/stars/rickyrsn/uas_spk_ahp?style=social)
![GitHub forks](https://img.shields.io/github/forks/rickyrsn/uas_spk_ahp?style=social)

## Table of Contents

- [Demo](#demo)
- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

## Demo
Insert demo link or screenshots here.

## About the Project
This project implements an Analytic Hierarchy Process (AHP)-based decision support system for evaluating creditors. It allows users to input various criteria such as business feasibility, economic conditions, character, and collateral to assess and rank creditors based on their suitability.

The system utilizes Flask for the web framework, SQLAlchemy for database management with SQLite, and integrates AHP calculations using the AHPy library.

### Built With

- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/)
- [Bootstrap](https://getbootstrap.com/)

### Installation

```sh
git clone https://github.com/rickyrsn/uas_spk_ahp.git
cd uas_spk_ahp
pip install -r requirements.txt
python app.py

Open a web browser and go to http://localhost:5000.
```

## Usage

1. Input Data:
  - Navigate to the home page.
  - Fill out the form to input creditor details including business feasibility, economic conditions, character, and collateral.
  - Click on "Submit" to save the data.

2. View Results:
  - The system automatically calculates the score based on AHP weights.
  - Results are displayed in a table, sorted by the calculated score.

## Roadmap

- Enhance UI/UX design.
- Implement user authentication and authorization.
- Add export functionalities for reports.
- Integrate more advanced AHP features.

## Contributing

Contributions are welcome! Follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.
