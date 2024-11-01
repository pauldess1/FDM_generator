# Match Sheet Application

This application streamlines the management of team match sheets for the French FSGT Championship. It enables users to update player attendance, preview match details, and export a finalized PDF version of the match sheet. With this tool, preparing weekly match sheets becomes faster and more efficient.

## Table of Contents

1. [Visual](#visual)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Requirements](#requirements)
6. [Future Improvements](#future-improvements)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

## Visual

<p align="center">
  <img src="visual/generator.PNG" alt="Attendance manager" width="60%" />
</p>

<p align="center">
  <img src="visual/generated.PNG" alt="Match sheet generated" width="60%" />
</p>

## Features

- View a list of players and their license numbers.
- Change the attendance status of players.
- Preview the match sheet before downloading.
- Generate a PDF match sheet based on the updated information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pauldess1/FDM_generator.git
   cd FDM_generator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py --original_FDM_path team_infos.txt
   ```

## Usage

1. Open the application and load the player data from the `team_infos.txt` file.
2. Modify player attendance by selecting a player and clicking the "Change attendance" button.
3. Preview the match sheet to verify the details.
4. Download the updated match sheet as a PDF.

## Requirements

- Python 3.x
- See `requirements.txt` for the list of required packages.

## Future Improvements

- Ability to see the preview of the pdf in real-time
- Keep the track of players attendance in each match

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF handling.

Feel free to contribute or contact me if you have any questions or need assistance with using the application!
Let me know if you’d like further adjustments!
