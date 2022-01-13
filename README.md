# xenovaping

Unofficial service which sends you an email when you can get the payback of your trips done with the Xente Nova card. 
An instance hosted by me its avaliable at [xenovaping.peprolinbot.com](https://xenovaping.peprolinbot.com/).

## 🔧 Deploy it yourself

### 🐳 Docker (Recommended)

If you want to host this yourself, you probbably know the way, but just in case here are some nice, little, simple instrunctions on how to do it using docker-compose:

```bash
# Create a directory and enter it
mkdir xenovaping
cd xenovaping

# Download docker-compose.yml
curl -O https://raw.githubusercontent.com/peprolinbot/xenovaping/main/docker-compose.yml

# Download .env and edit it
curl -O https://raw.githubusercontent.com/peprolinbot/xenovaping/main/.env.example --output .env
vim .env # Use your favorite text editor. Function of each variable is described below

# Bring up the containers
docker-compose up -d

# The web is now avaliable at port 8080
```

#### Environment Variables

| Name              | Description                                        |
|-------------------|----------------------------------------------------|
| `DB_PASSWORD`     | Set this to a secure password, just in case.       |
| `TPGAL_EMAIL`     | The bus.gal account's email.                       |
| `TPGAL_PASSWORD`  | The bus.gal account's password.                    |
| `CHECK_INTERVAL`  | Interval, in seconds, to wait between card checks. |

#### Build the images

```bash
git clone https://github.com/peprolinbot/xenovaping.git
cd xenovaping
docker build -t xenovaping:web -f Dockerfile.web .
docker build -t xenovaping:notifications -f Dockerfile.notifications .
```

### 💪🏻 Without Docker

Sorry, I'm not going to write instructions for something no one is going to do and if someone wants to get this running so badly, he/she probably has enough knowledge to do so without my help.

## Disclaimer

This project is not endorsed by, directly affiliated with, maintained by, sponsored by or in any way officially related with la Xunta de Galicia, the bus operators or any of the companies involved in the [bus.gal](https://www.bus.gal/) website and the [app](https://play.google.com/store/apps/details?id=gal.xunta.transportepublico).
