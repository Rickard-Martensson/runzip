# Runzip


## Installation

1. Clone this repo:

```bash
git clone https://github.com/Rickard-Martensson/runzip.git

```
2. Navigate to the `runzip` folder

```bash
cd runzip
```

3. Make script executable

```bash
chmod +x runzip.py
```

## Setup
Create a symlink to make runzip accessible from any directory:

```bash
sudo ln -s /path/to/your/runzip/runzip.py /usr/local/bin/runzip
```

Replace `/path/to/your/runzip.py` with the actual path where you have `runzip.py`.

For me, that is `/home/rickard/Code/python/runzip/runzip.py`

## Usage

To unzip a file, simply type


```bash
runzip <filename>
```

## Supported File Types
- .zip
- .tar
- .gz
- .tar.bz2

## Contributing

I welcome contributions to enhance the functionality and usefulness of this project. If you're interested in contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request, describing the changes you've made.
5. Our team will review the pull request and provide feedback.

I appreciate your contributions and efforts in making this project better!


## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code according to the terms of the license.

## Acknowledgments

I'd like to express my gratidude to [Rickard Mårtensson](www.ric.ke) for making all of this when I was annoyed. I'm sure there are better solutions out there but you know.
