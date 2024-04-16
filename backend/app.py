import ast 
from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import json
from testData import pair_freq_ans

app = Flask(__name__)
CORS(app)

@app.route('/run_code', methods=['POST'])
def run_code():
    # Extract code from request
    data = request.get_json()
    code = data['code']

    # Security considerations: This is a placeholder for actual secure execution
    # You should replace this with a secure execution environment
    try:
        # Execute the code
        # WARNING: Executing code directly is highly insecure and risky
        output = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT, text=True)
        # output_str = str(output)
        # return jsonify({'output': output_str}), 200
        return output.strip() 
    except subprocess.CalledProcessError as e:
        # Specific error message for subprocess.CalledProcessError
        error_message = 'Error: {}'.format(e.output)
        return jsonify({'error': error_message}), 500
    except Exception as e:
        # General error message for other exceptions
        error_message = 'Error: {}'.format(e)
        return jsonify({'error': error_message}), 500
    
@app.route('/run_code_check', methods=['POST'])
def run_code_check():
    # Extract code from request
    data = request.get_json()
    code = data['code']

    # Security considerations: This is a placeholder for actual secure execution
    # You should replace this with a secure execution environment
    try:
        # Execute the code
        # WARNING: Executing code directly is highly insecure and risky
        # pair_freq_ans = {1,2,3}
        output = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT, text=True)
        code_output = ast.literal_eval(output)
        print('user output', code_output, type(code_output))
        print('correct output', pair_freq_ans, type(pair_freq_ans))
        print('same?',pair_freq_ans == code_output)
        if pair_freq_ans == code_output: 
            return jsonify({'success': True, 'result': output.strip()})
        else: 
            return jsonify({'success': False, 'result': output.strip()})
    except subprocess.CalledProcessError as e:
        # Specific error message for subprocess.CalledProcessError
        error_message = 'Error: {}'.format(e.output)
        return jsonify({'error': error_message}), 500
    except Exception as e:
        # General error message for other exceptions
        error_message = 'Error: {}'.format(e)
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
