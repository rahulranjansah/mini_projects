import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    link = re.search(r"(?:<iframe)?(?:width=\"[0-9]{1,4}\")?(?:height=\"[0-9]{1,4}\")?(?:src=)?\"?(https?://)(?:www\.)?(?:youtube\.){1}com/embed/([A-Za-z0-9]*)\"?(?:title=\"YouTube video player\" frameborder=\"[0-9]{1,3}\" allow=\"acclerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen)?(?:></iframe>)?", s)
    if link:
        shorten = link.group(1) + "youtu.be/" + link.group(2)
        return shorten

    else:
        return None

if __name__ == "__main__":
    main()
