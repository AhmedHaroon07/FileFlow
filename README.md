<h1>📁 FileFlow</h1>
FileFlow is a lightweight file management API with a minimalistic web interface, enabling seamless file operations such as upload, search, download, rename, delete, and info retrieval. It’s perfect for developers who need a simple way to interact with server-side files through both browser and API.

<h2>✨ Features</h2>

🔍 Search files by name

⬆️ Upload files through the web interface

📥 Download files

📝 Rename existing files

🗑️ Delete unwanted files

ℹ️ Get file metadata

🖥️ Simple, modern UI with gradient theme

✅ RESTful API integration ready

🚀 Getting Started


<i>Prerequisites</i><br>
<li>Python 3.7+</li>
<li>Flask</li>
<br><br>
<i>Installation</i>

git clone https://github.com/yourusername/fileflow.git<br>
cd fileflow<br>
pip install -r requirements.txt<br>

<i>Running the Application</i><br>
python app.py



### 📬 API Endpoints

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | `/`            | Web UI with search  |
| POST   | `/upload_file` | Upload a file       |
| POST   | `/select_file` | Select file by name |
| POST   | `/rename_file` | Rename a file       |
| POST   | `/delete_file` | Delete a file       |
| GET    | `/download_file` | Download file    |
| GET    | `/file_info`   | Get file metadata   |

