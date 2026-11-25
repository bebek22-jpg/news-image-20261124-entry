# The World in One Day — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/bebek22-jpg/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/bebek22-jpg/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for make.fun's **news-image-20261124** — [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124) ($100 shared by the top 50).

## The image

A newspaper front page for **Tuesday, 24 November 2026**, drawn from that day's
reporting:

- **Lead — Huawei found guilty.** A U.S. jury convicts the Chinese telecom
  giant of stealing trade secrets and bank fraud, but clears it of racketeering.
- **Middle East — four tankers hit by mines** in the Strait of Hormuz; the IRGC
  claims a strike on a container ship.
- **Tech — Huang is back at Nvidia.** Jensen Huang is reinstated as CEO days
  after resigning.
- **War — Ukraine hits Russian ships.** Drone strikes on the Sparta II in the
  Gulf of Finland and off Libya; a new analysis puts Russian dead above 700,000.
- **Gaza — Hamas security chief killed** in an Israeli airstrike.
- **Space — NATO warns of a "nuclear satellite"** after reports Russia is
  readying a nuclear-armed satellite.
- **World — Turkish helicopter crash kills 5** in western Turkiye.
- **Markets** — S&P 500 +4.7%, Nasdaq +6.5%, Nikkei +3.9%, Brent $86.70.
  Also: Senegal retakes the Africa Cup, a 5.6 quake hits Nepal, Germany is
  first to use Ukraine's Delta system.

## How it runs

`main.py` (Python 3.13, standard library only) copies the finished image
(`entry.png`, 1024×1024 PNG) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`). No network; the output bytes are identical on
every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
