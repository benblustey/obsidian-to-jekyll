# Obsidian 2 Jekyll

This is a simple python script that converts [Obsidian](https://obsidian.md/) notes to a format that is compatible with [Jekyll](https://jekyllrb.com/) theme Chirpy.

## Prerequisites

* [Python3](https://www.python.org/downloads/) installation.

## Usage Instructions

### Converting

To convert your vault into Jekyll markdown, run

```
python3 [OBSIDIAN_VAULT_DIR] [OUTPUT_DIR]
```

### How I Use This Script

I simply have a folder within a Obsidian Vault called posts. When I have completed a note or post, I copy or move that note from its current folder into the posts folder. 

* 

## Limitations

* (TODO) obsidian aliases do not work atm
* duplicate filenames - when there are two notes with the same name, only one will be copied to the destination directory
* copy only the updated or recently changed files
* get tags working correctly
* add the preview image to the frontmatter

## Obsidian => Jekyll Pipline

This script is part of my selfmade Obsidian publish setup, which is roughly outlined below. For automatic publishing, I have my Obsidian Vault backed up in iCloud which is synced onto my unraid server using the CA [icloud-drive-sync](https://hub.docker.com/r/mandarons/icloud-drive) that runs once a day.

The setup consists of 2 separate repositories:
* obsidian-to-jekyll (this one)
* Jekyll Serve (the repository of the Jekyll instance)


```
obsidian-publish
├── obsidian-to-jekyll
├── jekyll-directory
└── obsidian-vault
```

Yada yada explain the pipeline once built out.

```
Add Pipeline Instructions Here
```

## Authors

- **Benjamin Steyaert** [BStey](https://github.com/BenBluStey) [website](https://benjamin-steyaert.com/)
