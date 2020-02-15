# IIT_CareerFair_Crawler

This is a simple web crawler design for scraping the employers information of "2020 Spring IIT CareerFair" on the Fair Apps.

## Installation

Use the [pipenv](https://pipenv.kennethreitz.org/en/latest/#) to manage and install the Python packages.

```bash
pipenv install
```

To handle the Javascript, we need a headless borwser [splash](https://splash.readthedocs.io/en/stable/#).

1. Install [Docker](http://docker.io) for the OS you are using.

2. Pull the image:

```bash
sudo docker pull scrapinghub/splash
```

## Usage

Start the Splash container

```bash
sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
```

Run the following command under top `/careerSpider` folder.

```bash
scrapy crawl careerfair_spider -o OUTPUTFILE_NAME.csv
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)