# 🖼️ SVD-Based Image Compression

This project implements **image compression** using the **Singular Value Decomposition (SVD)** technique, reducing image size while preserving visual quality. The method decomposes an image matrix and reconstructs it using a reduced number of singular values.

## 📌 Features

- **Lossy Image Compression**: Reduces image size while keeping visual similarity.
- **Adjustable Compression**: Users can choose different ranks (`r=5, 20, 100`) for varying levels of quality.
- **Grayscale Conversion**: Converts RGB images to grayscale before applying SVD.
- **Visualization**: Displays original and compressed images side by side.

## 📂 Project Structure
 
    SVD_ImageCompression/
    ├── Compression Project/
    │   ├── compression.py                 # Python script for performing SVD compression
    │   ├── t_R=5.PNG                      # Compressed image with r=5
    │   ├── t_R=20.PNG                     # Compressed image with r=20
    │   ├── t_R=100.PNG                    # Compressed image with r=100
    │   ├── Toyota_FJ_Cruiser.jpg          # Original image
    │   ├── Toyota_FJ_Cruiser_- Compressed.PNG  # Final compressed version
    │   ├── requirements.txt              
    ├── README.md                           

## 🚀 Installation & Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/salvabehnam/SVD_ImageCompression.git
    cd "SVD_ImageCompression/Compression Project"
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Compression Script**

    ```bash
    python compression.py
    ```

    - The script reads `Toyota_FJ_Cruiser.jpg`, converts it to grayscale, and applies SVD with ranks `r=5, 20, 100`.
    - The compressed images are displayed and saved.

## 🖼️ Compression Results

### 🔷 Low Compression (`r=5`)
![r=5](Compression%20Project/t_R=5.PNG)

### 🔷 Medium Compression (`r=20`)
![r=20](Compression%20Project/t_R=20.PNG)

### 🔷 High Compression (`r=100`)
![r=100](Compression%20Project/t_R=100.PNG)

### 🔷 Original vs Compressed
![Original](Compression%20Project/Toyota_FJ_Cruiser.jpg)

![Compressed](Compression%20Project/Toyota_FJ_Cruiser_-%20Compressed.PNG)

## ✨ Technologies Used

- Python
- NumPy (for SVD computation)
- Matplotlib (for image visualization)

## 🔧 Requirements

```plaintext
matplotlib
numpy
