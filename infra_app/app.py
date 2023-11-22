from flask import Flask, request, render_template
from . import app
from . import backend
from dotenv import load_dotenv
import os

load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            environment = request.form.get('environment')
            region = request.form.get('region')
            bucket_name = request.form.get('bucket_name')
            stack_name = request.form.get('stack_name')
            # Call the backend function to create the bucket
            result, outputs = backend.create_bucket(environment, region, bucket_name, stack_name)
            result = result.replace('\n', '<br>')
            outputs = str(outputs).replace('\n', '<br>')
            return f"{result}<br>{outputs}"
        except Exception as e:
            error_message = str(e).replace('\n', '<br>')
            return f"Error: {error_message}"
    return render_template('index.html')

@app.route('/destroy', methods=['POST'])
def destroy():
    try:
        environment = request.form.get('environment')
        region = request.form.get('region')
        bucket_name = request.form.get('bucket_name')
        stack_name = request.form.get('stack_name')
        # Call the backend function to destroy the bucket
        result = backend.destroy_bucket(environment, region, bucket_name, stack_name)
        result = result.replace('\n', '<br>')
        return f"{result}"
    except Exception as e:
        error_message = str(e).replace('\n', '<br>')
        return f"Error: {error_message}"

def main():
    port = int(os.getenv('PORT', 8000))
    app.run(debug=True, port=port)

if __name__ == '__main__':
    main()