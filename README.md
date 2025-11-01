# Sorting Algorithms

A comprehensive collection of sorting algorithm implementations demonstrating various approaches to organizing data efficiently. This repository serves as both a learning resource and reference for understanding different sorting techniques.

## 📖 About

This repository contains implementations of fundamental and advanced sorting algorithms, showcasing their unique approaches, time complexities, and use cases. Each algorithm is implemented with clear, readable code to facilitate learning and comparison.

## 🎯 Purpose

- **Educational Resource**: Learn and understand how different sorting algorithms work
- **Algorithm Comparison**: Compare performance and efficiency across different sorting techniques
- **Interview Preparation**: Reference implementations for common coding interview questions
- **Practical Reference**: Ready-to-use implementations for various projects

## 🔍 Algorithms Implemented

### Elementary Sorting Algorithms
- **Bubble Sort** - Simple comparison-based algorithm with repeated swapping
- **Selection Sort** - Finds minimum element and places it at the beginning
- **Insertion Sort** - Builds sorted array one element at a time

### Efficient Sorting Algorithms
- **Merge Sort** - Divide and conquer approach with guaranteed O(n log n)
- **Quick Sort** - Fast, in-place sorting with partitioning
- **Heap Sort** - Uses binary heap data structure for sorting

### Specialized Sorting Algorithms
- **Counting Sort** - Integer sorting algorithm for limited range
- **Radix Sort** - Non-comparative sorting for integers
- **Bucket Sort** - Distributes elements into buckets

### Other Algorithms
- **Shell Sort** - Generalized insertion sort with gap sequences
- **Cocktail Sort** - Bidirectional bubble sort variant

## 📊 Complexity Comparison

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Stable |
|-----------|-----------|--------------|------------|------------------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | Yes |
| Bucket Sort | O(n + k) | O(n + k) | O(n²) | O(n) | Yes |

*where n = number of elements, k = range of input*

## 🚀 Getting Started

### Prerequisites

- Programming language compiler/interpreter (based on implementation language)
- Basic understanding of data structures and algorithms

### Installation

Clone this repository:
```bash
git clone https://github.com/KodeWithKeshav/Sorting_Algorithms.git
cd Sorting_Algorithms
```

### Usage

Each sorting algorithm can be run independently. Navigate to the specific algorithm file and execute it according to the language used.

Example (assuming Python/C++/Java):
```bash
# Python
python bubble_sort.py

# C++
g++ merge_sort.cpp -o merge_sort
./merge_sort

# Java
javac QuickSort.java
java QuickSort
```

## 💡 Key Concepts

### Stability
A sorting algorithm is **stable** if it maintains the relative order of equal elements.

### In-Place Sorting
An algorithm is **in-place** if it requires only a constant amount O(1) of additional space.

### Comparison-Based vs Non-Comparison
- **Comparison-based**: Compare elements to determine order (most algorithms)
- **Non-comparison**: Use other properties like digit/character position (Counting, Radix, Bucket)

### Adaptive Algorithms
Some algorithms perform better when the input is partially sorted (e.g., Insertion Sort, Bubble Sort).

## 📚 Learning Resources

### When to Use Which Algorithm?

- **Nearly Sorted Data**: Insertion Sort, Bubble Sort
- **Small Datasets**: Insertion Sort, Selection Sort
- **Large Datasets**: Merge Sort, Quick Sort, Heap Sort
- **Memory Constraints**: Heap Sort, Quick Sort (in-place)
- **Stable Sorting Required**: Merge Sort, Counting Sort, Radix Sort
- **Integer Data with Limited Range**: Counting Sort, Radix Sort
- **Guaranteed O(n log n)**: Merge Sort, Heap Sort

## 🛠️ Implementation Details

Each algorithm includes:
- Clear, well-commented code
- Time and space complexity analysis
- Example usage and test cases
- Explanation of the algorithm's approach

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewAlgorithm`)
3. Commit your changes (`git commit -m 'Add new sorting algorithm'`)
4. Push to the branch (`git push origin feature/NewAlgorithm`)
5. Open a Pull Request

### Contribution Guidelines
- Ensure code is well-documented
- Include time and space complexity analysis
- Add test cases for your implementation
- Follow consistent coding style

## 📝 Project Structure

```
Sorting_Algorithms/
├── bubble_sort.*
├── selection_sort.*
├── insertion_sort.*
├── merge_sort.*
├── quick_sort.*
├── heap_sort.*
├── counting_sort.*
├── radix_sort.*
├── bucket_sort.*
└── README.md
```

## 🎓 Learning Outcomes

Through this repository, you'll gain understanding of:
- Different algorithmic paradigms (divide and conquer, greedy, etc.)
- Trade-offs between time and space complexity
- Practical applications of sorting algorithms
- Algorithm optimization techniques
- Performance analysis and benchmarking

## 📬 Contact

**Keshav**
- GitHub: [@KodeWithKeshav](https://github.com/KodeWithKeshav)

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Inspired by classic computer science textbooks and courses
- Built as a learning resource for students and developers
- Thanks to the open-source community for continuous learning

---

⭐ If you find this repository helpful for your learning journey, consider giving it a star!

**Happy Sorting! 🎯**
