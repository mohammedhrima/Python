#!/bin/bash

init() {
  clean
  
  if [ ! -f "requirements.txt" ]; then
    touch "requirements.txt"
  fi

  if [ ! -f "./src/__main__.py" ]; then
    mkdir -p ./src
    echo "print(\"Hello World\")" > "./src/__main__.py"
  fi

  if [ ! -f ".gitignore" ]; then
    cat <<EOF > .gitignore
*.pyc
*.pyo
*.pyd
__pycache__
venv/
.vscode/
.idea/
.DS_Store
*.log
*.sqlite3
EOF
  fi

  python3 -m venv venv
  ./venv/bin/pip install -r requirements.txt
  touch ./venv/bin/activate
  source ./venv/bin/activate
}

run() {
  ./venv/bin/python3 ./src
}

freeze() {
  ./venv/bin/pip freeze > requirements.txt
}

clean() {
  rm -rf __pycache__
  rm -rf venv
}

install() {
  if [ ! -f "venv/bin/activate" ]; then
    init
  fi

  if [ $# -eq 0 ]; then
    echo "Please specify at least one package to install."
    return 1
  fi

  for package in "$@"; do
    ./venv/bin/pip install "$package"
  done

  ./venv/bin/pip freeze > requirements.txt
}

init