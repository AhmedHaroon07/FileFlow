from flask import Flask, request, jsonify, send_file, render_template_string, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'file_storage'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_INTERFACE = """


<!DOCTYPE html>
<html>
<head>
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='logo.ico') }}">

    <title>File Flow</title>
    

    <style>
        body {
            font-family: 'Roboto Thin', Tahoma, sans-serif;
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 40px;
            background: linear-gradient(135deg, #5e00a1, #1a007a, #0043c1, #00bcd4);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            width: 100%;
            max-width: 1000px;
            display: flex;
            gap: 30px;
            padding: 30px;
            color: white;
        }

        .left-panel, .right-panel {
            flex: 1;
        }

        h1, h3, p, li, label {
            color: white;
        }

        .form-group {
            margin-bottom: 20px;
        }

        input[type="text"], input[type="file"] {
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ccc;
            margin-top: 5px;
        }

        button {
            padding: 10px 20px;
            background: #8e44ad;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
        }

        button:hover {
            background: #732d91;
        }

        ul {
            list-style-type: none;
            padding-left: 0;
        }

        li {
            padding: 5px 0;
        }

        .file-actions {
            background: rgba(255, 255, 255, 0.15);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .file-info {
            font-size: 14px;
            margin-top: 10px;
        }

        .message {
            color: #90ee90;
        }

        .error {
            color: #ff7373;
        }

.page-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.page-title {
    text-align: center;
    font-size: 48px;
    color: white;
    margin-bottom: 30px;
    font-family: "Franklin Gothic Medium";
}


.logo {
    width: 185px; /* adjust size as needed */
    height: auto;
    
}

.title-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px; /* spacing between logo and text */
    margin-bottom: 30px;
}

    </style>
</head>
<body>
    
    <div class="page-wrapper">
    <div class="title-bar">
    <img src= "/static/logo.png" class="logo">
    <h1 class="page-title" >File Flow</h1>
    </div>
    <div class="container">
    
        <!-- LEFT: All files -->
        <div class="left-panel">
            <h3>All Files in Storage</h3>
            {% if files %}
                <ul>
                    {% for file in files %}
                        <li>
                            <form method="post" action="/select_file" style="display:inline;">
                                <input type="hidden" name="file_path" value="{{ file }}">
                                <button type="submit">{{ file }}</button>
                            </form>
                        </li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No files found.</p>
            {% endif %}
        </div>

        <!-- RIGHT: Actions + metadata -->
        <div class="right-panel">
            

            <!-- Upload -->
            <div class="form-group">
                <h3>Upload a File</h3>
                <form action="/upload_file" method="post" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <button type="submit">Upload</button>
                </form>
            </div>

            <!-- Search -->
            <div class="form-group">
                <h3>Search Files</h3>
                <form action="/" method="get">
                    <input type="text" name="q" placeholder="Search file name">
                    <button type="submit">Search</button>
                </form>
            </div>

            {% if selected_file %}
            <div class="file-actions">
                <h3>Selected File: {{ selected_file }}</h3>

                <form action="/rename_file" method="post">
                    <input type="hidden" name="current_path" value="{{ selected_file }}">
                    <input type="text" name="new_name" placeholder="New file name">
                    <button type="submit">Rename</button>
                </form>

                <form action="/delete_file" method="post">
                    <input type="hidden" name="file_path" value="{{ selected_file }}">
                    <button type="submit" style="background-color: #e74c3c;">Delete</button>
                </form>

                <form action="/download_file" method="get">
                    <input type="hidden" name="file_path" value="{{ selected_file }}">
                    <button type="submit">Download</button>
                </form>

                {% if file_info %}
                <div class="file-info">
                    <p><strong>Size:</strong> {{ file_info.size_bytes }} bytes</p>
                    <p><strong>Last Modified:</strong> {{ file_info.last_modified }}</p>
                    <p><strong>Type:</strong> {{ "File" if file_info.is_file else "Directory" }}</p>
                </div>
                {% endif %}
            </div>
            {% endif %}

            {% if message %}<p class="message">{{ message }}</p>{% endif %}
            {% if error %}<p class="error">{{ error }}</p>{% endif %}
        </div>
    </div>
    </div>
</body>
</html>
















"""


