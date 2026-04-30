# Motion Detection

A robust motion detection system that processes video streams or images to identify and track motion in real-time.

## Features

- Real-time motion detection from video feeds or image sequences
- Multi-frame analysis for accurate motion identification
- Configurable sensitivity settings
- Support for various video formats
- Efficient processing pipeline
- Visual output with motion indicators

## Getting Started

### Prerequisites

- Python 3.7+
- OpenCV
- NumPy
- Additional dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Nikhildhankar/Motion-Detection.git
cd Motion-Detection
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

```bash
python motion_detection.py --input <video_file_or_camera> --output <output_path>
```

**Options:**
- `--input`: Path to video file or camera index (default: 0 for webcam)
- `--output`: Path to save processed video
- `--sensitivity`: Adjust motion detection sensitivity (0-100)
- `--threshold`: Motion detection threshold value

## Project Structure

```
Motion-Detection/
├── motion_detection.py    # Main detection script
├── utils/                 # Utility functions
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

The motion detection system uses frame differencing and background subtraction techniques to:
1. Capture consecutive frames from the input source
2. Compare frames to identify pixel-level changes
3. Apply morphological operations to reduce noise
4. Generate motion masks and contours
5. Visualize detected motion regions

## Configuration

Adjust detection parameters in the configuration section:
- **Frame skip rate**: Process every nth frame for performance
- **Blur factor**: Smoothing for noise reduction
- **Threshold**: Sensitivity to motion detection
- **Min contour area**: Minimum motion region size to detect

## Performance

- Optimized for real-time processing
- Supports GPU acceleration (when available)
- Configurable frame rates and resolution

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Nikhil Dhankar**

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Last Updated:** April 30, 2026
