<img src="/static/logo.png" width="196" align="left"/>

<h1>FileFlow</h1>
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


### 🔧 Prerequisites
- Python 3.7+
- Flask

### 🚀 Installation

```bash
git clone https://github.com/yourusername/fileflow.git
cd fileflow
pip install -r requirements.txt
```


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

