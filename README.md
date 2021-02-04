# Data Project 2 - Master Data Analytics EDEM

## Equipo

* [Sofía Zander](https://github.com/sozanmen)
* [Vicente Gil](https://github.com/vicentegilso)
* [Jorge Camáñez](https://github.com/jcamcre)
* [Javier Briones](https://github.com/jabrio)
* [Vicent Asensio](https://github.com/viasmo1)

## Program setup

### Clone the repo and run containers

* Git clone the following repo: [edem-mda-DP2-wake](https://github.com/viasmo1/edem-mda-DP2-wake)

```sh
git clone https://github.com/viasmo1/edem-mda-DP1-wake
```

* Go to the repo's folder

```sh
 cd edem-mda-DP2-wake
```

* Run the docker-compose

```sh
docker-compose up -d
```

### Access nifi notebook and run the template

* Go to [localhost:8090/nifi](https://localhost:8090/nifi)

* Upload the template *WakeTeam_DataProject2_NifiTemplate.xml* available in the Nifi folder

* Enter your twitter API credentials in the GetTwitter processor

* Run the workflow

### Access jupyter notebook and run the file

* Go to [localhost:8888](https://localhost:8888)

* Upload the file *DP2-WakeTeam.ipynb*

* Enter your twitter API credentials in the *Twitter authentication cell*

* Run all cells

## CONGRATULATIONS

You're all set! Your clients will start receiving your tweet replies!
