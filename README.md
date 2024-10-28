# Match Sheet Application

This application allows users to manage match sheets for a team. Users can modify player attendance, preview the match sheet, and download a PDF version of the completed form.

## Features

- View a list of players and their license numbers.
- Change the attendance status of players.
- Preview the match sheet before downloading.
- Generate a PDF match sheet based on the updated information.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Open the application and load the player data from the `infos.txt` file.
2. Modify player attendance by selecting a player and clicking the "Change attendance" button.
3. Preview the match sheet to verify the details.
4. Download the updated match sheet as a PDF.

## Requirements

- Python 3.x
- See `requirements.txt` for the list of required packages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF handling.
