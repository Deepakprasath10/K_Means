## Customer Segmentation Web App
    A Flask-based web application that performs customer segmentation using K-Means Clustering. Users can upload a CSV file containing customer data, specify the number of clusters, and view the clustering results in an interactive format.

## Features
    Upload your own customer dataset (CSV)

    Choose the number of clusters (K)

    Perform K-Means Clustering using scikit-learn
    View clustered results with cluster labels

    Beautiful and responsive UI (HTML/CSS)

    Powered by Flask and Python

## Technologies Used
    Component	Tech Stack
    Backend	Python, Flask
    Machine Learning	Scikit-learn, Pandas, NumPy
    Frontend	HTML, CSS (modern UI)
    Deployment	Localhost (development server)

## 📂Project Structure
```
customer-segmentation-flask/
│
├── static/
│   └── style.css                # Custom CSS styles
│
├── templates/
│   ├── index.html               # Upload & input form page
│   └── result.html              # Results display page
│
├── uploads/
│   └── (uploaded csv files)    # Temporary file storage
│
├── app.py                      # Flask application code
├── requirements.txt            # Python dependencies
└── sample_customers.csv        # Sample dataset for testing
```
## Sample Dataset Format
To use this app, your CSV should contain numerical features only.
    Age,Annual_Income,Spending_Score
    25,40000,60
    32,60000,42
    45,85000,30

Column names are optional, but make sure the data has consistent numeric format.

## ⚙️ How to Run the App
Clone the Repository

        git clone https://github.com/Deepakprasath10/K_Means.git
        cd customer-segmentation-flask
        Install Required Libraries
        (It’s recommended to use a virtual environment)
        pip install -r requirements.txt
        Run the Flask App
        python app.py
        Open in Browser
        Visit: http://127.0.0.1:5000

 ## Screenshots
 ![alt text](<Screenshot 2025-08-01 152622.png>)
 ![alt text](<Screenshot 2025-08-01 152634.png>)
 ![alt text](<Screenshot 2025-08-01 152656.png>)
 ![alt text](<Screenshot 2025-08-01 152713.png>)

## Future Improvements
Visualize clusters on a 2D or 3D plot

Export clustered results as downloadable CSV

Integration with database for historical records

Input validation and error handling