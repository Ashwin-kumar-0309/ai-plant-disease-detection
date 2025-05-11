# 🌿 AI Plant Disease Detection

This project leverages deep learning to detect plant diseases from leaf images. Utilizing a Convolutional Neural Network (CNN) model, it classifies images into various disease categories, aiding in early detection and management. The application is built with Flask, providing a user-friendly web interface for real-time predictions.


## 🚀 Features

* **Deep Learning Model**: Trained CNN model for accurate disease classification.
* **Web Interface**: Interactive Flask application for image uploads and result display.
* **Modular Codebase**: Organized structure with separate modules for utilities and configurations.
* **Extensible Design**: Easily adaptable for additional plant species and diseases.

## 🗂️ Project Structure

```
ai-plant-disease-detection/
├── plant-disease-app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── class_names.py
│   ├── utils.py
├── AI-plant-disease-detection.ipynb
├── requirements.txt
```

* `plant-disease-app/`: Contains the Flask application components.

  * `templates/index.html`: HTML template for the web interface.
  * `app.py`: Main Flask application script.
  * `class_names.py`: Defines the mapping of class indices to disease names.
  * `utils.py`: Utility functions for image processing and prediction.
* `AI-plant-disease-detection.ipynb`: Jupyter notebook for model training and experimentation.
* `requirements.txt`: Lists the Python dependencies required for the project.

## 🖥️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ashwin-kumar-0309/ai-plant-disease-detection.git
   cd ai-plant-disease-detection/plant-disease-app
   ```

2. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r ../requirements.txt
   ```

## 🚀 Usage

1. **Run the Flask Application**:

   ```bash
   python app.py
   ```

2. **Access the Web Interface**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

3. **Predict Plant Disease**:

   * Upload an image of a plant leaf.
   * Click on the "Predict" button.
   * View the predicted disease class displayed on the page.

## 🧪 Model Training

The `AI-plant-disease-detection.ipynb` notebook provides a comprehensive guide for training the CNN model:

* **Data Loading**: Import and preprocess the dataset.
* **Model Architecture**: Define the CNN structure.
* **Training**: Compile and train the model on the dataset.
* **Evaluation**: Assess the model's performance on validation data.
* **Saving the Model**: Save the trained model for inference in the Flask app.

## 📦 Dependencies

Ensure the following Python packages are installed (listed in `requirements.txt`):

* Flask
* TensorFlow
* NumPy
* Pillow
* OpenCV
* Other dependencies as specified

Install them using:

```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make enhancements, and submit pull requests.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Ashwin-kumar-0309/ai-plant-disease-detection/blob/main/LICENSE) file for details.
