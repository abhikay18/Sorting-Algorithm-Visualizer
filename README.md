
# 🔄 Sorting Algorithm Visualizer

A comprehensive and interactive web application built with **Streamlit** and **Python** that visualizes various sorting algorithms in real-time. This educational tool helps users understand how different sorting algorithms work by providing step-by-step visual representations with customizable parameters.

---

## 🚀 Live Demo

[Try the Application]([https://your-live-demo-link.com](https://abhikay18-sorting-algorithm-visualizer-app-gozvxo.streamlit.app/)) <!-- Replace with actual live link if deployed -->

---

## ✨ Features

- **Interactive Visualization**: Real-time step-by-step visualization of sorting processes  
- **Multiple Algorithms**: Support for 5 different sorting algorithms  
- **Customizable Parameters**: Adjustable array size and animation speed  
- **Custom Input**: Add your own arrays for sorting  
- **Color-coded Elements**: Visual distinction between comparing and swapping elements  
- **Progress Tracking**: Real-time progress bar and step counter  
- **Responsive Design**: Works seamlessly on desktop and mobile devices  

---

## 🎯 Supported Sorting Algorithms

| Algorithm       | Best Time     | Average Time  | Worst Time    | Space        |
|----------------|---------------|---------------|---------------|--------------|
| Bubble Sort     | O(n)          | O(n²)         | O(n²)         | O(1)         |
| Insertion Sort  | O(n)          | O(n²)         | O(n²)         | O(1)         |
| Selection Sort  | O(n²)         | O(n²)         | O(n²)         | O(1)         |
| Merge Sort      | O(n log n)    | O(n log n)    | O(n log n)    | O(n)         |
| Quick Sort      | O(n log n)    | O(n log n)    | O(n²)         | O(log n)     |

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Visualization**: Matplotlib  
- **Data Processing**: NumPy  

---

## 📁 Project Structure

```
sorting_visualizer/
├── app.py                 # Main Streamlit application
├── sorting_algorithms.py  # Sorting algorithm implementations
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher  
- `pip` package manager  

### Installation

```bash
git clone https://github.com/yourusername/sorting-algorithm-visualizer.git
cd sorting-algorithm-visualizer
pip install -r requirements.txt
streamlit run app.py
```

### Open your browser

Navigate to [http://localhost:8501](http://localhost:8501) to view the application

---

## 📖 How to Use

1. **Select Algorithm**: Choose from the dropdown menu in the sidebar  
2. **Adjust Parameters**:
   - Set array size (10–100 elements)
   - Control animation speed (10–500ms)
3. **Generate Array**: Click "Generate New Array" for random data  
4. **Custom Input**: Enter your own numbers separated by commas  
5. **Start Sorting**: Click the "Start" button to begin visualization  
6. **Watch & Learn**: Observe the process with color-coded bars and progress indicators  

---

## 🎨 Visual Elements

- 🔵 **Blue Bars**: Normal array elements  
- 🔴 **Red Bars**: Elements being compared  
- 🟠 **Orange Bars**: Elements being swapped  
- 📊 **Progress Bar**: Shows sorting completion percentage  
- 🧮 **Step Counter**: Displays current step number  

---

## 🔧 Configuration

### Array Size  
- Minimum: 10 elements  
- Maximum: 100 elements  
- Default: 50 elements  

### Animation Speed  
- Fastest: 10ms  
- Slowest: 500ms  
- Default: 100ms  

---

## 📊 Algorithm Details

- **Bubble Sort**: Compares and swaps adjacent elements if they’re in the wrong order  
- **Insertion Sort**: Builds the sorted array by inserting each element into its correct position  
- **Selection Sort**: Finds and moves the minimum element to its correct position iteratively  
- **Merge Sort**: Recursively divides and merges sorted halves  
- **Quick Sort**: Partitions around a pivot and recursively sorts subarrays  

---

## 🤝 Contributing

Contributions are welcome!  

```bash
# Steps
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Streamlit team for the amazing framework  
- Matplotlib for powerful visualization capabilities  
- NumPy for efficient array operations  
- Educational resources that inspired this project  

---

