# Deploying Flask and React

Structure folder
```
📦deploying-structure-flask-react
 ┣ 📂api
 ┣ 📂build
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📜main.e45d1cc0.chunk.css
 ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┣ 📜2.9ecfb76c.chunk.js
 ┃ ┃ ┃ ┣ 📜2.9ecfb76c.chunk.js.LICENSE.txt
 ┃ ┃ ┃ ┣ 📜main.8eab8b9a.chunk.js
 ┃ ┃ ┃ ┗ 📜runtime-main.83c3e0c4.js
 ┃ ┣ 📜asset-manifest.json
 ┃ ┣ 📜favicon.ico
 ┃ ┣ 📜index.html
 ┃ ┣ 📜logo192.png
 ┃ ┣ 📜logo512.png
 ┃ ┣ 📜manifest.json
 ┃ ┣ 📜precache-manifest.725ffa00339cc9f27857182ad03035c9.js
 ┃ ┣ 📜robots.txt
 ┃ ┗ 📜service-worker.js
 ┣ 📂config
 ┣ 📂controllers
 ┣ 📂key
 ┣ 📂models
 ┣ 📂security
 ┣ 📂services
 ┣ 📜.gitignore
 ┣ 📜Procfile
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜server.py
```
## Install 
```
pip install -r requirements.txt
python server.py
```
## How to create build folder
run ``` npm run-script build ``` from react project, after copy ``` build ``` folder to project ``` flask``` as folder structure


