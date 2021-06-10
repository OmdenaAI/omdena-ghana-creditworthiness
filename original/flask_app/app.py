from flask import Flask, render_template, request, jsonify
import os
import json
import pandas as pd

# Creating Flask APP
app = Flask(__name__)

app.config['SECRET_KEY'] = '^%huYtFd90;90jjj'
app.config['UPLOADED_FILES'] = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}


@app.route('/')
def main():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_columns_numerical(filename):
    try:
        columns = []
        extension = filename.rsplit('.', 1)[1].lower()
        data = None
        if extension == 'csv':
            data = pd.read_csv(filename)
        elif extension == 'xlsx':
            data = pd.read_xlsx(filename)
        for column in list(data.columns):
            try:
                data[column].astype('float')
                columns.append(column)
            except:
                continue
        print(columns)
        return list(columns)
    except:
        return []


def get_columns_categorical(filename):
    try:
        columns = []
        extension = filename.rsplit('.', 1)[1].lower()
        data = None
        if extension == 'csv':
            data = pd.read_csv(filename)
        elif extension == 'xlsx':
            data = pd.read_xlsx(filename)
        for column in list(data.columns):
            try:
                if data[column].dtype == int or data[column].dtype == float:
                    print('Numeric Column')
                data[column].astype('object')
                columns.append(column)
            except:
                continue            
        return list(columns)
    except:
        return []


@app.route('/upload', methods=['POST'])
def success():
    if request.method == 'POST':
        numerical_file = categorical_file = target_file = None
        response = {}
        if 'numeric_file' in request.files:
            numerical_file = request.files['numeric_file']
            if numerical_file and allowed_file(numerical_file.filename):
                numerical_file_name = os.path.join(
                    app.config['UPLOADED_FILES'], 'numerical.' + numerical_file.filename.rsplit('.', 1)[1].lower())
                numerical_file.save(numerical_file_name)
                response['numeric_file'] = numerical_file.filename
                response['numeric_columns'] = get_columns_numerical(
                    numerical_file_name)
            else:
                response['numeric_file_error'] = "Numeric File not Uploaded !"
        if 'category_file' in request.files:
            categorical_file = request.files['category_file']
            if categorical_file and allowed_file(categorical_file.filename):
                categorical_file_name = os.path.join(
                    app.config['UPLOADED_FILES'], 'categorical.' + numerical_file.filename.rsplit('.', 1)[1].lower())
                categorical_file.save(categorical_file_name)
                response['category_file'] = categorical_file.filename
                response['category_columns'] = get_columns_categorical(
                    categorical_file_name)
            else:
                response['category_file_error'] = "Category File not Uploaded !"
        if 'target_file' in request.files:
            target_file = request.files['target_file']
            if target_file and allowed_file(target_file.filename):
                target_file_name = os.path.join(
                    app.config['UPLOADED_FILES'], 'target.' + target_file.filename.rsplit('.', 1)[1].lower())
                target_file.save(target_file_name)
                response['target_file'] = target_file.filename
            else:
                response['target_file_error'] = "Target File not Uploaded !"
        return jsonify(json.dumps(response))


if __name__ == '__main__':
    app.run(debug=True)