def get_file_path(filename):
    return os.path.join(UPLOAD_FOLDER, secure_filename(filename))

#search dala hai main page pr
@app.route('/', methods=['GET'])
def file_manager():
    query = request.args.get('q', '')
    all_files = os.listdir(UPLOAD_FOLDER)
    files = [f for f in all_files if query.lower() in f.lower()] if query else all_files
    return render_template_string(HTML_INTERFACE, files=files)


@app.route('/select_file', methods=['POST'])
def select_file():
    file_path = request.form.get('file_path')
    files = os.listdir(UPLOAD_FOLDER)
    
    if not file_path:
        return render_template_string(HTML_INTERFACE, files=files, error="Please enter a file name")

    full_path = get_file_path(file_path)
    if not os.path.exists(full_path):
        return render_template_string(HTML_INTERFACE, files=files, error="File not found")

    stats = os.stat(full_path)
    info = {
        'filename': file_path,
        'size_bytes': stats.st_size,
        'last_modified': stats.st_mtime,
        'is_file': os.path.isfile(full_path)
    }

    return render_template_string(HTML_INTERFACE, files=files, selected_file=file_path, file_info=info)

@app.route('/rename_file', methods=['POST'])
def rename_file():
    current_path = request.form.get('current_path')
    new_name = request.form.get('new_name')
    files = os.listdir(UPLOAD_FOLDER)

    if not current_path or not new_name:
        return render_template_string(HTML_INTERFACE, files=files, error="Both current path and new name are required")

    old_path = get_file_path(current_path)
    new_path = get_file_path(new_name)

    if not os.path.exists(old_path):
        return render_template_string(HTML_INTERFACE, files=files, error="Original file not found")

    os.rename(old_path, new_path)
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_INTERFACE, files=files, selected_file=new_name, message="File renamed successfully")

@app.route('/delete_file', methods=['POST'])
def delete_file():
    file_path = request.form.get('file_path')
    files = os.listdir(UPLOAD_FOLDER)

    full_path = get_file_path(file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
        files = os.listdir(UPLOAD_FOLDER)
        return render_template_string(HTML_INTERFACE, files=files, message="File deleted successfully")
    return render_template_string(HTML_INTERFACE, files=files, error="File not found")

#upload
@app.route('/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files.get('file')
    files = os.listdir(UPLOAD_FOLDER)

    if not uploaded_file or uploaded_file.filename == '':
        return render_template_string(HTML_INTERFACE, files=files, error="No file selected")

    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(get_file_path(filename))
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_INTERFACE, files=files, message="File uploaded successfully")




@app.route('/download_file', methods=['GET'])
def download_file():
    file_path = request.args.get('file_path')
    full_path = get_file_path(file_path)
    if os.path.exists(full_path):
        return send_file(full_path, as_attachment=True)
    return render_template_string(HTML_INTERFACE, files=os.listdir(UPLOAD_FOLDER), error="File not found")

@app.route('/file_info', methods=['GET'])
def file_info():
    file_path = request.args.get('file_path')
    full_path = get_file_path(file_path)
    files = os.listdir(UPLOAD_FOLDER)

    if os.path.exists(full_path):
        stats = os.stat(full_path)
        info = {
            'filename': file_path,
            'size_bytes': stats.st_size,
            'last_modified': stats.st_mtime,
            'is_file': os.path.isfile(full_path)
        }
        return render_template_string(HTML_INTERFACE, files=files, selected_file=file_path, file_info=info)
    return render_template_string(HTML_INTERFACE, files=files, error="File not found")

if __name__ == '__main__':
    app.run(debug=True)
