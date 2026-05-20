from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__, static_folder='.', static_url_path='')

BLOG_FILE = 'blog.html'
TARGET_FILES = {
    'blog': 'blog.html',
    'diagnosis': 'energy-diagnosis.html'
}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'b7x2kR9mL.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory('.', filename)

@app.route('/api/save-blog', methods=['POST'])
def save_blog():
    try:
        data = request.get_json()
        html_content = data.get('html')
        target = data.get('target', 'blog')
        target_file = TARGET_FILES.get(target, BLOG_FILE)
        
        if not html_content:
            return jsonify({'success': False, 'error': 'No HTML provided'}), 400
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return jsonify({'success': True, 'message': f'{target_file} updated successfully!'})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    print("Blog server running at http://localhost:5000")
    print("Open http://localhost:5000 to create posts")
    app.run(debug=False, port=5000)
