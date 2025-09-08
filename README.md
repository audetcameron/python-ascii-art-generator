# ASCII Art Generator

Use an existing .png image (Chat GPT or AI generated if needed)

## Setup
Download this repo or clone it
Terminal / cd into this folder

For OSX using pythong3

### Create a new venv (Virtual Environment)

```bash
python3 -m venv ascii 
```

Note the venv is called ascii (this will create a folder called ascii)

### Activate the venv:

```bash
source ascii/bin/activate
```

### Install the reqirements.txt

```bash
pip install -r requirements.txt
```


## Usage
Add any images to the /images folder as .png  eg: cat.png
skeleton.png is included as an example

Run main.py with a filename *(exclude the extension)*

```python
python3 main.py yourfilename 
```

eg:
```python
python3 main.py skeleton 
```

## Result
Ascii art text files are created in the /ascii-art/yourfilename.txt location

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)