# 📊 Variance Calculator

A robust Python application for calculating population variance of test scores with comprehensive input validation and automated testing.

## ✨ Features

- **🎯 Precise Variance Calculation**: Computes population variance using the formula `σ² = Σ((xᵢ - μ)²) / N`
- **🛡️ Input Validation**: Ensures scores are integers between 0-100, with configurable limits
- **🔄 Interactive Input**: User-friendly command-line interface with error handling and retries
- **🧪 Comprehensive Testing**: 14 unit tests covering edge cases, error conditions, and integration scenarios
- **📈 Audit Trail**: Automatic test result logging with timestamped reports
- **📝 Production Logging**: Structured logging with file rotation for observability and debugging
- **🏗️ Modular Architecture**: Clean separation of concerns with reusable functions

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- No external dependencies required

### Installation
```bash
git clone https://github.com/rhoolan/nww_playbox.git
cd nww_playbox
```

### Usage
Run the interactive calculator:
```bash
python variance.py
```

Example interaction:
```
Enter scores separated by commas (e.g. 90, 85, 88): 85,87,88
Score variance: 2.0000
```

## 🏗️ Architecture

### Core Functions

#### `_find_variance(scores: list[int]) -> float`
Calculates population variance with type checking and validation.
- **Input**: List of integers (0-100 range enforced elsewhere)
- **Output**: Population variance as float
- **Raises**: `TypeError` for invalid types, `ValueError` for empty lists

#### `_get_scores_from_user() -> list[int] | None`
Handles user input with validation and error recovery.
- **Features**: Parses comma-separated input, validates ranges, limits count
- **Returns**: Valid score list or `None` on invalid input

#### `find_variance_from_user_input() -> float`
Orchestrates the complete user interaction flow.

### Configuration Constants
- `MAX_SCORE = 100`: Maximum allowed score
- `MAX_SCORE_COUNT = 3`: Maximum number of scores per calculation

## 🧪 Testing

### Run Tests
```bash
python -m unittest test_variance.py -v
```

### Automated Test Reporting
```bash
python update_test_readme.py
```
Generates timestamped reports in `test_results/` directory.

### Test Coverage
- ✅ Normal variance calculations
- ✅ Edge cases (single score, identical scores)
- ✅ Error handling (empty lists, wrong types, invalid ranges)
- ✅ User input validation and retry logic
- ✅ Integration testing

## 📝 Logging

### Log Configuration
The application uses Python's built-in logging module with structured output and file rotation:
- **Log Level**: INFO and above (INFO, WARNING, ERROR, CRITICAL)
- **File Location**: `logs/variance_calculator.log`
- **Rotation**: Automatic rotation at 10MB with 5 backup files
- **Format**: Timestamp, log level, module, function, and message

### Log Levels Used
- **INFO**: Successful operations and key application events
- **WARNING**: Non-critical issues that don't stop execution
- **ERROR**: Errors that prevent normal operation
- **CRITICAL**: Severe errors requiring immediate attention

### Viewing Logs
```bash
# View recent log entries
tail -f logs/variance_calculator.log

# View all log files (including rotated ones)
ls -la logs/

# Search for specific log entries
grep "ERROR" logs/variance_calculator.log
```

### Log Examples
```
2024-01-15 10:30:15,123 - INFO - variance - _find_variance - Starting variance calculation for 3 scores
2024-01-15 10:30:15,124 - INFO - variance - _find_variance - Variance calculated successfully: 2.0000
2024-01-15 10:30:16,001 - WARNING - variance - _get_scores_from_user - Invalid input format, retrying...
2024-01-15 10:30:16,002 - ERROR - variance - find_variance_from_user_input - Failed to get valid scores after retries
```

## 📊 Example Calculations

| Scores | Mean | Variance | Interpretation |
|--------|------|----------|----------------|
| [85, 87, 88] | 86.67 | 2.00 | Low variance - consistent performance |
| [50, 70, 85, 95, 100] | 80.00 | 300.00 | High variance - wide performance range |
| [90, 90, 90] | 90.00 | 0.00 | No variance - identical scores |

## 🎯 Use Cases

### Education
- **Assessment Analysis**: Evaluate test consistency and fairness
- **Student Performance**: Identify outliers and learning gaps
- **Grade Distribution**: Understand score spread in classrooms

### Quality Control
- **Process Monitoring**: Measure consistency in manufacturing
- **Performance Metrics**: Analyze system reliability
- **Data Validation**: Ensure measurement accuracy

### Research
- **Statistical Analysis**: Foundation for more complex statistical measures
- **Data Quality**: Detect anomalies in datasets
- **Comparative Studies**: Benchmark performance across groups

## 📁 Project Structure

```
nww_playbox/
├── variance.py              # Main application
├── test_variance.py         # Unit test suite
├── update_test_readme.py    # Test automation script
├── logs/                    # Application log files
│   └── variance_calculator.log  # Main log file (rotating)
├── test_results/            # Audit trail directory
│   └── test_results_*.md    # Timestamped test reports
├── README.md               # This file
└── __pycache__/           # Python bytecode
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`python update_test_readme.py`)
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

## 🔗 Links

- **Repository**: [GitHub](https://github.com/rhoolan/nww_playbox)
- **Issues**: [Report Bugs](https://github.com/rhoolan/nww_playbox/issues)
- **Discussions**: [Q&A](https://github.com/rhoolan/nww_playbox/discussions)

---

*Built with ❤️ for educational and analytical purposes*