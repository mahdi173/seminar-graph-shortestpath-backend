## **Installation**

### Prerequisites
Rensure you have the following installed on your system:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Node.js and npm**: [Download Node.js](https://nodejs.org/)
- **Git**: [Download Git](https://git-scm.com/)

### Steps to Set Up

#### Clone the Repository
```bash
git clone git@github.com:mahdi173/seminar-graph-shortestpath-backend.git
cd seminar-graph-shortestpath-backend
```

#### Set Up the Backend (Flask)
The backend is responsible for processing GeoJSON data, calculating graphs, and determining optimal paths.


1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```
   The backend will now be running at `http://localhost:5000`.


#### Access the Application
- Open your browser and navigate to `http://localhost:8080`.
- Ensure both the backend (`http://localhost:5000`) and frontend are running simultaneously for full functionality.
