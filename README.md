# pixels_analysis

An analysis tool for the [Pixels](https://play.google.com/store/apps/details?id=ar.teovogel.yip&hl=en&gl=US) app.

Pixels is a daily mood tracker and journal, but it provides poor in-app analytics.
This project aims to provide a way to search for keywords within pixels and visualise
keyword frequency.

Each day also links to the google maps timeline, which, if enabled, will show your location history
on the given day and provide some context to your pixels journal.

## How to use
~~Download the project as ZIP and open index.html with your browser.~~  
No need to download! Project is available at [plojyon.github.io/pixels_analysis](https://plojyon.github.io/pixels_analysis)  
You'll need to paste your pixels backup JSON file when queried. No data is being collected. Pinky promise.

Alternatively (and preferably) you can create a new file called `data.json` next
to index.html, and enter `data = '<your JSON data>'` (without <>).  
Make sure you escape special characters by running a search and replace:  
`\` -> `\\` and `'` -> `\'`  
(you need to download the project for this variant)

### P.S.
To change which years are displayed (default is 2019 and 2020, add or remove them in `index.html` on line 69)

Mood colours (palette) can also be changed on lines 50-65.
