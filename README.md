
# CSV_Detector

`CSV_Detector` is a tool designed for parsing and querying large CSV files. It provides a interface that allows users to load, sort, filter, and query specific rows of CSV data efficiently. The primary purpose of this program is to help users efficiently parse and analyze complex datasets stored in CSV format, especially files with numerous columns, such as various scores and metadata. Through this tool, users can quickly sort data by specific columns, filter within score ranges, and retrieve details of specific rows.

## Installation

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/weizart/CSV_Detector
cd CSV_Detector
```

### 2. Set Up a Virtual Environment
It’s recommended to use a virtual environment to keep dependencies isolated:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Environment
This project is compatible with Python 3.7 and above. It leverages `pandas` for data manipulation and `streamlit` for creating the web interface.

## Dependencies
The main dependencies for `CSV_Detector` include:
- `pandas`: for data handling and manipulation
- `streamlit`: for building the interactive user interface

All dependencies are listed in `requirements.txt` and can be installed using `pip`.

## Usage

1. **Start the Application**:
   Run the Streamlit application by executing:
   ```bash
   streamlit run app.py
   ```

2. **Load a CSV File**:
   - Upload your CSV file containing columns such as `path`, `id`, `num_frames`, `score_aes`, `score_flow`, etc.

3. **Sorting and Filtering**:
   - Sort data by columns like `score_aes`, `score_flow`, and filter within score ranges.

4. **Row Query**:
   - Enter a row index to view specific details like `path`, `text`, `height`, `width`, and `fps`.

### Example
To test the application, you can use a sample CSV file structured as follows:

```csv
path,id,relpath,num_frames,height,width,aspect_ratio,fps,resolution,score_aes,text,score_flow,face_id_consistency,face_confidence,face_area_ratio,face_bbox_w,face_bbox_h,face_similarity,face_image_path,face_ref_image_path
/sample/path,1,/sample/relpath,10,720,1280,1.78,30,HD,7.8,"Sample text",5.2,1.0,0.9,0.5,100,200,0.95,/sample/face/path,/sample/ref/path
...
```

## License
This project is licensed under the MIT License.
