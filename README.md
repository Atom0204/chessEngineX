# Neural Network Chess Engine ♟️

A basic chess engine powered by a PyTorch neural network, trained on Lichess.org PGNs. The engine evaluates positions and selects moves based on the model’s prediction.

## 🔧 Features

- GUI using `pygame`
- Move animations
- Neural network-based board evaluation
- Training using Lichess PGNs
- Optional GPU acceleration (CUDA)
- Custom evaluation model saved and loaded from `models/`

## 📁 Folder Structure

chessp/
├── data/ # PGN files (e.g., lichess_db_standard_2015-09.pgn)
├── models/ # Trained model (saved as trained_chessnet.pt)
├── src/
│ ├── main.py # Pygame GUI + main loop
│ ├── engine.py # Chess move selection using neural net
│ ├── net.py # PyTorch neural network architecture
│ ├── train.py # PGN training pipeline
│ └── utils.py # PGN parsing and board tensor conversion
├── README.md
└── requirements.txt


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chessp.git


2. Create a Virtual Environment (Optional but Recommended)

3. Install Dependencies
pip install -r requirements.txt

4. Train the Neural Network (Optional)
Download a PGN dataset (e.g., from https://database.lichess.org/)

Place it in the data/ folder (e.g., data/lichess_db_standard_rated_2015-09.pgn)

Start training:

The trained model will be saved in src/models/trained_chessnet.pt

5. Run the Chess GUI

python main.py

Use the graphical interface to play against the neural network engine.