## Setup Instructions

### Step 1: Create and activate the Conda environment
```bash
conda create --name neurolens python=3.10
conda activate neurolens
```

### Step 2: Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
pip install -e .
```

## Data for Camera Calibration

### Option 1

Use the data in `data/target/points.json`

### Option 2

- Load images in `data/target/images`
- Use `calibration.ipynb` to sample points and create your own points.json file for calibration


## Run Calibration

``` Python
python calibration/scripts/calibrate.py
```

Checkpoint is saved in `data/logs/lensnet_latest.pth`
