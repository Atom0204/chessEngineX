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

shell
Copy
Edit

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
2. Train the Model (Optional)
Place PGN files in the data/ folder.

bash
Copy
Edit
cd src
python train.py
3. Run the Chess GUI
bash
Copy
Edit
cd src
python main.py
🧠 Training Info
Model: 5-layer feedforward network

Input: Flattened tensor of chess board (773 floats)

Output: Score between -1 (loss) to +1 (win)

Loss: MSELoss

Optimizer: Adam

You can adjust the training settings (games, epochs, learning rate) in train.py.

🖥️ GPU Support
Make sure CUDA is installed and PyTorch is GPU-enabled:

bash
Copy
Edit
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Check if GPU is used:

python
Copy
Edit
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))