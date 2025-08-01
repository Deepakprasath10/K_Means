## Customer Segmentation Web App
   A simple, elegant Flask-based machine learning web app that performs Customer Segmentation using the K-Means Clustering algorithm. Upload your CSV data, choose the number of clusters, and visualize results with ease.
---
## Features
   Upload your own customer dataset (CSV format)

   Choose the number of clusters (K)

   Performs K-Means Clustering using scikit-learn

   View clustered results with assigned labels

   Modern and responsive UI built with HTML & CSS
---
##  Technologies Used
  Component	Tech Stack
  
  Backend	Python, Flask
  
  Machine Learning	Scikit-learn, Pandas, NumPy
  
  Frontend	HTML, CSS (Modern UI)
  
  Deployment	Localhost (Development Server)

## 📁 Project Structure
```
customer-segmentation-flask/
│
├── static/
│   └── style.css                # Custom CSS styles
│
├── templates/
│   ├── index.html               # Upload & input form page
│   └── result.html              # Clustering results page
│
├── uploads/
│   └── (uploaded csv files)    # Temporarily stored uploaded files
│
├── sample_customers.csv        # Sample dataset
├── app.py                      # Main Flask application
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```
---
## Sample Dataset Format
Make sure your dataset contains only numerical features. Column names are optional, but values should be numeric and consistent.
```
Age,Annual_Income,Spending_Score
25,40000,60
32,60000,42
45,85000,30

```
---
## How to Run the App
 Clone the Repository
  git clone https://github.com/Deepakprasath10/K_Means.git
  cd customer-segmentation-flask
  
 Install Requirements
   It’s recommended to use a virtual environment.
   pip install -r requirements.txt

 Run the Flask App
   python app.py
 
 Open in Browser
    Visit: http://127.0.0.1:5000

##  Screenshots
Upload CSV & Choose K	Clustering Result
![alt text](<Screenshot 2025-08-01 152622.png>)
 ![alt text](<Screenshot 2025-08-01 152634.png>)
 ![alt text](<Screenshot 2025-08-01 152656.png>)
 ![alt text](<Screenshot 2025-08-01 152713.png>)

---
 ## Future Improvements
   Visualize clusters on a 2D/3D scatter plot
   
   Download clustered results as a CSV file
   
   Connect to database for persistent storage
   
   Better input validation & error handling
