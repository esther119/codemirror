import ast 
from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import json
from getFunctionName import get_function_name, extract_function
from testData import answers, pair_freq_ans

app = Flask(__name__)
CORS(app)

@app.route('/run_code', methods=['POST'])
def run_code():
    # Extract code from request
    data = request.get_json()
    code = data['code']

    try:
        # Execute the code
        # WARNING: Executing code directly is highly insecure and risky
        output = subprocess.check_output(['python3', '-c', code], stderr=subprocess.STDOUT, text=True)
        return output.strip(), 200
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
    code_str = extract_function(code)
    function_name = get_function_name(code)
    if function_name in answers: 
        test_cases = answers[function_name]['test_cases']
        correct_answers = answers[function_name]['correct_answers']
    else: 
        return jsonify({'success': False, 'result': 'incorrect function name'})    
    
    try:
        for i, test_case in enumerate(test_cases):
            
            new_code_str = code_str+ f"\nprint({function_name}({test_case}))\n"
            # print('code str', new_code_str)
            try:
                # Execute the code with the current test case inputs
                # print(f'start for test case {i}', input_data)
                output_str = subprocess.check_output(['python3', '-c', new_code_str], stderr=subprocess.STDOUT, text=True)
                output = ast.literal_eval(output_str) #parse back to whatever python object

                # print(f'output for test case {i}', type(output),output)
                # Compare the output with the expected answer
                if output== correct_answers[i]:  # Assuming correct_answers is a list of strings
                    print(f'Test case {i}: Passed')
                else:
                    print(f'Test case {i}: Failed')
                    return jsonify({'success': False, 'result': f'failed test case {i}: {test_case}'})
            except subprocess.CalledProcessError as e:
                print(f'Error executing test case {i+1}: {e.output_str}')        
            
        return jsonify({'success': True, 'result': '👍'}), 200
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
