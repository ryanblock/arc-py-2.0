# Architect Python 2.0 demo

## Get started

**Have installed**

- Python >= 3.7 + pip (recent)
- Node.js

**Run**
- `npm i`
- `pip3 install -r requirements.txt`


## Cross-runtime session support

- Start Sandbox: `npm run sandbox`
- Visit `http://localhost:3333` (Python), note the session visit count increment
- Then visit `http://localhost:3333/node`, note the session visit count carries over and continues incrementing


## Python treeshaking

- Run `npx arc hydrate`
- Open `src/htt/get-index/vendor/` to see the automatically installed Python deps
